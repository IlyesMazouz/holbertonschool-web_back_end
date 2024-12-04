#!/usr/bin/env python3
"""
Main API file that includes the routes and handlers for user authentication.
"""

from flask import Flask, request, jsonify, abort
from models.user import User
from auth import Auth

app = Flask(__name__)

auth = Auth()


@app.route("/sessions", methods=["POST"])
def login():
    """
    Logs in a user, creates a session, and returns a JSON response.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, "Email and password are required")

    user = auth.login_user(email, password)
    if user is None:
        abort(401)

    session_id = auth.create_session(user.id)

    response = jsonify({"email": user.email, "message": "logged in"})

    response.set_cookie("session_id", session_id)

    return response


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


@app.route("/profile", methods=["GET"])
def profile():
    """
    Returns the profile information of the logged-in user.
    Expects the session_id as a cookie in the request.
    """
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)  # No session ID provided in the cookie

    user = auth.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route("/")
def home():
    """
    Home route (GET /), could be used for a landing page or a check.
    """
    return "Welcome to the Home Page", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
