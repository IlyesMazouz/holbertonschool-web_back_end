#!/usr/bin/env python3
"""
DB class for handling database operations
"""
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from user import User


class DB:
    """
    DB class for handling user authentication and database operations
    """

    def __init__(self):
        """Initialize the DB class"""
        self.engine = create_engine("sqlite:///users.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        User.__table__.create(self.engine, checkfirst=True)

    def add_user(self, email: str, hashed_password: str):
        """Add a new user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def find_user_by(self, **kwargs):
        """Find user by arbitrary keyword arguments"""
        try:
            user = self.session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("User not found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")
