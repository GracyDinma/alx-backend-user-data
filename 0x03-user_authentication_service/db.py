#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created user object.
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
            return user
        except Exception as e:
            self._session.rollback(
                    raise RuntimeError(f"Error adding user: {e}") from e

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first row in the user by given attributes.
        Args:
            kwargs: Arbitrary keyword arguments.
        Returns:
            User: The found user object.

        Raises:
            NoResultFound: if no matching record is found.
            InvalidRequestError: If the query arguments are invalid.
        """

        for attr in kwargs.keys():
            if not hasattr(User, attr):
                raise InvalidRequestError(f"Invalid attribute: {attr}
