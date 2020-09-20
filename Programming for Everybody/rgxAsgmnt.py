import re
file=open('F:\Coursera\\files\\regex_sum_875023.txt')

lst=list()

for line in file:
    line=line.rstrip()
    lst1=re.findall('([0-9]+)',line)
    if len(lst1)>0:
        for eachElement in lst1:
            lst.append(eachElement)

sum=0
for x in lst:
    sum=sum+int(x)

print(sum)
