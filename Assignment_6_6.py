""" Write a python script to check whether a given number
is a three digit number or not."""

x = int(input("Enter a number: "))
y = 0
i = 1
while i <= 3:
    y = x % 10
    x = x // 10
    if x == 0:
        break
    else:
        i+=1
if i != 3:
    print("Not a three digit number")
elif x == 0:
    print("Yes three digit number")
