#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False

    # Initialize Babel
    babel = Babel(app)

    @babel.localeselector
    def get_locale() -> str:
        """Retrieves the locale for a web page."""
        queries = request.query_string.decode('utf-8').split('&')
        query_table = dict(map(
            lambda x: (x if '=' in x else '{}='.format(x)).split('='),
            queries,
        ))
        if 'locale' in query_table and query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
        return request.accept_languages.best_match(app.config["LANGUAGES"])

    @app.route('/')
    def get_index() -> str:
        """The home/index page."""
        return render_template('4-index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

