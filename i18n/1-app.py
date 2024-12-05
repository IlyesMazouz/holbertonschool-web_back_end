#!/usr/bin/env python3
"""
A simple Flask app that uses Flask-Babel for internationalization (i18n).
"""
from flask import Flask, render_template
from flask_babel import Babel

babel = Babel()


class Config:
    """
    Configuration class for the Flask app with languages and locale settings.
    """

    LANGUAGES = ["en", "fr"]
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel.init_app(app)


@app.route("/")
def hello_world() -> str:
    """
    Route to display the 'Hello World' message.

    Returns:
        str: Rendered HTML template with a greeting message.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
