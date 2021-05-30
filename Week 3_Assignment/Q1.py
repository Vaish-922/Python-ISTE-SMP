n1=int(input())
d1 = dict()

for i in range(0,n1):
        word = input().split()
        key = word[0]
        value = word[1]
        d1[key]=value

n2=int(input())
d2 = dict()

for i in range(0,n2):
        word = input().split()
        key = word[0]
        value = word[1]
        d2[key]=value

for i in d1:
  if i in d2.keys():
    d2[i]=d2[i]+d1[i]
  else:
    d2[i]=d1[i]

print(d2)