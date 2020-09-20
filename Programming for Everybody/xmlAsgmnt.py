import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url=input('Enter URL:')
uh=urllib.request.urlopen(url)

data=uh.read()
tree=ET.fromstring(data)

counts= tree.findall('comments/comment')
#print(counts)
#print(len(counts))

sum=0
for x in counts :
    sum=sum+int(x.find('count').text)

print(sum)
