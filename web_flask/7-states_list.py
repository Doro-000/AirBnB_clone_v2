#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
import models

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def route_states():
        pep_fix = models.dummy_classes["State"]
        data = models.storage.all(cls=pep_fix)
        states = data.values()
        return render_template('7-states_list.html', states_list=states)


@app.teardown_appcontext
def refresh(exception):
        models.storage.close()

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
