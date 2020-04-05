FROM python:3-slim

WORKDIR /vuln_server
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt
ENV FLASK_APP server.py
ENV FLASK_ENV development
RUN date | sha256sum | base64 > /root/flag
ADD vuln_server/ /vuln_server

CMD flask run --host=0.0.0.0
