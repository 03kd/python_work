def check(op):
    vow =['a','e','i','o','u']
    #print('as]sdfewrewdsd')
    for i in vow:
        if i==op:
            print('true')
            return True
            
        else:
            print('fladsed')
            return False


s ='great'

k=[]
l=[]
words= s.split()
for word in words:
    for character in word:
        k.append(character)
        #print(character)
        
count=0
while(count<len(k)-1):
    a=check(k[count])
    b=check(k[count+1])
    if (a==True or b==True):
        l.append(k[count])
    
    count+=1
    
print(l)
