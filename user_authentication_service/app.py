#!/usr/bin/env python3
""" Basic flask app """
from flask import (Flask, jsonify, request, make_response,
                   abort, redirect, url_for)
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def root_route():
    """ Root route """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """ Create user """
    try:
        AUTH.register_user(request.form.get("email", ""),
                           request.form.get("password", ""))
        return jsonify({
            "email": request.form.get("email", ""),
            "message": "user created"
        })
    except ValueError:
        return make_response(jsonify(
            {"messsage": "email already registered"}
        ), 400)


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def session():
    """ Create session """
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logout session and redirect to / """
    session_id = request.cookies.get("session_id", "")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user_id=user.id)
    return redirect(url_for('root_route'))


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile():
    """ Get profile """
    session_id = request.cookies.get("session_id", "")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Get reset password token """
    email = request.form.get("email", "")
    try:
        reset_pass = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({
        "email": email,
        "reset_token": reset_pass
    })


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update password """
    email = request.form.get("email", "")
    reset_token = request.form.get("reset_token", "")
    new_password = request.form.get("new_password", "")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({
            "email": email,
            "message": "Password updated"
        })
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
