#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth

    auth = Auth()


@app.before_request
def before_request():
    """Before request handler"""
    if auth is None:
        return

    excluded_paths = ["/api/v1/status/", "/api/v1/unauthorized/", "/api/v1/forbidden/"]
    if request.path in excluded_paths:
        return

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(make_response(jsonify({"error": "Unauthorized"}), 401))

    if auth.current_user(request) is None:
        abort(make_response(jsonify({"error": "Forbidden"}), 403))


@app.errorhandler(404)
def not_found(error):
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
