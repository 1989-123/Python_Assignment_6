""" Write a python script to print greater between two numbers.
Print number only once even if the numbers are the same."""

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x > y:
    print("%d is greter than %d" %(x, y))
elif x < y:
    print("%d is greter than %d" %(y, x))
else:
    print("Numbers are same")
