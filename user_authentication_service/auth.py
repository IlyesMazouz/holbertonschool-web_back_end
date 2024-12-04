#!/usr/bin/env python3
"""
Auth module to handle user authentication logic.
"""

import uuid
from models.user import User
from models.base import Base
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth class to manage user authentication,
    session handling, and password reset.
    """

    def __init__(self):
        """Initializes the Auth object with the database session."""
        self._db = Base()

    def get_user_from_session_id(self, session_id: str):
        """
        Retrieves the user from the session ID.
        """
        if session_id is None:
            return None

        try:
            user = self._db.session.query(User).filter_by(session_id=session_id).one()
        except NoResultFound:
            return None

        return user

    def create_session(self, user_id: int):
        """
        Creates a session for the user and returns the session ID.
        """
        session_id = str(uuid.uuid4())
        user = self._db.session.query(User).filter_by(id=user_id).one()
        user.session_id = session_id
        self._db.session.commit()

        return session_id

    def destroy_session(self, user_id: int):
        """
        Destroys the session of the user.
        """
        user = self._db.session.query(User).filter_by(id=user_id).one()
        user.session_id = None
        self._db.session.commit()

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates and returns a reset password token for the user with the provided email.
        If the user does not exist, raises a ValueError.
        """
        user = self._db.session.query(User).filter_by(email=email).one_or_none()

        if user is None:
            raise ValueError("User not found")

        reset_token = str(uuid.uuid4())
        user.reset_token = reset_token
        self._db.session.commit()

        return reset_token

    def reset_password(self, reset_token: str, new_password: str) -> None:
        """
        Resets the user's password using the reset token.
        """
        user = (
            self._db.session.query(User)
            .filter_by(reset_token=reset_token)
            .one_or_none()
        )

        if user is None:
            raise ValueError("Invalid reset token")

        user.password = new_password
        user.reset_token = None
        self._db.session.commit()
