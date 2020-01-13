import httpx
import os
import time

class MakerAPI:

    def __init__(self, token, api_base_url, ssl_verify=False):
        """
        Token and API URL are generated by Hubitat when making Maker API
        API URL takes the form of 'https://[hub-ip-address-or-hostname]/apps/api/[app-id]'
        """
        self.token = token
        self.api_base_url = api_base_url
        self.ssl_verify = ssl_verify
        
    def _request_sender(self, url_suffix):
        """
        Helper function to send commands to Hubitat Maker API
        """
        params = {'access_token': self.token}
        url = '{}/{}'.format(self.api_base_url, url_suffix)
        return httpx.get(url, params=params, verify=self.ssl_verify)
        
    def list_devices(self):
        """
        Lists available devices
        """
        r = self._request_sender('devices')
        return r.json()

    def list_devices_detailed(self):
        """
        Lists available devices with detailed information
        """       
        r = self._request_sender('devices/all')
        return r.json()

    def get_device_info(self, device_id):
        """
        Get detailed information for a specific device
        """
        r = self._request_sender('devices/{}'.format(device_id))
        return r.json()

    def get_device_events(self, device_id):
        """
        Get the last 20 events for a device
        """
        r = self._request_sender('devices/{}/events'.format(device_id))
        return r.json()

    def get_device_commands(self, device_id):
        """
        Get a list of available commands
        """
        r = self._request_sender('devices/{}/commands'.format(device_id))
        return r.json()
    
    def get_device_capabilities(self, device_id):
        """
        Returns a list of device properties
        """
        r = self._request_sender('devices/{}/capabilities'.format(device_id))
        return r.json()

    def send_command(self, device_id, *commands):
        """
        *commands allows for singular commands as well as primary/seconday commands.
        Simply supply the requisite number of commands as args in order.
        """
        if len(commands) > 2:
            raise Exception("Number of commands cannont exceed 2, you entered {}".format(len(commands)))
        command = "/".join(map(str, commands))
        r = self._request_sender('devices/{}/{}'.format(device_id, command))
        return r.json()

    def device_status(self, device_id):
        """
        Gets the value of all configurable options and returns as dict
        """
        status = {}
        r = self.get_device_info(device_id)
        attributes = r.get('attributes')

        for attribute in attributes:
            name = attribute.get('name')
            if name not in status:
                status[name] = {'currentValue': attribute.get('currentValue'), 'dataType': attribute.get('dataType')}

        return status
