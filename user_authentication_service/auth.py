#!/usr/bin/env python3
"""
Module for handling user authentication
"""

from db import DB
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt)

    def register_user(self, email: str, password: str) -> Optional[object]:
        """Register a new user with email and password."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = self._hash_password(password)

        user = self._db.add_user(email, hashed_password.decode("utf-8"))
        return user
