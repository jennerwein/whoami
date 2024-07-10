import time
import socket
import psutil
import urllib.request

from flask import Flask, render_template, request, jsonify  # pip3 install flask
from requests import get
import netifaces    # https://github.com/al45tair/netifaces
import platform     # https://docs.python.org/3/library/platform.html
import os           # https://docs.python.org/3/library/os.html
import hashlib

import helper

global numberOfCalls, startupTime
numberOfCalls = 1
startupTime = time.time()

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def valueCalculation(requestEnvironment):

    global numberOfCalls
    numberOfCalls = numberOfCalls+1
    # Check environment variable WHOAMICOLOR
    WHOAMICOLOR = os.getenv('WHOAMICOLOR')
    print(WHOAMICOLOR)
    if WHOAMICOLOR == None:
        # Define arbitrary background color depending on host name given by docker
        global bgColor
        HexValue = hashlib.sha1(socket.gethostname().encode("utf-8")).hexdigest()[0:6]
        try: 
            if int(HexValue, 16) >= 0:
                bgColor = "#" + HexValue
        except:
            bgColor = "#28a745" # Default background color
    else:
        # evaluate WHOAMICOLOR
        if WHOAMICOLOR == "red":
            bgColor = "#ff3030"
        elif WHOAMICOLOR == "green":
            bgColor = "#76ee00"
        elif WHOAMICOLOR == "blue":
            bgColor = "#4876ff"
        elif WHOAMICOLOR == "yellow":
            bgColor = "#eeee00"
        elif WHOAMICOLOR == "purpel":
            bgColor = "#9b30ff"
        else:
            bgColor = "#28a745" # Default background color

    # Determine text color depending on the background brightness
    # print("Brightness ==> ", helper.rgb_brightness(bgColor))
    if helper.rgb_brightness(bgColor) < 150:
        txtColor = "#ffffff"
    else:
        txtColor = "#000000"

    # Public IP by: https://www.ipify.org/
    try:
        publicIP4 = get('https://api.ipify.org').text
    except:
        publicIP4 = "no IPv4"
    # comment this out when IPv6 problems inside docker environment
    try:
        publicIP6 = get('https://api6.ipify.org').text
    except:
        publicIP6 = "no IPv6"
    if publicIP4 == publicIP6:
        publicIP6 = "no IPv6"

    # Collect all values
    Werte={ 
        "numberOfCalls": numberOfCalls,
        "bgColor": bgColor,
        "txtColor": txtColor,
        "hostname" : socket.gethostname(),
        #"localAddress" : requestEnvironment['SERVER_NAME'],
        "localAddress" : get_ip(),
        "localPort" : requestEnvironment['SERVER_PORT'],
        "remoteAddress" : requestEnvironment['REMOTE_ADDR'],
        "remotePort" : requestEnvironment['REMOTE_PORT'],
        # Modul netifaces: https://github.com/al45tair/netifaces
        "defaultGateway": netifaces.gateways()['default'][netifaces.AF_INET][0],
        "publicIP4": publicIP4,
        # "publicIP6": publicIP6,
        "uptime" : helper.duration(int(time.time()-startupTime)),
        # Modul psutil: https://psutil.readthedocs.io/en/latest/
        "osPlatform" : platform.system(),
        "osKernel" : platform.release(),
        "osVersion" : platform.version(),
        "processor" : platform.processor(),
        "osNumberOfCores" : os.cpu_count(), # https://docs.python.org/3/library/os.html
        # Modul platform: https://docs.python.org/3/library/platform.html#module-platform
        "sysMemTotal": helper.humanbytes(psutil.virtual_memory().total),
        "sysMemFree": helper.humanbytes(psutil.virtual_memory().free),
        "curPID": os.getpid(),
        "pythonVersion" : platform.python_version(),
        } 
    return Werte

app = Flask(__name__, template_folder="templates")
@app.route('/')
def home():
    """Landing page."""
    ### Testing: Print request environment as dictionary
    # for key in request.environ:
    #     print(key, ':', request.environ[key])
    #
    Werte=valueCalculation(request.environ)
    return render_template('/index.html', Werte=Werte)

if __name__ == '__main__':
    #
    debug = False
    if debug:
      app.run(host='0.0.0.0', port=8080, debug=True)  # With debug mode
    else:
      app.run(host='0.0.0.0', port=80)