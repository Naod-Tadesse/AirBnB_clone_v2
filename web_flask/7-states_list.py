#!/usr/bin/python3
"""web application for airbnb"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def liststates():
    """list states"""
    result = list(storage.all("State").values())
    result.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=result)


@app.teardown_appcontext
def tdb(exception):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
