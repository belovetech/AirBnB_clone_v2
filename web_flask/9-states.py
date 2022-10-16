#!/usr/bin/python3
"""Script that runs a Flask web application"""

import os
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """List all states"""
    states = storage.all("State")
    return render_template('7-states_list.html',
                           Table="States", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_city(id=None):
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html',
                                   Table=state.name,  state=state)
    return render_template('9-states.html', Table=state.name,  state=None)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
