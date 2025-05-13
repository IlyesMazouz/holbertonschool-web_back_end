#!/usr/bin/env python3
"""
This module provides an authentication class to manage user-related operations
such as registration and login validation using hashed passwords.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    The Auth class is responsible for handling all
    authentication logic, including
    user registration and validating login credentials.
    """

    def __init__(self) -> None:
        """
        Initialize the Auth class with a database connection.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user by storing their email and a hashed password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user credentials by checking if the
        user exists and if the password
        matches the hashed password stored in the database.
        """
        try:
            user: User = self._db.find_user_by(email=email)
        except Exception:
            return False

        if not user or not user.hashed_password:
            return False

        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with automatic salt generation.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
