#!/usr/bin/env python3
"""
Module containing the BasicAuth class for basic authentication
"""


class BasicAuth(Auth):
    """BasicAuth class for managing basic authentication"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header for Basic Authentication
        """
        if base64_authorization_header is None or (
            type(base64_authorization_header) != str
        ):
            return None
        try:
            decodeBytes = base64.b64decode(base64_authorization_header)
            decodedStr = decodeBytes.decode("utf-8")
            return decodedStr
        except ValueError:
            return None
