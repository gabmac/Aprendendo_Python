import re #import regex library

data = open("work.txt","r").read() #open the document with the txt

match = re.findall('([^A-Z])([A-Z])([A-Z])([A-Z])([a-z])([A-Z])([A-Z])([A-Z])([^A-Z])',data) #find the pattern, ([^A-Z] match anything other than uppercase letter)
#there is something really important: the match is only okay if there is only 3 uppercase letter before only 3 uppercase letters after
for x in match:
    print x[4],
