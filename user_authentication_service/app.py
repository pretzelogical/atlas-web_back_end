#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, jsonify, request, make_response
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


@app.route('/session', methods=["POST"], strict_slashes=False)
def session():
    """ Create session """
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    return make_response(jsonify({"message": "wrong email or password"}), 401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
