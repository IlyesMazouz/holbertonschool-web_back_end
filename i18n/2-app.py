#!/usr/bin/env python3
"""
A simple Flask app that uses Flask-Babel for internationalization (i18n).
"""
from flask import Flask, render_template, request
from flask_babel import Babel

babel = Babel()


class Config:
    """
    Configuration class for the Flask app with languages and locale settings.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """
    Select the best match language for the
    user based on the 'Accept-Language' header.

    Returns:
        str: The language to use ('en' or 'fr').
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)

babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello_world() -> str:
    """
    Route to display the 'Hello World' message.

    Returns:
        str: Rendered HTML template with a greeting message
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
