import numpy as np
import scipy.io as sio
import os, sys, cv2
import argparse
import math

usage = "Program which adds images' filenames to a txt file\n"+
        "Usage:\n   annotate2move\n"+
        "You must have a file named filenames.txt containing a list of the images you want to annotate"

if len(sys.argv) != 1:
	print (usage)
	sys.exit()

lines = []
with open("filenames.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

i = 0
newList = []
filename = "newlist.txt"
thefile = open(filename, 'w')

print "Simple program to annotate filenames on images \n\n"
print "ESC   =   quit"
print "->    =   next image"
print "<-    =   previous image"
print " M    =   annotate filename"
print " R    =   remove from list"
print " P    =   print list"
print " S    =   save list"
print "----------------------------------------------\n\n"

while True:
    imgname = lines[i]
    print imgname
    try:
        im = cv2.imread(imgname)
        cv2.imshow('image',im)
        k = cv2.waitKey(0)
    except:
        print "!!                           Error!!"
        if len(newList) > 0:
            print "                         Saving list..."
            for item in newList:
                thefile.write("%s\n" % item)
            print "                             List saved as "+filename
        break

    if k==1048603:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    elif k==1048685:  # M to move to another list
        if not imgname in newList:
            print "                             Moving "+imgname+" to newList"
            newList.append(imgname)
        else:
            print "                             File already in newList"
        continue
    elif k==1048690:  # R to remove from newList
        try:
            newList.remove(imgname)
            print "                             Removing "+imgname+" from newList"
        except:
            print "                             newList doesnt contain the file"
        continue
    elif k==1048688:  # P to print list
        print "\n\nPrinting newList:\n"
        for x in newList:
            print x
        print "---------------------\n\n"
        continue
    elif k==1048691:  # S to save
        print "                             Saving list..."
        for item in newList:
            thefile.write("%s\n" % item)
        print "                             List saved as "+filename
        continue
    elif k==1113939:  # -> to skip to the next image
        if i+1 <= len(lines)-1:
            i += 1
            imgname = lines[i]
        continue
    elif k==1113937:  # <- to skip to the previous image
        if i-1 >= 0:
            i -= 1
            imgname = lines[i]
        continue
    else:
        print k # else print its value
        continue

cv2.destroyAllWindows()
