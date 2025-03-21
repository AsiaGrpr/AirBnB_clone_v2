#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """close"""

    if isinstance(storage, DBStorage):
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a list of state"""

    states_list = []
    states = storage.all(State).values()
    for state in states:
        states_list.append(state.to_dict())
    print(states_list)
    states_list = sorted(states_list, key=lambda d: d['name'])
    return render_template("7-states_list.html", state_item=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
