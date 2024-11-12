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
            - bool: True is the path is authenticated otherwise False
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        # Ensure trailing slashes are consistent for comparison
        path = path if path.endswith('/') else path + '/'

        """
        Returns:
            False if the the path is in the excluded paths
        """
        return not any(excluded_paths == path for
                       excluded_paths in excluded_paths)

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
