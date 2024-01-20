#!/usr/bin/env python3
""" Authentication module that works on a session basis """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Creates a session ID for user_id
            : user_id(str) : the user id to create a session from
            : return(str) : the session id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
