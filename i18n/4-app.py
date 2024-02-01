#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


class Config:
    """ Class that holds configuration values for babel """
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """ Gets the locale for the current request """
    locale = request.args.get("locale", None)
    if locale is None:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return locale


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def root():
    """ Root route """
    locale = get_locale()
    return render_template("4-index.html", locale=locale)


if __name__ == "__main__":
    host = getenv("BASIC_HOST", "localhost")
    port = getenv("BASIC_PORT", "5000")
    app.run(host, port)
