def factorial(i):
    fact =1
    for j in (range(i)):
        fact= fact*(j+1)
    return fact



a=int(input("Enter the no: "))
print("The factorial of ",a," is ",factorial(a))