# Vulnerable Python server
## Description

This project aims to be educational about Python deseralization and common vulnerabilities.
Will provide different rest URL paths for each of the security issues.

Try to gather contents from /root/flag exploiting the input forms.

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

## Example exploits

Sample code exploits are located at exploits/ directory.
Read carefully the code to make sure you understand what it does and change what is needed.

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

## TODO

- Add more vulnerabilites
- Add documentation
- Add example code fixes
