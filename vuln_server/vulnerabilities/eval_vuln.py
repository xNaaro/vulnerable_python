import random

from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class EvalVuln():

    def bypass(self):
        if request.method == 'POST':
            # Check if data is not empty, post forms has all params defined
            # which may be empty and cause unexpected behaviour.
            if request.form['input_data'] != '':
                data = random.randint(1, 1000)
                try:
                    # Instanciate a different stdout grabber for subprocess
                    output = OutputGrabber()
                    with output:
                        # Eval input data and execute code from it
                        if data != eval(request.form['input_data']):
                            pass
                    return output.capturedtext
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            else:
                return redirect(request.url)
        return render_template('eval.html')
