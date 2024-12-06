#!/usr/bin/env python3
"""
A Flask app with Flask-Babel for internationalization (i18n).
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

babel = Babel()


class Config:
    """App configuration class."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """
    Determine the best match with the supported languages.

    Returns:
        str: The best matching language ('en' or 'fr').
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)

babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Render the index page with translations.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
