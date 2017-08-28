import json
import requests
import pprint


r = requests.get('https://lookup.binlist.net/52788300',headers = {'Accept-Version':'3'})
pprint.pprint(r.json())



