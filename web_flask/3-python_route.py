#!/usr/bin/python3
"""flash app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """route hello controller"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """route hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c route"""
    return f"C {text.replace('_', ' ')}"

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_route(text="is cool"):
    """p route"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
