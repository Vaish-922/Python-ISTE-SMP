n=int(input("Enter the value of n: "))
a=0
b=1
sum=0
count = 1
print("The series is: \n")
while(count <=n):
    print(sum,end= ' ')
    count+=1
    a=b
    b=sum
    sum=a+b