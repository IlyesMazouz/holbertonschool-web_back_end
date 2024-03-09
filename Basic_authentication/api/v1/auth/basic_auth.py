#!/usr/bin/env python3
"""
Module containing the BasicAuth class for Basic Authentication
"""
import base64
from typing import TypeVar
from models.user import User


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
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieve the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header
        )
        if decoded_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user


if __name__ == "__main__":
    a = BasicAuth()
