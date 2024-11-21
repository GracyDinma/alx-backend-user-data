#!/usr/bin/env python3
"""
Craetes SQLAlchemy model.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """ Define number of mapped classes in class User.
    Args:
        User - A SQLAlchemy model.
    """

    __tablename__ = 'users'
    """ Table whcih mapping occurs that icludes the table id and
    datatypes of colimns.

    Args:
        id - A unique key
        email - a non-nullable string
        hashed_password - a non-nullable string
        session_id - a nullable string
        reset_token - a nullable string.
    """

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
