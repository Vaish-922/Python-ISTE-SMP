def multiples(m,n):
    arr= range(n,m*n+1,n)
    return arr

m=int(input("Enter the no of multiples: "))
n=int(input("Enter the no: "))
print("The Multiples are: \n", *multiples(m,n))