# api/v1/auth/auth.py

from typing import List


class Auth:
    """Auth class for managing API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if authentication is required for a given path.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip("/") + "/"
        excluded_paths = [p.rstrip("/") + "/" for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Method to extract the authorization header from the request
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> str:
        """
        Method to retrieve the current authenticated user
        """
        return None
