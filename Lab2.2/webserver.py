from flask import Flask
from flask import jsonify
import sys
import glob
import re

app = Flask(__name__)

@app.route('/')
def info():
    return "This is flask web server"

@app.route('/python')
def python_info():
    return jsonify(str(sys.__dict__))

@app.route('/configs')
def hosts_configs():
    return jsonify(str(hosts.keys()))

#@app.route('/config/hostname')

def clasificator(line):
    result = 0
    hostname_match = re.match('hostname (.+)', line)
    if (bool(hostname_match)):
        hostname = hostname_match.group(1)
        return ("HOST", hostname)
    return ("UNCLASSIFIED",)

if __name__ == '__main__':

    hosts = {}


    files = glob.glob("C:\\Users\\rusmanov.SUPPORT\\Seafile\\p4ne_training\\config_files\\*.txt")
    for j in files:
        with open(j) as f:
            for i in f:
                a = clasificator(i)
                if a[0] != "UNCLASSIFIED":
                    hosts[a[1]] = a[1]

    app.run(debug = True)


