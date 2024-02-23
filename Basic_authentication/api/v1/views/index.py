#!/usr/bin/env python3
""" Module of Index views
"""
from flask import abort, Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/forbidden', methods=['GET'])
def forbidden_endpoint():
    """Handler for forbidden endpoint."""
    abort(403)
