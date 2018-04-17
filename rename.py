import cv2
import os
import sys

usage = "Usage:\nrename DIRNAME STATE\nDIRNAME = name of the directory\nSTATE = 'liquid', 'empty' or 'unknown'"

if len(sys.argv) != 3:
	print (usage)
	sys.exit()

DIRNAME = str(sys.argv[1])
STATE = str(sys.argv[2])

if STATE.lower() == "liquid":
	suffix = "n01111111"
elif STATE.lower() == "empty":
	suffix = "n01122222"
elif STATE.lower() == "unknown":
	suffix = "n01133333"
else:
	print (usage)
	sys.exit()

count = 0
for filename in os.listdir(DIRNAME):
	if filename.find('JPEG'):
		count_str = str(count)
		newfilename = suffix+"_"+count_str.zfill(4)+".JPEG"
		os.rename(DIRNAME+"/"+filename, DIRNAME+"/"+newfilename)
		print (filename+" renamed to "+newfilename)
		count = count + 1
