#!/usr/bin/env python3.4
from flask import Flask
import requests


app = Flask(__name__)


@app.route('/count/<key>')
def count(key):
    return requests.get('http://127.0.0.1:8080/count/{}'.format(key)).text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
