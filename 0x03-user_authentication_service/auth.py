#!/usr/bin/env python3
"""
Define _hash_password method.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import hashpw, gensalt


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The newly created user object.

        Raises:
            valueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            # if no exception is raised, user exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # User does not exist; proceed with registration
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            self._db._session.rollback()
            return new_user

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """
        Hash a password using bcrypt.

        Args:
            password (str): The plain text password to hash.

        Returns:
            bytes: The hashed password as bytes.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
