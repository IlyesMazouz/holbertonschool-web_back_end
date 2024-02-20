#!/usr/bin/env python3

"""
A hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the given password using bcrypt
    """
    password_bytes = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password.
    """
    password_bytes = password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hashed_password)
