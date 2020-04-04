import base64
import pickle
import random
import subprocess
import yaml

from flask import Flask, flash, request, redirect, render_template
from outputgrabber import OutputGrabber
from xml.dom.pulldom import parseString
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pickle', methods=['GET', 'POST'])
def pickle_injection():
    """Pickle object command injection/execution.

    This funtion will evaluate if the user includes a file or
    a pickle base64 object and load the object.
    """
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined which
        # may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            try:
                # Instanciate a different stdout grabber for subprocess out.
                output = OutputGrabber()
                with output:
                    # Load base64 encoded pickle object, output from the
                    # exploit is stored into Outputgrabber stdout.
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


@app.route('/yaml', methods=['GET', 'POST'])
def yaml_injection():
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined which
        # may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            try:
                # Instanciate a different stdout grabber for subprocess out.
                output = OutputGrabber()
                with output:
                    # Load unsafe YAML input, output from the exploit
                    # is stored into Outputgrabber stdout.
                    yaml.load(request.form['input_data'],
                              Loader=yaml.UnsafeLoader)
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('yaml.html')


@app.route('/xml', methods=['GET', 'POST'])
def xml_injection():
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined which
        # may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            # Instanciate an XML parser allowing unsafe external sources to
            # to be parsed by xml.parseString.
            parser = make_parser()
            parser.setFeature(feature_external_ges, True)
            doc = parseString(request.form['input_data'], parser=parser)
            for event, node in doc:
                doc.expandNode(node)
                return(node.toxml())
        else:
            return redirect(request.url)
    return render_template('xml.html')


@app.route('/eval', methods=['GET', 'POST'])
def eval_bypass():
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined which
        # may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            data = random.randint(1, 1000)
            try:
                # Instanciate a different stdout grabber for subprocess out.
                output = OutputGrabber()
                with output:
                    # Eval input data and execute code from it.
                    if data != eval(request.form['input_data']):
                        pass
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('eval.html')


@app.route('/subprocess', methods=['GET', 'POST'])
def exec_bypass():
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined which
        # may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            try:
                # Instanciate a different stdout grabber for subprocess out.
                output = OutputGrabber()
                with output:
                    # Execute system command with an unsafe input parameter.
                    subprocess.call("ping -c1 " + request.form['input_data'],
                                    shell=True)
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('subprocess.html')
