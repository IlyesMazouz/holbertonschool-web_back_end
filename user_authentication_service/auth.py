"""Auth module
"""
from db import DB

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """Register a new user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except:
            pass

        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    import bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
