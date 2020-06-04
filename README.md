# pyhubitat
![Python application](https://github.com/danielorf/pyhubitat/workflows/Python%20application/badge.svg?branch=master)
[![image](https://img.shields.io/pypi/v/pyhubitat.png)](https://pypi.org/project/pyhubitat/)
[![image](https://img.shields.io/pypi/pyversions/pyhubitat.png)](https://pypi.org/project/pyhubitat/)
[![image](https://img.shields.io/pypi/l/pyhubitat.png)](https://pypi.org/project/pyhubitat/)

A python library for interacting with the Hubitat API

## Highlights
This package is new and rapidly developing.  It currently exposes only the Hubitat 'Maker API' which is limited to the functionality of the devices, not the hub.  The official Maker API docs can be found [here](https://docs.hubitat.com/index.php?title=Maker_API).
Endpoints exposed include:
- Get All Devices (/devices)
- Get All Devices with Full Details (/devices/all)
- Get Device Info (/devices/[device ID])
- Get Device Event History (/device/[device ID]/events)
- Get Device Commands (/device/[device ID]/commands)
- Get Device Capabilities (/device/[device ID]/capabilities)
- Send Device Command (/device/[device ID]/[Command]/[Secondary Value])

## Installation
`pip install pyhubitat`

## Usage
### Initialization
```
import os
import pprint

from pyhubitat import MakerAPI

HUB_TOKEN = os.environ['HUBITAT_TOKEN']
HUB_URL_EXAMPLE = 'https://192.168.1.39/apps/api/24'  # Follow the generic format of 'https://[hub-ip-address-or-hostname]/apps/api/[app-id]'

ph = MakerAPI(HUB_TOKEN, HUB_URL_EXAMPLE)
```

### Get Devices
```
devices = ph.list_devices()
pprint.pprint(devices)
```

### Send Command
```
response1 = ph.send_command(5, 'on')
response2 = ph.send_command(6, 'setLevel', 50)
```

### Hubitat update 2.0.9
With Hubitat update 2.0.9, Maker API supports Modes and HSM as endpoints.  pyhubitat has been updated to support calles to these endpoints.
...
#devices = ph.modes()
#devices = ph.modes_set(1)                   # example modes 1=Day, 2=Evening, 3=Night, 4=Away
#devices = ph.hsm_status()
#devices = ph.hsm_set('disarm')              # example hsm status codes disarm, armNight, armAway
...

## Note about TLS/SSL
The Hubitat hub uses a self-signed root certificate for https and I see no reasonable way to add your own.  Despite this, it is still recommended that you enable login auth on the hub and use the https API url since your API token is sent with every request.
