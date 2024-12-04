#!/usr/bin/env python3
"""
Flask application for user authentication.
"""
from flask import Flask, request, jsonify, abort, make_response
from auth import Auth
import uuid

app = Flask(__name__)

auth = Auth()


@app.route("/sessions", methods=["POST"])
def login():
    """
    Handles user login, creates a session, and sets a session cookie.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, description="Missing email or password")

    user = auth.valid_login(email, password)

    if user is None:
        abort(401, description="Unauthorized")

    session_id = auth.create_session(email)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
