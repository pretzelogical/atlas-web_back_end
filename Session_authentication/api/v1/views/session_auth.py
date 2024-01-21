#!/usr/bin/env python3
""" Session authentication module """
from api.v1.views import app_views
from flask import request, jsonify, make_response, abort
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
        Session authentication login
    """
    usr_email = request.form.get('email', None)
    usr_pass = request.form.get('password', None)
    if usr_email is None:
        return make_response(jsonify({"error": "email missing"}), 400)
    if usr_pass is None:
        return make_response(jsonify({"error": "password missing"}), 400)
    users = User.search({'email': usr_email})
    if users == []:
        return make_response(
            jsonify({"error": "no user found for this email"}), 404)
    valid_user = None
    for user in users:
        if user.is_valid_password(usr_pass):
            valid_user = user
            break
    if valid_user is None:
        return make_response(jsonify({"error": "wrong password"}), 401)
    from api.v1.app import auth
    session_id = auth.create_session(valid_user.id)
    response = make_response(jsonify(valid_user.to_json()))
    response.set_cookie(os.environ.get('SESSION_NAME', '_my_session_id'),
                        session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
        End a session by removing the session id
    """
    from api.v1.app import auth
    dest_res = auth.destroy_session(request)
    if dest_res is False:
        abort(404)
    return make_response(jsonify({}), 200)
