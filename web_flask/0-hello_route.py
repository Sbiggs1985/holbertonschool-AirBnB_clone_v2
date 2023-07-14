#!/usr/bin/python3

from flask import Flask
# Imports Flask

app = Flask(__name__)
# Creates Flask application instance
# __name__ argument represents the name of the current module

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
# @app.route is the decorator provided by Flask

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# Starts the Flask development server
