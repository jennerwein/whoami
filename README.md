# whoami

A server that gives information about the container environment such as:

![local address / local port / remote address / remote port / default gateway IPv4 / public IP / uptime / ... ](./images/whoami.jpg)

## Run whoami

`docker run -p 8080:8080 --name whoami -d jennerwein/whoami`

## Remarks

* Run a 'red' whoami container by: `docker run -p 8080:8080 -e WHOAMICOLOR=red --name whoami --restart=always -d jennerwein/whoami`
* Available values for `WHOAMICOLOR` are `red`, `blue`, `green`, `yellow`, `purpel`.
* Build and start a whoami container with the script: `./start-whoami.sh`
* Start the *app* whoami in the directory `/app` with: `python3 app.py`
* Run the *app* whoami with environment variables: `WHOAMICOLOR=red python app.py`
