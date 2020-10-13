#!/usr/bin/python3

#- look for status
#- if status then 
#else:
#    pass


import config
import OctoRest

# login(config.octourl, config.octoapi) ## dunno why this is here



def make_client(url, apikey):
     """Creates and returns an instance of the OctoRest client.

     Args:
         url - the url to the OctoPrint server
         apikey - the apikey from the OctoPrint server found in settings
     """
     try:
         client = OctoRest(url=config.octourl, apikey=config.octoapi)
         return client
     except ConnectionError as ex:
         # Handle exception as you wish
         print(ex)

print("Homing your 3d printer...")
client.status()