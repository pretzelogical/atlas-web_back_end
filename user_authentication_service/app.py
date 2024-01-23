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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
