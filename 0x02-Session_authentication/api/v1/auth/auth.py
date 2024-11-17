#!/usr/bin/env python3
"""
Auth class for API authentication.
"""

import os
from flask import request
from typing import List, TypeVar


class Auth:
    """ _summary_
    """

    def session_cookie(self, request=None):
        """
        Update method that returns a cookie value from a request

        Args:   request: Flask request object

        Returns:
            The value of the session cookie or None if not found
        """
        if request is None:
            return None

        # Get the name of the session cookie from env
        session_name = os.getenv('SESSION_NAME')

        if not session_name:
            return None

        # Return the value of the session cookie using .get()
        return request.cookies.get(session_name)

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

        # Allow * at the end of excluded paths.
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                """ For paths ending with *, check if the path
                start with the prefix."""

                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                # If there's an exact match with the path, no auth
                return False

        # if no match is found, auth is required
        return True

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the Authorization header, or None if not present
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Display current user from the request.

        Args:
            request: The Flask request object.

        Returns:
            None
        """

        return None
