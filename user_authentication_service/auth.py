#!/usr/bin/env python3
"""
Generating uuid
"""
import uuid


class Auth:
    def __init__(self):
        pass

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return it as a string.

        """
        return str(uuid.uuid4())
