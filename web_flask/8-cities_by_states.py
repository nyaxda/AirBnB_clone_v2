#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.

    States/cities are sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    states_with_cities = {state: (sorted(storage.all(City).values(), key=lambda city: city.name) for state in states)}
    return render_template("8-cities_by_states.html", states=states_with_cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
