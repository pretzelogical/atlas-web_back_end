#!/usr/bin/env python3
""" Basic authentication module """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str):
        """ Extracts the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str):
        """ Decodes the Base64 part of the Authorization header """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return (base64.b64decode(base64_authorization_header)
                    .decode('utf-8'))
        except Exception:
            return None
