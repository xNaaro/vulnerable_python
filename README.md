# Vulnerable Python server
## Decription

This project aims to be educational about Python desaralization and common vulnerabilities.
Will provide an different rest URL path for each of the security issues.

## Vulnerabilities done

* Pickle

## Vulnerabilities missing TBD

* YAML injection
* XML injection
* input RCE
* eval RCE
* Assert bypass
* Common input checks bypass


## Usage

```
export FLASK_APP=vuln_server.py ; export FLASK_ENV=development ; flask run
```

## TODO

- Add more vulnerabilites
- Add documentation
- Flask docker image