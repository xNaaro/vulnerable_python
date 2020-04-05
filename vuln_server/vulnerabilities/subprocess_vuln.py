import subprocess

from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class SubprocessVuln():

    def bypass(self):
        if request.method == 'POST':
            # Check if data is not empty, post forms has all params defined
            # which may be empty and cause unexpected behaviour.
            if request.form['input_data'] != '':
                try:
                    # Instanciate a different stdout grabber for subprocess
                    output = OutputGrabber()
                    with output:
                        # Execute system command with an unsafe input parameter
                        subprocess.call("ping -c1 " +
                                        request.form['input_data'], shell=True)
                    return output.capturedtext
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            else:
                return redirect(request.url)
        return render_template('subprocess.html')
