str =input("Enter a string: ")
x=0;
word = "are"
for i in str.split():
    if i == word:
        x+=1

print(x)