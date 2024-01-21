#!/usr/bin/env python3
""" Authentication module that works on a session basis """
from api.v1.auth.auth import Auth
from models.user import User
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
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def destroy_session(self, request=None):
        """
            Deletes the user session
        """
        if request is None:
            return False
        ses_cookie = self.session_cookie(request)
        if ses_cookie is None:
            return False
        usr_id = self.user_id_for_session_id(ses_cookie)
        if usr_id is None:
            return False
        del self.user_id_by_session_id[usr_id]
        return True

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Returns a User ID based on the session_id
            : session_id(str) : the session id to search for
            : return(str) : the user id
        """
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
            Returns a User instance based on a cookie value
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
