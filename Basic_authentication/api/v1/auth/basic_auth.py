#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar
import base64
from models.user import User


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication."""
        if path is None or excluded_paths is None:
            return True

        for excluded_path in excluded_paths:
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
        """Retrieves the current user from the request based on Basic Auth."""
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header
        )
        if base64_authorization_header is None:
            return None

        decoded_base64_authorization_header = self.decode_base64_authorization_header(
            base64_authorization_header
        )
        if decoded_base64_authorization_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_authorization_header
        )
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the Base64 string."""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extracts the user email and password from the decoded Base64 string."""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """Retrieves the User instance based on email and password."""
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        if user_email is None or user_pwd is None:
            return None

        user = User.search({"email": user_email})
        if not user:
            return None

        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
