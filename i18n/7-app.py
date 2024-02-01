#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from os import getenv
from pytz import timezone


class Config:
    """ Class that holds configuration values for babel """
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


def get_user(login_as: int) -> dict:
    """ Gets user from users """
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    if login_as not in users:
        return None
    return users[login_as]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """ Gets the locale for the current request """
    locale = request.args.get("locale", None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """ Get the timeznoe for the current request """
    user = get_user(request.args.get("login_as", None))
    arg_tz = request.args.get('timezone', None)
    if arg_tz is not None:
        locale = request.args.get('timezone')
    if user:
        locale = user['timezone']

    try:
        return timezone(locale).zone
    except Exception:
        return None


@app.before_request
def before_req():
    """ Checks for a user and and sets it as a global on flask.g.user """
    user_id = request.args.get("login_as", None)
    if user_id is None:
        g.user = None
        return
    g.user = get_user(int(user_id))


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def root():
    """ Root route """
    locale = get_locale()
    return render_template("5-index.html", locale=locale, user=g.user)


if __name__ == "__main__":
    host = getenv("BASIC_HOST", "localhost")
    port = getenv("BASIC_PORT", "5000")
    app.run(host, port)
