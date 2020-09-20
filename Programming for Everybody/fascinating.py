import collections
num=int(input('Enter a number'))
data=str(num)+str(num*2)+str(num*3)
list1=[]
list2=[1,2,3,4,5,6,7,8,9]
for x in data:
    list1.append(int(x))

list1.sort()

if collections.Counter(list1)==collections.Counter(list2):
    print('Facinating number')
else:
    print('Not Fascinating number')
