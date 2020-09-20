import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup



url=input('Enter URL:')
count=int(input('Enter count:'))
position=int(input('Enter position:'))
x=0

while x<count:
    lst=list()
    #print('Before tag',url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href'))
    url=lst[position-1]
    #print('After tag',url)
    x=x+1

print(url[39:url.find('.html')])
