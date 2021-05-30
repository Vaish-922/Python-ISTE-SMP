str = input("Enter A String: ")
d1=dict()
for i in str:
    if i in d1.keys():
        d1[i]+=1
    else:
        d1[i]=1

print(d1)