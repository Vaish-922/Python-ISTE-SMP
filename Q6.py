vowels={'a','e','i','o','u'}

def genstr(str):
    newstr=''
    for i in str:
        if i in vowels:
            newstr+=i
    for i in str:
        if i not in vowels and i!=' ':
            newstr+=i

    return newstr

a=input("Enter a string")
print("String after modification is: ", genstr(a))

