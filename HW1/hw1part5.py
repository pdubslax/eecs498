#Patrick Wilson 
#EECS 498 HW 1

from lxml import html 
import requests 
import re
import sys
import os


def crawl(page):
	


	newfoundlinks = []

	page = requests.get(page) 
	tree = html.fromstring(page.text)



	for link in tree.iterlinks(): 
		if (('.umich.edu' in link[2]) and ('.js' not in link[2]) 
			and ('.css' not in link[2]) and ((link[2].endswith(".html") 
			or link[2].endswith(".htm"))or( link[2].endswith(".txt")==False
			and  link[2].endswith(".mov")==False and  link[2].endswith(".gif")==False 
			and  link[2].endswith(".rss")==False and  link[2].endswith(".mp4")==False 
			and  link[2].endswith(".jpg")==False and  link[2].endswith(".doc")==False 
			and  link[2].endswith(".jpeg")==False and  link[2].endswith(".ogv")==False 
			and  link[2].endswith(".pdf")==False and link[2].endswith(".png")==False 
			and link[2].endswith(".css")==False and link[2].endswith(".js")==False 
			and link[2].endswith(".ico")==False and link[2].endswith(".xml")==False))):
			newfoundlinks.append(link[2])
	return newfoundlinks
			 



	 

found_links = ["http://www.eecs.umich.edu"]
past_num = len(found_links)
function_list = []
end_condition = False

while True:

	

	for all_found in found_links:	
		function_list = crawl(all_found)
		for boom in function_list:
			if boom not in found_links:
				found_links.append(boom)
				#print boom
				if len(found_links)>1500:
					end_condition = True
			if end_condition:
				break
		function_list[:]
		if end_condition:
			break

	if end_condition:
		break


for gdg in found_links:
	print gdg








