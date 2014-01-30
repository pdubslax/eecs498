#Patrick Wilson 
#EECS 498 HW 1

from lxml import html 
from time import sleep
import requests 
import re
import sys
import os



def crawl(page):
	


	newfoundlinks = []
	if (page == "http://www.eecs.umich.edu/~bnoble/"
		or page == "http://http://www.eecs.umich.edu/eecs/academics/courses/eecs-461.html/eecs/academics/courses/course.html?id=23"):
		return newfoundlinks


	sleep(1)
	page = requests.get(page) 
	tree = html.fromstring(page.text)



	for link in tree.iterlinks(): 
		if (('http://www.eecs.umich.edu' in link[2]) and ('.js' not in link[2]) 
			and ('.css' not in link[2]) and ((link[2].endswith(".html") 
			or link[2].endswith(".htm"))or( link[2].endswith(".txt")==False
			and  link[2].endswith(".mov")==False and  link[2].endswith(".gif")==False 
			and  link[2].endswith(".rss")==False and  link[2].endswith(".mp4")==False 
			and  link[2].endswith(".jpg")==False and  link[2].endswith(".doc")==False 
			and  link[2].endswith(".jpeg")==False and  link[2].endswith(".ogv")==False 
			and  link[2].endswith(".pdf")==False and link[2].endswith(".png")==False 
			and link[2].endswith(".css")==False and link[2].endswith(".js")==False 
			and link[2].endswith(".ico")==False and link[2].endswith(".xml")==False))
			and link[2].startswith("https://www.eecs.umich.edu/~smbrain")==False
			and link[2].startswith("https://www.eecs.umich.edu/robots.txt")==False
			and link[2].startswith("https://www.eecs.umich.edu/courses")==False
			and link[2].startswith("https://www.eecs.umich.edu/etc/")==False
			and link[2].startswith("https://www.eecs.umich.edu/~imarkov/5")==False
			and link[2].startswith("https://www.eecs.umich.edu/etc/calendar")==False
			and link[2].startswith("https://www.eecs.umich.edu/eecs/etc/calendar")==False
			and link[2].startswith("https://www.eecs.umich.edu/techday")==False
			and link[2].startswith("https://www.eecs.umich.edu/vlsipool")==False):
			newfoundlinks.append(link[2])
	return newfoundlinks
			 



	 
var = input('Please enter the number of urls that you want to crawl: ')
found_links = ["http://www.eecs.umich.edu"]
past_num = len(found_links)
function_list = []
end_condition = False

while True:
	for all_found in found_links:	
		#print all_found
		function_list = crawl(all_found)
		for boom in function_list:
			if boom not in found_links:
				found_links.append(boom)
				#print boom
				if len(found_links)>var:
					end_condition = True
			if end_condition:
				break
		function_list[:]
		if end_condition:
			break

	if end_condition:
		break

print "{}{}{}".format("The crawler successfully found ",var," links!")

'''
print "------------------------------------------------------"
for gdg in found_links:
	print gdg
print
'''








