#!/usr/bin/env python3
"""
Auth class for handling user authentication logic.
"""
import bcrypt


class Auth:
    def __init__(self):
        """
        Initializes the Auth class with an empty user database.
        In a real application, this would interact with a database.
        """
        self.users = {}

    def register_user(self, email: str, password: str) -> None:
        """
        Registers a new user by email and password.
        Password is hashed before storing.
        """
        if email in self.users:
            raise ValueError("User already exists")

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.users[email] = hashed_password

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates login credentials.
        Returns True if the email exists and the
        password is correct, otherwise False.
        """
        if email not in self.users:
            return False

        stored_password_hash = self.users[email]

        if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash):
            return True
        return False
