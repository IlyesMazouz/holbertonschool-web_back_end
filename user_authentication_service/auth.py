#!/usr/bin/env python3

"""Auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


if __name__ == "__main__":
    print(_hash_password("Hello Holberton"))
