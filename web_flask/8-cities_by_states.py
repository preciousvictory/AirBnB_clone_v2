#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_states():
    """ /states_list route """
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_state=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
