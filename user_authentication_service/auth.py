#!/usr/bin/env python3
"""
Module for handling user registration and authentication.
"""

from db import DB
from user import User
from auth_utils import _hash_password
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize Auth instance with a DB connection."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user by email and password."""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)

        user = self._db.add_user(email, hashed_password)

        return user
