import sys
import requests

ARGS = sys.argv

req = requests.get(ARGS[1])

while req.status_code != int(ARGS[2]):
    print('Error. Requesting...')
    req = requests.get(ARGS[1])

print('Ok')
