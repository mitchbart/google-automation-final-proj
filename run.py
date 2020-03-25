#! /usr/bin/env python3

import os
import requests

#change for remote version maybe?
dir = os.path.abspath("supplier-data/descriptions")
#print(os.listdir(dir))
fruit_data = os.listdir(dir)

fruits = []

for file in fruit_data:
  f, e = os.path.splitext(file)
  with open(dir + "/" + file) as file:
    new_dict = {}
    new_dict["name"] = file.readline().strip()
    new_dict["weight"] = int(file.readline().strip().split()[0])
    new_dict["description"] = file.readline().strip()
    new_dict["image_name"] = f + ".jpeg"
    fruits.append(new_dict)

print(fruits)

#change for remote version
for fruit in fruits:
  requests.post("http://[linux-instance-external-IP]/fruits", data = fruit)
  print(response.status_code)
  #print(dict)