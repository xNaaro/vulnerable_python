import yaml
import pickle
import xml
import os
import base64
import logging
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from outputgrabber import OutputGrabber

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return 'Index Page'

@app.route('/pickle', methods=['GET', 'POST'])
def pickle_injection():
    if request.method == 'POST':
        if request.form['input_data'] != '':
            try:
                output = OutputGrabber()
                with output:
                    pickle.loads(base64.b64decode(request.form['input_data']))
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        elif request.files['file'].filename != '':
            file_data = request.files['file'].read()
            try:
                output = OutputGrabber()
                with output:
                    pickle.loads(base64.b64decode(file_data.decode()))
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            flash('No selected file')
            return redirect(request.url)
    return render_template('pickle.html')


@app.route('/yaml')
def yaml_injection():
    return 'Hello, World'

@app.route('/xml')
def xml_injection():
    return 'Hello, World'

@app.route('/input')
def input_injection():
    return 'Hello, World'