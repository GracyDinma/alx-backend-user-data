#!/usr/bin/env python3
"""
This module defines the SessionAuth module.
"""

import uuid
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    This class is currently empty and serves as a placeholder for future.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create an instance method that creates a session ID.

        Args:
            user_id (str): The user ID for which the session ID is created.

        Returns:
            str: The session ID if created successfully, otherwise None.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        # Generating a new session Id
        session_id = str(uuid.uuid4())

        # Store the session ID with the associated user ID
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Create an instance method that returns a user ID
        based on a Session ID

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The user ID if found, otherwise None.
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

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

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        A method that reurns the user instance based on his email
        and password.

        Args:
            user_email(str): The user's email address.
            user_pwd(str): The user's password.

        Returns:
            User: The User instance if credentials are valid, otherwise None.
        """

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        """ Search for the user in the databse by email."""
        users = User.search({"email": user_email})
        if not users or len(users) == 0:
            return None

        """ Verify password."""
        user_instance = users[0]
        if not user_instance.is_valid_password(user_pwd):
            return None
        return user_instance

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request.

        Args:
            Request.
        Returns:
            User instance.
        """

        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        """ Decode the Base64 part of the header."""
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if not base64_auth:
            return None

        """ Decode the Base64 string."""
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if not decoded_auth:
            return None

        """ Extract user email and password."""
        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if not user_email or not user_pwd:
            return None

        """ Retrieves and return the User instance."""
        return self.user_object_from_credentials(user_email, user_pwd)
