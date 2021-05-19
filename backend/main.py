#!/usr/bin/env python3

'''
Main backend application
To run: python3 main.py
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'OK'


@app.route('/login')
def login():
    return 'TODO'


if __name__ == '__main__':
    app.run(debug=True)
