#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask

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
    """ Display HBNB """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', defaults={"text": "is cool"},
           strict_slashes=False)
def python(text):
    """ Display HBNB """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0')
