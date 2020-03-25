#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

dir = "supplier-data/images"

for file in os.listdir(dir):
  if ".jpeg" in file:
    with open(dir + "/" + file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
