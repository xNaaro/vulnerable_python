from flask import Flask, render_template

from vuln_server.vulnerabilities.pickle_vuln import PickleVuln
from vuln_server.vulnerabilities.yaml_vuln import YAMLVuln
from vuln_server.vulnerabilities.xml_vuln import XMLVuln
from vuln_server.vulnerabilities.eval_vuln import EvalVuln
from vuln_server.vulnerabilities.subprocess_vuln import SubprocessVuln


app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pickle', methods=['GET', 'POST'])
def pickle_injection():
    vuln = PickleVuln()
    return vuln.injection()


@app.route('/yaml', methods=['GET', 'POST'])
def yaml_injection():
    vuln = YAMLVuln()
    return vuln.injection()


@app.route('/xml', methods=['GET', 'POST'])
def xml_injection():
    vuln = XMLVuln()
    return vuln.injection()


@app.route('/eval', methods=['GET', 'POST'])
def eval_bypass():
    vuln = EvalVuln()
    return vuln.bypass()


@app.route('/subprocess', methods=['GET', 'POST'])
def subprocess_bypass():
    vuln = SubprocessVuln()
    return vuln.bypass()
