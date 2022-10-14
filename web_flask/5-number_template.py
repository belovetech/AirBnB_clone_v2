#!/usr/bin/python3
"""Script that runs a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function invoked with / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function invoked with /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Function invoked with /c/<text> route"""
    return 'C  %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Function invoked with /python/<text> route"""
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function invoked with /number/<n> route"""
    return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
