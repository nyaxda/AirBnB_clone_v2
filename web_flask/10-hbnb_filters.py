from models import storage, State, City, Amenity
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays an HTML page with a list of all states, cities, and amenities.

    States, cities, and amenities are sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template("10-hbnb_filters.html",
                           states=states, cities=cities, amenities=amenities)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """Displays an HTML page with a list of all states or a specific state."""
    states = storage.all(State)
    if id is None:
        return render_template("9-states.html", states=states, state=None)
    else:
        state = None
        for state_obj in states.values():
            if state_obj.id == id:
                state = state_obj
                break
        return render_template("9-states.html", states=None, state=state)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    """Main method."""
    app.run(host="0.0.0.0")
