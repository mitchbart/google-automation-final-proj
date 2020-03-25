#!/usr/bin/env python3

import os
from PIL import Image

dir = "supplier-data/images"

#dir for remote version
#dir = "supplier-data/images"

for file in os.listdir(dir):
  f, e = os.path.splitext(file)
  outfile = f + ".jpeg"
  try:
    Image.open(dir + "/" + file).convert("RGB").resize((600, 400)).save(dir + "/" + outfile)
  except IOError:
    #print(IOError)
    print("cannot convert", file)
