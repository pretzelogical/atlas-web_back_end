#!/usr/bin/env python3
""" Authentication module that works on a session basis """
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class """
    def __init__(self) -> None:
        super().__init__()
        print("SessionAuth activated")
