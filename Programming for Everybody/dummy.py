import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url=input('Enter URL:')
uh=urllib.request.urlopen(url)

data=uh.read()
tree=ET.fromstring(data)

counts= tree.findall('comments/comment')
#counts = tree.findall('.//count')
print(counts)
c=0
for n in counts :
   c+= (int)(n.find('count').text)
   print(c)
