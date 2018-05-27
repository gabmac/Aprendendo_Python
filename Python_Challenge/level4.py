import urllib2 #library for access urls
import re

page = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
number = "12345"

#the while will run while the informations exists, after this will crash
while True:
    page1 = page + number
    information = urllib2.urlopen(page1).read() #take the information from the website
    print information #show the information
    match = re.search('and the next nothing is ([-+]?\d+)',information) #take the value after check the pattern, ([-+]?\d+) is equivalent by scanf("%d"), the regex divide the information based on the numbers of the terms
    number = match.group(1)
    if number == "16044": #after this number we need to divide the number by 2
        number = str(16044/2)
