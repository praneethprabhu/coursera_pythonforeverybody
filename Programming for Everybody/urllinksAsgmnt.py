import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url='http://py4e-data.dr-chuck.net/comments_875025.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
lst=list()
for tag in tags:
    lst.append(int(tag.contents[0]))

sum=0
for x in lst:
    sum=sum+x

print(sum)
