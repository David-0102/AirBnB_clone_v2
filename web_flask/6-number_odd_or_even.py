#!/usr/bin/python3
"""
This module starts a Flask web application with multiple routes.
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display 'n is a number' only if n is an integer.
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display a HTML page only if n is an integer:
    H1 tag: 'Number: n' inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to display a HTML page only if n is an integer:
    H1 tag: 'Number: n is even|odd' inside the tag BODY
    """
    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        even_or_odd=even_or_odd
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
