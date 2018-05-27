import urllib2
import pickle #pick hell


page = "http://www.pythonchallenge.com/pc/def/banner.p"

information = urllib2.urlopen(page) #take the information as object

data = pickle.load(information)#de-serielize the pickle object

print data
