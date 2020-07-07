# whoami

Whoami based on python with flask.

* You can start whoami-py in the directory `/app` by: `python3 apy.py`.
* On your local machine you can start whoami-py (using docker) by `./start-whoami-py.sh`.
* Start whoami-py by `docker run -p 8002:8080 --name whoami-py --restart=always -d jennerwein/whoami-py:latest`
* Start with environment variable: `WHOAMICOLOR=red python app.py`
* Available values for `WHOAMICOLOR` are red, blue, green, yellow, purpel
* Start red whoami: `docker run -p 8002:8080 -e WHOAMICOLOR=red --name whoami-py --restart=always -d jennerwein/whoami-py:latest`
