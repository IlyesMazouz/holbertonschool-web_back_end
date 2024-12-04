#!/usr/bin/env python3
"""
Module for hashing passwords.

"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password string using bcrypt with a salt.

    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_password
