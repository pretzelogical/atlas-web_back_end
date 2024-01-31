#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template
from os import getenv


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Root route """
    return render_template("0-index.html")


if __name__ == "__main__":
    host = getenv("BASIC_HOST", "localhost")
    port = getenv("BASIC_PORT", "5000")
    app.run(host, port)
