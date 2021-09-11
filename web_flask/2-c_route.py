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

if __name__ == "__main__":
        app.run()
