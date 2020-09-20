import urllib.request,urllib.parse,urllib.error
import json

url=input('Enter location:')
uh=urllib.request.urlopen(url)

data=uh.read()


info = json.loads(data)

sum=0
for k,v in info.items():
    if k=="comments":
        for x in range(len(info[k])):
            sum=sum+int(v[x]['count'])

print(sum)
