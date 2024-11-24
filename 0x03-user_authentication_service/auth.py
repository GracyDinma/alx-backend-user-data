#!/usr/bin/env python3
"""
Define _hash_password method.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
