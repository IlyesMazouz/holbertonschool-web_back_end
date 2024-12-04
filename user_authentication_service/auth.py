#!/usr/bin/env python3
"""
Auth class for handling user authentication logic.
"""

from models.user import User
from models.base import Base
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Type, Union
from sqlalchemy.orm.session import Session


class Auth:
    """
    Auth class to manage user authentication.
    """

    def __init__(self):
        """
        Initialize the Auth class with a session.
        """
        self._db = Session()

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID for the session.
        """
        return str(uuid4())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user in the system.
        """
        user = User(email=email, password=password)
        self._db.add(user)
        self._db.commit()
        return user

    def create_session(self, email: str) -> Union[str, None]:
        """
        Create a session for a given user by email.
        """
        user = self._db.query(User).filter_by(email=email).first()
        if not user:
            return None
        session_id = self._generate_uuid()
        user.session_id = session_id
        self._db.commit()
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Return the user associated with the given session ID.
        """
        if not session_id:
            return None
        user = self._db.query(User).filter_by(session_id=session_id).first()
        return user

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys the session for the user by setting session_id to None.
        """
        try:
            user = self._db.query(User).filter_by(id=user_id).one()

            user.session_id = None

            self._db.commit()
        except NoResultFound:
            return None

    def login(self, email: str, password: str) -> Union[dict, None]:
        """
        Login a user by email and password.
        """
        user = self._db.query(User).filter_by(email=email).first()
        if not user or user.password != password:
            return None
        session_id = self.create_session(email)
        if not session_id:
            return None
        return {"email": email, "message": "logged in"}
