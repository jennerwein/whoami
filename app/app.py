import time
import socket
import urllib.request

from flask import Flask, render_template, request, jsonify  # pip3 install flask
from requests import get
import netifaces    # https://github.com/al45tair/netifaces
import platform
import os           # https://docs.python.org/3/library/os.html

from zeit import zeitdauer

global anzahlAufrufe, startZeit
anzahlAufrufe = 1
startZeit = time.time()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def werteBerechnung(requestUmgebung):
    global anzahlAufrufe
    anzahlAufrufe = anzahlAufrufe+1

    try:
        with open('/proc/meminfo') as file:
            for line in file:
                if 'MemTotal' in line:
                    MemTotal_in_kb = line.split()[1]
                if 'MemFree' in line:
                    MemFree_in_kb = line.split()[1]
                    break
    except:
        MemTotal_in_kb = "no Value"
        MemFree_in_kb = "no Value"

    Werte={ 
        "hostname" : socket.gethostname(),
        #"localAddress" : requestUmgebung['SERVER_NAME'],
        "localAddress" : get_ip(),
        "localPort" : requestUmgebung['SERVER_PORT'],
        "remoteAddress" : requestUmgebung['REMOTE_ADDR'],
        "remotePort" : requestUmgebung['REMOTE_PORT'],
        # Modul netifaces: https://github.com/al45tair/netifaces
        "defaultGateway": netifaces.gateways()['default'][netifaces.AF_INET][0],
        # Public IP mit der API: https://api.ident.me/
        "publicIP4": get('https://api.ipify.org').text,
        "publicIP6": get('https://api6.ipify.org').text,
        "uptime" : zeitdauer(int(time.time()-startZeit)),
        # Modul psutil: https://psutil.readthedocs.io/en/latest/

        # Modul platform: https://docs.python.org/3/library/platform.html#module-platform
        "osPlatform" : platform.system(),
        "osKernel" : platform.release(),
        "osVersion" : platform.version(),
        "processor" : platform.processor(),
        "osNumberOfCores" : os.cpu_count(), # https://docs.python.org/3/library/os.html
        "sysMemTotal": MemTotal_in_kb,
        "sysMemFree": MemFree_in_kb,
        "curPID": os.getpid(),
        "pythonVersion" : platform.python_version(),
        } 
    return Werte

app = Flask(__name__, template_folder="templates")
@app.route('/')
def home():
    """Landing page."""
    #
    print("#########################################################################")
    print('Methode2: ', request.environ)
    #####
    # Zeilenweise Ausgabe der requestUmgebung als dictionary
    # for key in request.environ:
    #     print(key, ':', request.environ[key])
    #
    Werte=werteBerechnung(request.environ)
    return render_template('/index.html', Werte=Werte)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)