#!/usr/bin/env python3
"""
This module defines the BasicAuth class.
"""

from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        A method that returns the decoded value of a Base64 string
        base64_authorization_header.

        Args:
            base64_authorization_header: value of a Base64 string

        Returns:
            str: Decoded value of a Base64 string.
        """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            """ Decode the Base64 string."""
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            """ Return None if decoding fails."""
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        A method that returns the user email and password from
        the Base64 decoded value.

        Args:
            decoded_base64_authorization_header: value of Base64

        Returns:
            tuple: user email and password.
        """

        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        """ Split the string at the first occurence of ':'."""
        user_email, user_password = decoded_base64_authorization_header.split(
                                    ':', 1)
        return user_email, user_password
