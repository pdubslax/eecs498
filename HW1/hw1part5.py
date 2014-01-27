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
		if link[2].startswith("http://www.eecs.umich.edu") and link[2].endswith("html") :
			newfoundlinks.append(link[2])
	return newfoundlinks
			 



	 
page = requests.get('http://www.eecs.umich.edu') 
tree = html.fromstring(page.text) 
found_links = ["http://www.eecs.umich.edu"]
searched_links = ["http://www.eecs.umich.edu"]

for link in tree.iterlinks(): 
 if link[2].startswith("http://www.eecs.umich.edu") and (link[2] not in searched_links) and link[2].endswith("html") :
 	found_links.append(link[2])
 	
past_num = len(found_links)
while len(found_links)<1500:
	past_num = len(found_links)
	print len(found_links)

	return_list = []
	
	for all_found in found_links:
		function_list = []
		if all_found not in searched_links:
			searched_links.append(all_found)
			function_list = crawl(all_found)
		return_list = return_list + function_list

	#here you have this return_list of all links after searching one layer
	for boom in return_list:
		if boom not in found_links:
			found_links.append(boom)

	if past_num==len(found_links):
		for link in found_links:
			print link
		break


 	
 









