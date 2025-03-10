#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """print Hello HBNB"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def write_HBNB():
    """print HBNB"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """print c text"""

    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def Python_text(text):
    """print python text"""

    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:number>", strict_slashes=False)
def number_route(number):
    """print number if number is an integer"""

    return "{} is a number".format(number)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_route(n):
    """display html page if n is an integer"""

    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """display html page if n is an integer, depend if n is odd or even"""

    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
