#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"HBNB"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display 'C ', followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'ís cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """display 'Python ', followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
