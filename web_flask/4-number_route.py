#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape
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
        return "C %s" % escape(string.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string>', strict_slashes=False)
def python_route(string="is cool"):
        """Handles optional variables"""
        return "Python %s" % escape(string.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
        """Handles converted variables"""
        if (n):
                return "%d is a number" % n

if __name__ == "__main__":
        app.run()
