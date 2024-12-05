#!/usr/bin/env python3
"""
A simple Flask app that displays a "Hello World" message.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """
    Route to display the 'Hello World' message.

    Returns:
        str: Rendered HTML template with a greeting message.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
