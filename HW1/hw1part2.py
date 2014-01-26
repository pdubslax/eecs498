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


num_lines = 0
num_words = 0
num_chars = 0
worddic = {}
print
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

print "{}{}{}".format("There are ",num_words," words total in the collection")
print
print "{}{}{}".format("There are ",len(worddic)," unique words total in the collection")
print
print "{}".format("The top 20 words are:")
print
############################################################
iters = 0
stopword20 = []
goword20 = []
sorted_count = sorted(worddic.iteritems(), key=operator.itemgetter(1), reverse=True)
for word, times in sorted_count:
    if isStopword(word):
        print "#%d. \"%s\" ----- found %d times" % (iters+1,word, times)
        stopword20.append(word)
    else:   
        print "#%d. \"%s\" ----- found %d times" % (iters+1,word, times)
        goword20.append(word)
    iters+=1
    if iters>19:
        print
        break

print "{}".format("According to the class provided stopword list, the following of those top 20 are stopwords:")
print stopword20
print
print "{}".format("And the following words are not:")
print goword20
print

final_number = num_words/4
running_total_words = 0
iter_num = 0
for word,times in sorted_count:
    iter_num += 1
    running_total_words += times
    if running_total_words>final_number:
        print "{}{}".format(iter_num," UNIQUE WORDS ----- is the minimum number of unique words to account for 25 percent of total words")
        print "{}{}{}{}{}{}{}".format("25% of the total words is equal to ",final_number," words and ",iter_num," unique words account for ",running_total_words, " total words")

        print
        break






    



