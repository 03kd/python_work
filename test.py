import random
n=input()
a=int(n)
list_1=[]
for i in range(a):
    k=int(input())
    list_1.append(k)
l=list(list_1)
list_1.sort()
while(l!=list_1):
    x=random.randint(0,len(list_1)-1)
    y=random.randint(0,len(list_1)-1)
    z=l[x]
    l[x]=l[y]
    l[y]=z
for i in range(0,a):
  	print(l[i],end=" ")