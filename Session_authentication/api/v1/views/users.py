#!/usr/bin/env python3
"""User views"""
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id: str):
    """Get a user by ID or 'me' for the current user"""
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())
