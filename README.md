# whoami

A server that gives information about the container environment such as:

![local address / local port / remote address / remote port / default gateway IPv4 / public IP / uptime / ... ](./images/whoami.jpg)

## Run it by

`docker run -p 8080:8080 --name whoami -d jennerwein/whoami`

## Remarks

* Start whoami in the directory `/app` with: `python3 apy.py`
* Build and start a whoami container with the script: `./start-whoami-py.sh`
* Run whoami by: `docker run -p 8002:8080 --name whoami --restart=always -d jennerwein/whoami`
* Run whoami with environment variable: `WHOAMICOLOR=red python app.py`
* Available values for `WHOAMICOLOR` are `red`, `blue`, `green`, `yellow`, `purpel`
* Run a 'red' whoami container by: `docker run -p 8080:8080 -e WHOAMICOLOR=red --name whoami --restart=always -d jennerwein/whoami`
