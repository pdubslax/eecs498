#Patrick Wilson 
#EECS 498 HW 1


#!/usr/bin/env python
import re
import sys
import os
import operator

def stripSGML(input):
    pattern = re.sub("<[^<]+?>","",input)
    return pattern

def spacePeriod(input):
    pattern = re.sub("\. "," . ",input)
    return pattern

def spaceCommaApos(input):
    pattern = re.sub("\,"," , ",input)
    pattern = re.sub("\'"," ' ",pattern)
    return pattern

def removePunc(input):
    pattern = re.sub("\.","",input)
    pattern = re.sub("\,","",pattern)
    pattern = re.sub("\'","",pattern)
    pattern = re.sub("\+","",pattern)
    pattern = re.sub("\?","",pattern)
    pattern = re.sub("\$","",pattern)
    pattern = re.sub("\(","",pattern)
    pattern = re.sub("\)","",pattern)
    pattern = re.sub("\*","",pattern)
    pattern = re.sub("\/","",pattern)
    pattern = re.sub("\=","",pattern)
    pattern = re.sub("\:","",pattern)
    return pattern 

print
tokenlist = []
for filename in os.listdir('/Users/patrickwilson/Downloads/cranfieldDocs'):
    words = open('/Users/patrickwilson/Downloads/cranfieldDocs/'+filename,'r')
    readfile = words.read()
    readfile = stripSGML(readfile)
    readfile = spacePeriod(readfile)
    readfile = spaceCommaApos(readfile)
    readfile = removePunc(readfile)
    words = readfile.split()
    tokenlist.append(words)

    print readfile
    