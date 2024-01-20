#!/usr/bin/env python3
""" Auth module for the API """
# from flask import request
from typing import List, TypeVar
# from flask import request
import os


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth method. Slash tolerant"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header method """
        if (request is None or
                request.headers.get('Authorization', None) is None):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Documentation!!! """
        return None

    def session_cookie(self, request=None):
        """
            Returns a cookie value from a request
        """
        if request is None:
            return None
        session_name = os.environ.get('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name, None)
