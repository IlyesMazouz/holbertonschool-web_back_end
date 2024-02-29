#!/usr/bin/env python3
"""
Module containing the BasicAuth class for Basic Authentication
"""
from typing import TypeVar


class BasicAuth:
    """
    BasicAuth class for managing Basic Authentication
    """

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Check if authentication is required for a given path
        """
        pass

    def authorization_header(self, request=None) -> str:
        """
        Extract the authorization header from the request
        """
        pass

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieve the current authenticated user
        """
        pass

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header for Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]


if __name__ == "__main__":
    a = BasicAuth()
