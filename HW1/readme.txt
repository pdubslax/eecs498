Patrick Wilson
EECS 498 – Assignment 1 
README.txt file 


The following readme contains detailed instructions on how to run all of my files and answers to the questions asked in the spec. Please don’t hesitate to contact me if you have any additional questions at pdubslax@umich.edu or 2314099896

Thanks

-----------------------------------------------------------------


1. – hw1part1.py
a) There is a function in the hw1part1.py file called stripSGML that will effectively strip all the SGML tags
b) For tokenization, I treated all the specified cases the way I was told in the spec. If you wish to see the tokenization after all punctuation is removed, you can comment out the function call on line 48. I chose to divide two numbers separated by a comma. I only separate a period if it is followed by a space which effectively keeps acronyms in tact as one token 

Running file instructions: 
1. go to line 42 and 43 and replace the file locations with the local file location of the folder containing the Cransfield collection on your machine.

I tried giving you the option to run in put the location on the command line but I was getting strange errors. Anyway just copy and past the file location over the “/afs/umich.edu/user/p/d/pdubslax/EECS_498/cranfieldDocs” string both on lines 42 and 43 



-----------------------------------------------------------------


2. – hw1part2.py
Running file instructions:
1. go to line 58 and 59 and replace the file locations with the local file location of the folder containing the Cransfield collection on your machine.

I tried giving you the option to run in put the location on the command line but I was getting strange errors. Anyway just copy and past the file location over the “/afs/umich.edu/user/p/d/pdubslax/EECS_498/cranfieldDocs” string both on lines 58 and 59 

First I collapsed all SGML tags and tokenized the text. Then I removed all punctuation so I could get good data on the actual words in the collection.

The following output is what it produced on my machine which answers the questions in the spec.

a) There are 233156 words total in the collection

b) There are 12544 unique words total in the collection

c) 
#1. "the" ----- found 19449 times
#2. "of" ----- found 12672 times
#3. "and" ----- found 6662 times
#4. "a" ----- found 5961 times
#5. "in" ----- found 4627 times
#6. "to" ----- found 4529 times
#7. "is" ----- found 4111 times
#8. "for" ----- found 3490 times
#9. "are" ----- found 2427 times
#10. "with" ----- found 2263 times
#11. "on" ----- found 1940 times
#12. "at" ----- found 1833 times
#13. "by" ----- found 1747 times
#14. "flow" ----- found 1736 times
#15. "that" ----- found 1565 times
#16. "an" ----- found 1387 times
#17. "be" ----- found 1272 times
#18. "pressure" ----- found 1133 times
#19. "from" ----- found 1116 times
#20. "as" ----- found 1111 times

d) Of those 20, I identified the following to be stop words: ['the', 'of', 'and', 'a', 'in', 'to', 'is', 'for', 'are', 'with', 'on', 'at', 'by', 'that', 'an', 'be', 'from', 'as']
and the following are not:
['flow', 'pressure']

e) 8 UNIQUE WORDS ----- is the minimum number of unique words to account for 25 percent of total words
25% of the total words is equal to 58289 words and 8 unique words account for 61501 total words


-----------------------------------------------------------------


3. – hw1part3.py
Running file instructions: 
1. go to line 62,63,94 and 95 and replace the file locations with the local file location of the folder containing the Cransfield collection on your machine.

I tried giving you the option to run in put the location on the command line but I was getting strange errors. Anyway just copy and past the file location over the “/afs/umich.edu/user/p/d/pdubslax/EECS_498/cranfieldDocs” string both on lines 62,63,94 and 95 

For my numbers, I used subsets of the first 100 documents in the collection, and the first 500 documents in the collection to derive my data.

The following output is what it produced on my machine which answers the questions in the spec.

There are 18461 total words and 2893 total unique words in the collection subset composed of the first 100 documents in the collection

There are 85532 total words and 7005 total unique words in the collection subset composed of the first 500 documents in the collection

We now have two sets of data so we can calculate constants K and beta using:
N1 = 18461 and V1 = 2893
N2 = 85532 and V2 = 7005

After solving that system of equations using Heap's Law, we can determine the constants:
K = 10.0155639382 and beta = 0.576775860244

We can now plug our constants into the Heap's Law equation to predict that:
Corpus size of 1,000,000 words, the vocabulary size would be around 28928 unique words
Corpus size of 100,000,000 words, the vocabulary size would be around 411985 unique words


-----------------------------------------------------------------


4. – hw1part4.py
Running file instructions:
1. go to line 407 and 408 and replace the file locations with the local file location of the folder containing the Cransfield collection on your machine.

I tried giving you the option to run in put the location on the command line but I was getting strange errors. Anyway just copy and past the file location over the “/afs/umich.edu/user/p/d/pdubslax/EECS_498/cranfieldDocs” string both on lines 407 and 408 

I used the porter stemmer from the class page and removed all stop words and punctuation before doing the stemming. 

The following output is what it produced on my machine which answers the questions in the spec.



Output:

There are 147464 words total in the collection

There are 9772 unique words total in the collection

The top 20 words are:

#1. "flow" ----- found 1965 times
#2. "number" ----- found 1337 times
#3. "pressur" ----- found 1308 times
#4. "result" ----- found 1086 times
#5. "effect" ----- found 990 times
#6. "boundari" ----- found 926 times
#7. "method" ----- found 884 times
#8. "theori" ----- found 869 times
#9. "layer" ----- found 859 times
#10. "solut" ----- found 847 times
#11. "mach" ----- found 817 times
#12. "equat" ----- found 778 times
#13. "bodi" ----- found 740 times
#14. "us" ----- found 730 times
#15. "wing" ----- found 710 times
#16. "present" ----- found 699 times
#17. "heat" ----- found 686 times
#18. "surfac" ----- found 661 times
#19. "obtain" ----- found 643 times
#20. "distribut" ----- found 640 times

According to the class provided stopword list, the following of those top 20 are stopwords:
['us']

And the following words are not:
['flow', 'number', 'pressur', 'result', 'effect', 'boundari', 'method', 'theori', 'layer', 'solut', 'mach', 'equat', 'bodi', 'wing', 'present', 'heat', 'surfac', 'obtain', 'distribut']

60 UNIQUE WORDS ----- is the minimum number of unique words to account for 25 percent of total words
25% of the total words is equal to 36866 words and 60 unique words account for 36970 total words


-----------------------------------------------------------------


5.
Running file instructions:

1. $ python hw1part5.py
2. $ (the number or urls that you wish to crawl)

Extra Info:

I have implemented certain restrictions in the web crawler to accommodate the robots.txt file for eecs.umich.edu
Using import robotparser I can check each link that I am about to crawl to see if it complies with the restraints specified in the robots.txt file

I did not include links that ended in extensions that I didn’t want and I also had a 1 second sleep between each crawl as a respect to the eecs.umich.edu servers

There are some comments in the code you can adjust if you want to print the links to the terminal or not on line 68

I had to include two special cases for skipping the crawling of specific urls because of some malformed html on the pages. 

I limited my web crawl to urls within the eecs.umich.edu subdomain so all the necessary disallowed URLs are handled by the one robots.txt file

I submitted a list of all 1500 URLs that I found originally in a file called part5urls.txt
