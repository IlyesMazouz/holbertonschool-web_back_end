#!/usr/bin/env python3
"""
Main API file to handle routes and logic for user authentication
and password reset.
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route("/reset_password", methods=["POST"])
def reset_password():
    """
    Route to generate a reset password token for the given email.
    """
    email = request.form.get("email")

    if not email:
        return jsonify({"error": "email is required"}), 400

    try:
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        return jsonify({"error": "Email not registered"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
