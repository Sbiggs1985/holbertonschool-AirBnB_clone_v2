#!/usr/bin/python3

Imports Flask
from flask import Flask

# Creates an instance of Flask
app = Flask(__name__)

# decorator that specifies the URL route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# decorator deines route
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Condition statement - Starts Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
