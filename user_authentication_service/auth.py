#!/usr/bin/env python3
"""
Auth class for handling user authentication logic.
"""
from uuid import uuid4
from typing import Type
from models.user import User
from models.base import Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session


class Auth:
    """
    Auth class to manage user authentication.
    """

    def __init__(self):
        """
        Initialize the Auth class.
        """
        self._db = Base.session

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID.
        """
        return str(uuid4())

    def create_session(self, email: str) -> str:
        """
        Create a session for the user based on email.
        """
        user = self._db.query(User).filter_by(email=email).first()
        if user:
            session_id = self._generate_uuid()
            user.session_id = session_id
            self._db.commit()
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> Type[User]:
        """
        Returns the user corresponding to the session_id, or None if not found.
        """
        if not session_id:
            return None

        try:
            user = self._db.query(User).filter_by(session_id=session_id).one()
            return user
        except NoResultFound:
            return None

    def valid_login(self, email: str, password: str) -> Type[User]:
        """
        Validate login credentials.
        """
        user = self._db.query(User).filter_by(email=email).first()
        if user and user.password == password:
            return user
        return None
