#!/usr/bin/env python3
"""
Auth class for API authentication.
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ _summary_
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.

        Args:
            path: The requested URL path.
            excluded_paths: List of paths where authentication is not required

        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header

        Args:
            request: The Flask request object.

        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Display current user from the request.

        Args:
            request: The Flask request object.

        Returns:
            None
        """

        return None
