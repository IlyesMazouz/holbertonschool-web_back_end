#!/usr/bin/env python3

"""Auth module"""

from db import DB
import bcrypt
import uuid  

class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        """Initialize Auth object with a DB instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """Register a new user"""
        hashed_password = self._hash_password(password)
        self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the login is valid"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"), user.hashed_password.encode("utf-8")
            )
        except:
            return False

    def _hash_password(self, password: str) -> str:
        """Hashes a password using bcrypt"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def _generate_uuid(self) -> str:
        """Generate a new UUID"""
        return str(uuid.uuid4())  