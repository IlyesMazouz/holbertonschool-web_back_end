#!/usr/bin/env python3
"""
Flask app with user login simulation, i18n, and timezone support.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError

app = Flask(__name__)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    App configuration class.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    Priority Order:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    Retrieve a user dictionary based on the `login_as` parameter.
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before every request to set the current user.
    """
    g.user = get_user()


def get_timezone():
    """
    Determine the best match for supported timezones.
    Priority Order:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default timezone (UTC)
    """
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get("timezone"):
        try:
            pytz.timezone(g.user["timezone"])  # Validate timezone
            return g.user["timezone"]
        except UnknownTimeZoneError:
            pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(app, timezone_selector=get_timezone)


@app.route("/", methods=["GET"])
def index():
    """
    Render the index page.
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
