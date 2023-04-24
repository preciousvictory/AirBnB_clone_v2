#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filter():
    """ HBNB filters """
    states = storage.all(State).values()

    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", all_states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

