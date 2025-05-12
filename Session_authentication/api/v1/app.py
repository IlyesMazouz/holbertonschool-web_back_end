#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from flask_cors import CORS
import os
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)

auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()


@app.before_request
def before_request():
    """Filter requests before processing"""
    if auth is None:
        return
    excluded = ["/api/v1/status/", "/api/v1/unauthorized/", "/api/v1/forbidden/"]

    if request.path in excluded:
        return
    if not auth.require_auth(request.path, excluded):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)
