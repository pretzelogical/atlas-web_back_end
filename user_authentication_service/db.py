#!/usr/bin/env python3
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
""" DB module """

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
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

    def check_valid_kwargs(self, kwargs: dict) -> bool:
        """ Checks whether kwargs contains user fields """
        fields = set(User.__table__.columns.keys())
        if set(kwargs.keys()).issubset(fields):
            return True
        return False

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds user to db and returns the added user """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs):
        """
            Finds first user in db by kwargs
            Raises NoResultFound if no result are found
            Raises InvalidRequstError if wrong query is passed
        """
        if not kwargs:
            raise InvalidRequestError
        if not self.check_valid_kwargs(kwargs):
            raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update the user by finding the user_id and applying kwargs
            Raises ValueError if wrong update passed
        """
        if not self.check_valid_kwargs(kwargs):
            raise ValueError
        to_update = self.find_user_by(id=user_id)
        for arg in kwargs:
            to_update.__setattr__(arg, kwargs[arg])
        return None
