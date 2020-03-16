#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

CERTIFICATES_UPLOAD_FOLDER = '/certificates_uploads'

app.config['UPLOAD_FOLDER'] = CERTIFICATES_UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def hello_world():
    return 'Hello there!'
