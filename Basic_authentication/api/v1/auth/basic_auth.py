#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication."""
        if path is None or excluded_paths is None:
            return True

        for excluded_path in excluded_paths:
            # Split the long line into two for readability
            path_stripped = excluded_path.rstrip("/")
            if path == excluded_path or path.startswith(path_stripped):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Gets the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """Gets the current user (to be implemented in child classes)."""
        return None


class BasicAuth(Auth):
    """BasicAuth class to handle Basic Authentication."""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Extracts the Base64 part of the Authorization header."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
