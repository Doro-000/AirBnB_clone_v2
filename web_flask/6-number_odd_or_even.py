#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_route(n):
        """serves static files"""
        if (n):
                return render_template("5-number.html", my_num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_route(n):
        """serves static files, handles odd and even"""
        if (n):
                return render_template("6-number_odd_or_even.html", my_num=n)

if __name__ == "__main__":
        app.run()
