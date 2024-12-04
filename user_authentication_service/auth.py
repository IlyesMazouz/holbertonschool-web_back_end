#!/usr/bin/env python3
"""
Auth class for handling user authentication logic.

"""

import uuid
import bcrypt


class Auth:
    def __init__(self):
        """Initializes the Auth class."""
        self._db = {}

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

        self._db[email] = {
            "user_id": user_id,
            "password": hashed_password,
            "session_id": None,
        }

        return user_id

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates the login credentials for a user.
        """
        if email not in self._db:
            return False

        stored_password_hash = self._db[email]["password"]
        return bcrypt.checkpw(password.encode("utf-8"), stored_password_hash)

    def create_session(self, email: str) -> str:
        """
        Creates a session for the user by generating a new session ID.
        """
        if email not in self._db:
            return None

        session_id = self._generate_uuid()

        self._db[email]["session_id"] = session_id

        return session_id
