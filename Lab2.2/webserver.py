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

@app.route('/config/hostname')
def hosts_ipaddress():
    return jsonify(str(ips.keys()))



def clasificator(line):
    result = 0
    hostname_match = re.match('hostname (.+)', line)
    if (bool(hostname_match)):
        hostname = hostname_match.group(1)
        return ("HOST", hostname)

    ip_net_match = re.match(
        ' ip address ([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\ ([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})\.?([0-9]{1,3})',
        line)
    if (bool(ip_net_match)):
        ip_mask = ip_net_match.group(1, 2, 3, 4, 5, 6, 7, 8)
        ip = ip_mask[0] + '.' + ip_mask[1] + '.' + ip_mask[2] + '.' + ip_mask[3]
        return ("IP", ip)

    return ("UNCLASSIFIED",)

if __name__ == '__main__':
    hosts = {}
    ips = {}
    files = glob.glob("C:\\Users\\rusmanov.SUPPORT\\Seafile\\p4ne_training\\config_files\\*.txt")
    for j in files:
        with open(j) as f:
            for i in f:
                a = clasificator(i)
                if a[0] != "UNCLASSIFIED":
                    if a[0] == "HOST":
                        hosts[a[1]] = a[1]
                    if a[0] == "IP":
                        ips[a[1]] = a[1]
    app.run(debug = True)


