#!/usr/bin/env python3
"""
Authentication module for handling user registration and sessions.
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Class to manage user authentication.
    """

    def __init__(self) -> None:
        """
        Initialize Auth with a database instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user with email and hashed password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials.
        """
        try:
            user: User = self._db.find_user_by(email=email)
        except Exception:
            return False

        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        Create a new session ID for a user and store it.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a password reset token for the user.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User not found")

        reset_token = _generate_uuid()

        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token


def _hash_password(password: str) -> bytes:
    """
    Return the bcrypt hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Return a new UUID string.
    """
    return str(uuid.uuid4())
