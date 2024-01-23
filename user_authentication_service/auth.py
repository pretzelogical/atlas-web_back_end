#!/usr/bin/env python3
""" Authentication class that uses bcrypt """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Returns a salted hash of the input password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """ Auth class to interact with the authentication database """

    def __init__(self):
        """ Initialize Auth """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user object and returns it """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        try:
            to_validate = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(),
                                  to_validate.hashed_password)
        except NoResultFound:
            return False
