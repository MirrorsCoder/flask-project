#encoding: utf-8

from flask4 import app


@app.route('/')
def index():
    return 'Hello'