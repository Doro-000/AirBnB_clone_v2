#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
import models

app = Flask(__name__)


@app.teardown_appcontext
def refresh(exception):
    """reload storage when refreshed"""
    models.storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state_route(id=None):
    """route for states"""
    pep_fix = models.dummy_classes["State"]
    data = models.storage.all(cls=pep_fix)
    states = None
    if (id is not None):
        for key in data:
            k = key.split(".")[1]
            if (k == id):
                states = data["State.{}".format(k)]
    else:
        states = list(data.values())
    return render_template('9-states.html', states_list=states)


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
