#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
        """hello world func"""
        return "Hello HBNB!"
