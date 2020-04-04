# Vulnerable Python server
## Description

This project aims to be educational about Python desaralization and common vulnerabilities.
Will provide an different rest URL path for each of the security issues.

## Vulnerabilities done

* Pickle
* YAML injection
* XML Xternal Entity injection
* eval RCE
* subprocess.call RCE

## Vulnerabilities missing TBD

* exec RCE
* Assert bypass
* Common input checks bypass


## Usage
### From Docker
Create docker container and browse http://localhost:5000
```
docker run --name vuln_python_server --rm -ti -p 5000:5000 egonzalez90/vuln_python_server:latest
```
### From flask
Run local flask server at http://localhost:5000

```
export FLASK_APP=server.py ; export FLASK_ENV=development ; flask run
```

## TODO

- Add more vulnerabilites
- Add documentation
- Flask docker image
