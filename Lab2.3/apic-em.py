from flask import Flask
from flask import jsonify
import requests
import json
import pprint

ticket = ""

app = Flask(__name__)

@app.route('/')
def ticket_info():
    return ticket

@app.route('/api/topology')
def get_topology():
    global ticket
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    response = requests.get(url, headers=header, verify=False)

    return response


if __name__ == '__main__':

    global ticket
    header = {"content-type": "application/json"}
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    url = "https://sandboxapic.cisco.com/api/v1/ticket"
    response = requests.post(url,data=json.dumps(payload),headers=header,verify=False)
    ticket = response.json()["response"]["serviceTicket"]

    app.run(debug=True)
