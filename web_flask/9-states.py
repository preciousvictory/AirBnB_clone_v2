#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Displays an HTML page with a list of all States."""
    all_states = storage.all(State).values()
    f = 0
    return render_template("9-states.html", all_state=all_states, f=0)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", all_state=state, f=1)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
