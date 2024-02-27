#!/usr/bin/env python3
"""
app.py
"""
from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/users", methods=["POST"])
def register_user():
    """Endpoint to register a new user"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as err:
        return jsonify({"message": str(err)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
