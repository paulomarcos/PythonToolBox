import cv2
import os
import sys
import numpy as np
import numbers

usage = "Resize a bunch of images\n  Usage:\n   resize DIRECTORYNAME HEIGHT WIDTH\n"

if len(sys.argv) != 4:
	print (usage)
	sys.exit()

DIRNAME = str(sys.argv[1])
HEIGHT = sys.argv[2]
WIDTH = sys.argv[3]

if not (isistance(HEIGHT, int) and isistance(WIDTH, int)):
	print ("HEIGHT or WIDTH not integers")
	print (usage)
	sys.exit()

for root, dirs, files in os.walk(DIRNAME):
    for file in files:
        filename = (os.path.join(root, file))
        img = cv2.imread(filename)
        img = cv2.resize(img, (HEIGHT, WIDTH))
        cv2.imwrite(filename, img)
print ("Done")
