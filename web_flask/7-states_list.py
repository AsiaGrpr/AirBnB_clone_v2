#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """close"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = storage.all(State)

    if states:
        states_list = sorted(states.values(), key=lambda x: x.name)
    else:
        states_list = []
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
