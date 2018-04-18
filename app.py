#!/usr/bin/python3
""" list from db """

from flask import render_template
from flask import Flask
from models import storage, Url
from uuid import uuid4

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def home():
    return render_template('base.html')

# @app.route('/<url_id>', strict_slashes=False)
# def get_url():
#     return render_template()

@app.route('/generate_url', strict_slashes=False, methods=['POST'])
def generate_url():
    return render_template()


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
