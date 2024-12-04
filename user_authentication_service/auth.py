#!/usr/bin/env python3
"""
Auth class for handling user authentication logic.

"""

import uuid
import bcrypt


class Auth:
    """
    Auth class handles user authentication related functions.
    """

    def __init__(self):
        """
        Initialize an Auth object with a simple user storage.
        This would typically interface with a database.
        """
        self.users = {}

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return its string representation.

        """
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> None:
        """
        Register a new user with email and password.

        """
        if email in self.users:
            raise ValueError("User already exists")

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        user_id = self._generate_uuid()

        self.users[email] = {"id": user_id, "password": hashed_password}

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates the login for a given email and password.

        """
        if email not in self.users:
            return False

        stored_password = self.users[email]["password"]
        return bcrypt.checkpw(password.encode("utf-8"), stored_password)

    def get_user_id(self, email: str) -> str:
        """
        Retrieves the user ID for the given email.

        """
        if email in self.users:
            return self.users[email]["id"]
        return None
