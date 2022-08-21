""" Write a python script to check whether a given year
is a leap year or not """

x = int(input("Enter a year:"))
result = "Leap Year" if x % 400 == 0 or x % 100 and x % 4 ==0 else "Non Leap Year"
print(result)
