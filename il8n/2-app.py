#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


app = Flask(__name__)


class Config:
    """ Class that holds configuration values for babel """
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the locale for the current request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def root():
    """ Root route """
    return render_template("0-index.html")


if __name__ == "__main__":
    host = getenv("BASIC_HOST", "localhost")
    port = getenv("BASIC_PORT", "5000")
    app.run(host, port)
