# Write a python script to print two given words in dictionary order

x = str(input("Enter a word: "))
y = str(input("Enter a word: "))

if x > y:
    print(y, x)
else:
    print(x, y)
