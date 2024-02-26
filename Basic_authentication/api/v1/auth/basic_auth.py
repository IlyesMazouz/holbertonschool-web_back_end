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
        if authorization_header is None or not isinstance(authorization_header, str) or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]
