import yaml
import pickle
import base64
import random
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


@app.route('/yaml', methods=['GET', 'POST'])
def yaml_injection():
    if request.method == 'POST':
        if request.form['input_data'] != '':
            try:
                output = OutputGrabber()
                with output:
                    yaml.load(request.form['input_data'], Loader=yaml.UnsafeLoader)
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('yaml.html')


@app.route('/xml', methods=['GET', 'POST'])
def xml_injection():
    if request.method == 'POST':
        if request.form['input_data'] != '':
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
        if request.form['input_data'] != '':
            data = random.randint(1,1000)
            try:
                output = OutputGrabber()
                with output:
                    if data != eval(request.form['input_data']):
                        pass
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('eval.html')

@app.route('/exec')
def exec_bypass():
    return render_template('exec.html')
