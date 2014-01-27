#Patrick Wilson 
#EECS 498 HW 1


#!/usr/bin/env python
import re
import sys
import os
import operator
import math

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

stopwordlist = ["a","all","an","and","any","are","as","be","been", 
"but","by","few","for","have","he","her","here","him","his","how",  
"i","in","is","it","its","many","me","my","none","of","on","or", 
"our","she","some","the","their","them","there","they","that", 
"this","us","was","what","when","where","which","who","why","will", 
"with","you","your"]

def isStopword(word):
    for stopword in stopwordlist:
        if (word==stopword):
            return True
    return False



num_words = 0
worddic = {}
print

iter_num = 0
for filename in os.listdir('/Users/patrickwilson/Downloads/cranfieldDocs'):
    words = open('/Users/patrickwilson/Downloads/cranfieldDocs/'+filename,'r')
    readfile = words.read()
    readfile = stripSGML(readfile)
    readfile = spacePeriod(readfile)
    readfile = spaceCommaApos(readfile)
    readfile = removePunc(readfile)
    #possibly remove numbers
    
    words = readfile.split()
    for word in words:
            if word in worddic:
                worddic[word] += 1
            else:
                worddic[word] = 1
    num_words += len(words)
    iter_num+=1
    if iter_num>100:
        break



print "{}{}{}{}{}{}{}".format("There are ",num_words," total words and ",len(worddic)," total unique words in the collection subset composed of the first ",iter_num-1," documents in the collection")
n1 = num_words
v1 = len(worddic)


num_words = 0
worddic = {}


iter_num = 0
for filename in os.listdir('/Users/patrickwilson/Downloads/cranfieldDocs'):
    words = open('/Users/patrickwilson/Downloads/cranfieldDocs/'+filename,'r')
    readfile = words.read()
    readfile = stripSGML(readfile)
    readfile = spacePeriod(readfile)
    readfile = spaceCommaApos(readfile)
    readfile = removePunc(readfile)
    #possibly remove numbers
    
    words = readfile.split()
    for word in words:
            if word in worddic:
                worddic[word] += 1
            else:
                worddic[word] = 1
    num_words += len(words)
    iter_num+=1
    if iter_num>500:
        break


print "{}{}{}{}{}{}{}".format("There are ",num_words," total words and ",len(worddic)," total unique words in the collection subset composed of the first ",iter_num-1," documents in the collection")
print
n2 = num_words
v2 = len(worddic)

logn1 = math.log(n1)
logn2 = math.log(n2)
logv1 = math.log(v1)
logv2 = math.log(v2)

beta = (logv2 - logv1)/(logn2- logn1)
K = v1/(n1**beta)


print "{}".format("We now have two sets of data so we can calculate constants K and beta using:")
print "{}{}{}{}".format("N1 = ",n1," and V1 = ",v1)
print "{}{}{}{}".format("N2 = ",n2," and V2 = ",v2)
print
print "{}".format("After solving that system of equations using Heap's Law, we can determine the constants:")
print "{}{}{}{}".format("K = ",K," and beta = ",beta)
print
mil_result = int((1000000**beta)*K)
hun_mil_result = int((100000000**beta)*K)

print "{}".format("We can now plug our constants into the Heap's Law equation to predict that:")
print "{}{}{}".format("Corpus size of 1,000,000 words, the vocabulary size would be around ",mil_result," unique words")
print "{}{}{}".format("Corpus size of 100,000,000 words, the vocabulary size would be around ",hun_mil_result," unique words")
print





