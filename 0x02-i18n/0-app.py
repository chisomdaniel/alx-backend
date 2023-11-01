#!/usr/bin/env python3
from flask import Flask, render_template
'''Basic flask app'''

app = Flask(__name__)


@app.route("/")
def hello_world():
    '''hello world'''
    return render_template('0-index.html')
