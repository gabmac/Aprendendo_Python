#this challenge wants that you shift in two words all the text

#import thing: ord() convert a letter in decimal, chr() convert a decimal in a word, using ascii table

#this library allow to work with strings
import string

text =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
answer = ""
for x in text:  #
        if ord(x) < 66: #values that does not represent a character
            answer += x
        else:
            if ord(x) <= 120: #values of the last two chars of ascII table
                answer += chr(ord(x)+2)
            else:
                answer += chr(ord(x)-24) #transform y and z in a and b respectively

print answer


#applying in the url
url = "map"
answer = ""
for x in url:  #
        if ord(x) < 66: #values that does not represent a character
            answer += x
        else:
            if ord(x) <= 120: #values of the last two chars of ascII table
                answer += chr(ord(x)+2)
            else:
                answer += chr(ord(x)-24) #transform y and z in a and b respectively

print answer
