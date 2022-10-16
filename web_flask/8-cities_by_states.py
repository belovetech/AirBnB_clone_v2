#!/usr/bin/python3
"""Script that runs a Flask web application"""

import os
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    """List all states"""
    states = storage.all("State")
    return render_template('8-cities_by_states.html',
                           Table="States", states=states)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
