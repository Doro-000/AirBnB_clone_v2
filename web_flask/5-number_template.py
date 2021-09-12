#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
        """hello world func"""
        return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """hbnb func"""
        return "HBNB"


@app.route('/c/<string>', strict_slashes=False)
def c_route(string):
        """Handles variables"""
        return "C {}".format(string.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string>', strict_slashes=False)
def python_route(string="is cool"):
        """Handles optional variables"""
        return "Python {}".format(string.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
        """Handles converted variables"""
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_num_route(n):
        """serves static files with variables"""
        return render_template("5-number.html", name=n)


if __name__ == "__main__":
        app.run()
