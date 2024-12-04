#!/usr/bin/env python3
"""
Module for user registration with Flask.
"""
from flask import Flask, request, jsonify
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def users():
    """
    Endpoint to register a new user.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
