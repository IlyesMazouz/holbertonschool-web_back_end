#!/usr/bin/env python3
"""
Authentication module for handling user registration and login.
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth class for managing user authentication.
    """

    def __init__(self) -> None:
        """
        Initialize Auth with a database instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with an email and hashed password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check if provided email and password match a registered user.
        """
        try:
            user: User = self._db.find_user_by(email=email)
        except Exception:
            return False

        return bcrypt.checkpw(password.encode(), user.hashed_password)


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a new UUID string.
    """
    return str(uuid.uuid4())
