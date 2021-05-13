def norp (arr):
    even=0
    odd=0
    for i in arr:
        if arr[i] %2 == 0:
            even+=arr[i]
        else:
            odd+=arr[i]

    if even>odd:
        return "positive"
    else:
        return "negative"

n=int(input("Enter no of elements of array"))
ar=[0]
for i in range(n):
    ar.insert(n,int(input()))
print(norp(ar))


