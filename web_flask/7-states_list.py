#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Displays HTML page with states sorted from A to Z"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exc):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0')
