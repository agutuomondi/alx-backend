#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False

    # Initialize Babel
    babel = Babel(app)

    @app.route('/')
    def get_index() -> str:
        """The home/index page."""
        return render_template('1-index.html')

    return app


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

