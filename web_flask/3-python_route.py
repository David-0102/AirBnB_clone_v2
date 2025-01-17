#!/usr/bin/python3
"""
This module starts a Flask web application with four routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!' at the root URL.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display 'HBNB' at the /hbnb URL.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route to display 'C ' followed by the value of the text variable.
    Underscores in the text are replaced with spaces.
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route to display 'Python ' followed by the value of the text variable.
    Underscores in the text are replaced with spaces.
    The default value of text is 'is cool'.
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
