#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
import models

app = Flask("__name__")


@app.teardown_appcontext
def refresh():
        storage.close()


@app.route("/states_list", strict_slashes=False)
def route_states():
        pep_fix = models.dummy_classes["State"]
        data = models.storage.all(cls=pep_fix)
        states = data.values()
        refresh()
        return render_template("7-states-list.html", states=states)


if __name__ == "__main__":
        app.run()
