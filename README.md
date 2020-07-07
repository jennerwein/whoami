# whoami

A server that gives information about the container environment such as:

![Local Address / Local Port / Remote Address / Remote Port / Default Gateway IPv4 / Public IP / Uptime / ... ](./images/whoami.jpg)

* You can start the app whoami in the directory `/app` by: `python3 apy.py`.
* You can build and start a whoami docker container by `./start-whoami-py.sh`.
* Run whoami by `docker run -p 8002:8080 --name whoami-py --restart=always -d jennerwein/whoami-py:latest`
* Run whoami with environment variable: `WHOAMICOLOR=red python app.py`
* Available values for `WHOAMICOLOR` are red, blue, green, yellow, purpel
* Run red whoami by: `docker run -p 8002:8080 -e WHOAMICOLOR=red --name whoami-py --restart=always -d jennerwein/whoami-py:latest`
