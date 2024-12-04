#!/usr/bin/env python3
"""
Main API file that includes the routes and handlers for user authentication.
"""

from flask import Flask, request, redirect, jsonify, abort
from models.user import User
from auth import Auth

app = Flask(__name__)

auth = Auth()


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    Logs out the user by destroying their session.
    Expects the session_id as a cookie in the request.
    """
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = auth.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    auth.destroy_session(user.id)

    return redirect("/")


@app.route("/")
def home():
    """
    Home route (GET /), could be used for a landing page or a check.
    """
    return "Welcome to the Home Page", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
