"""
In-memory Flask application used as the System Under Test (SUT).

Started in a background thread by ``features/environment.py`` so that
the ``requests`` library can exercise a real HTTP API during tests.
"""
from __future__ import annotations

import threading
import time
from werkzeug.serving import make_server

from flask import Flask, jsonify, request, Response


def create_app() -> Flask:
    """Factory that builds a fresh Flask app with an in-memory data store."""
    app = Flask(__name__)
    app.config["TESTING"] = True

    # -- in-memory store -------------------------------------------------
    store: dict = {
        "users": {},
        "sequence": 0,
    }

    # -- helpers ---------------------------------------------------------
    def _next_id() -> int:
        """Increments and returns the next sequential user id."""
        store["sequence"] += 1
        return store["sequence"]

    def _find_user(user_id: int):
        """Returns the user dict for ``user_id`` or ``None`` if not found."""
        return store["users"].get(user_id)

    # -- routes ----------------------------------------------------------
    @app.get("/api/health")
    def health():
        """Health check endpoint — returns status and user count."""
        return jsonify(status="ok", users=len(store["users"]))

    @app.get("/api/users")
    def list_users():
        """Lists users with optional pagination via ?page=N&limit=M.

        Returns JSON with ``data`` (array of users) and ``total`` (int).
        """
        page = int(request.args.get("page", "1"))
        limit = int(request.args.get("limit", "10"))
        all_users = list(store["users"].values())
        start = (page - 1) * limit
        return jsonify(data=all_users[start:start + limit], total=len(all_users))

    @app.post("/api/users")
    def create_user():
        """Creates a new user — validates name and email, checks duplicates.

        Returns 201 on success, 400 if name/email missing, 409 if email exists.
        """
        body = request.get_json(silent=True) or {}
        name = body.get("name", "").strip()
        email = body.get("email", "").strip()
        role = body.get("role", "viewer")
        if not name or not email:
            return jsonify(error="name and email are required"), 400
        if any(u["email"] == email for u in store["users"].values()):
            return jsonify(error="email already exists"), 409
        user = {"id": _next_id(), "name": name, "email": email, "role": role}
        store["users"][user["id"]] = user
        return jsonify(user), 201

    @app.get("/api/users/<int:user_id>")
    def get_user(user_id: int):
        """Retrieves a single user by id — returns 404 if not found."""
        user = _find_user(user_id)
        if not user:
            return jsonify(error="not found"), 404
        return jsonify(user)

    @app.delete("/api/users/<int:user_id>")
    def delete_user(user_id: int):
        """Deletes a user by id — returns 204 on success, 404 if not found."""
        if user_id not in store["users"]:
            return jsonify(error="not found"), 404
        del store["users"][user_id]
        return Response(status=204)

    @app.get("/")
    def index():
        """Root endpoint — returns service name and version."""
        return jsonify(service="python-behave-examples", version="1.0.0")

    return app


class ServerThread(threading.Thread):
    """Runs a Flask app in a daemon thread so tests can hit it via HTTP.

    The thread is a daemon so it is automatically killed when the main
    process exits. Use ``shutdown()`` for a clean stop in ``after_all``.
    """

    def __init__(self, app: Flask, host: str = "localhost", port: int = 5000):
        super().__init__(daemon=True)
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self) -> None:
        """Starts serving the Flask app (blocking — runs in the thread)."""
        self.server.serve_forever()

    def shutdown(self) -> None:
        """Stops the Werkzeug server gracefully."""
        self.server.shutdown()


def start_server(host: str = "localhost", port: int = 5000, timeout: float = 5.0) -> ServerThread:
    """Start the SUT server and wait until it responds to /api/health."""
    import requests

    app = create_app()
    thread = ServerThread(app, host, port)
    thread.start()

    base_url = f"http://{host}:{port}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            resp = requests.get(f"{base_url}/api/health", timeout=0.5)
            if resp.ok:
                return thread
        except Exception:
            pass
        time.sleep(0.1)

    thread.shutdown()
    raise RuntimeError("SUT server did not start within timeout")
