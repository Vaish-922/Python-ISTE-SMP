str = input("Enter main string: ")
substr=input("Enter sub string: ")
max =0
for i in range(len(str)):
    if str[i] in substr:
        if i>max:
            max=i

print(str[:max+1])