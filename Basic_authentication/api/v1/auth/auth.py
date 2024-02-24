#!/usr/bin/env python3
""" Module containing the Auth class for API authentication """
from typing import List, TypeVar
from flask import Request


class Auth:
    """Auth class for managing API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if authentication is required for a given path
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip("/") + "/"
        excluded_paths = [p.rstrip("/") + "/" for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request: Request = None) -> str:
        """
        Method to extract the authorization header from the request
        """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request: Request = None) -> TypeVar("User"):
        """
        Method to retrieve the current authenticated user
        """
        return None
