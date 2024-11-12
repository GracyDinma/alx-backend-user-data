#!/usr/bin/env python3
"""
This module defines the BasicAuth class.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth.
    This class is currently empty and serves as a placeholder for future.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Authorization header for a Basic Authentication.

        Args:
            authorization_header (str): Authorization header
            for a Authentication

        Returns:
            str: The Base64 part of the Authorization header.
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
