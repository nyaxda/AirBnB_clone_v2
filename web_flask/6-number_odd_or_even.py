#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display C """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Display Python """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display html"""
    return render_template('5-number.html', n=n)


@app.route('airbnb_dynamic/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display html"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0')
