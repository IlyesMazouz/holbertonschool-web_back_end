#!/usr/bin/env python3
"""
Auth module for handling user authentication logic.
"""

import uuid
import bcrypt


class Auth:
    def __init__(self):
        """Initializes the Auth class."""
        pass

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return it as a string.
        """
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> str:
        """
        Registers a new user by email and password.

        """
        user_id = self._generate_uuid()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        return user_id

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates the login credentials for a user
        """
        stored_password_hash = b"$2b$12$somehashedpasswordhere"

        return bcrypt.checkpw(password.encode("utf-8"), stored_password_hash)
