#!/usr/bin/python3
"""flash app"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    """number route"""
    if type(n) == int:
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_route(n):
    """num route"""
    if type(n) == int:
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd_route(n):
    """even odd route"""
    if type(n) == int:
        if n % 2 != 0:
            text = f'{n} is odd'
        else:
            text = f'{n} is even'
        return render_template("6-number_odd_or_even.html", n=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
