import re,zipfile


file = zipfile.ZipFile("channel.zip")

num = "29"#first archive in .zip

while True:
    archieve = file.read(num+".txt") #take the information from the .zip
    print archieve
    match = re.search('Next nothing is ([-+]?\d+)',archieve) #take the value after check the pattern, ([-+]?\d+) is equivalent by scanf("%d"), the regex divide the information based on the numbers of the terms
    num = match.group(1) #update the number of archieve
