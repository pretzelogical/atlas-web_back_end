#!/usr/bin/env python3
""" Using bcrypt to encrypt and check passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string. """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the provided password matches the hashed password. """
    return bcrypt.checkpw(password.encode(), hashed_password)
