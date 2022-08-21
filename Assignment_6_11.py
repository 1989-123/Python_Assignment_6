""" Write a python script to take the month value in numeric format
and display the number of days in it. """

month = int(input("Enter a month number: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12:
    print("31 days a month")
elif month == 2:
    print("28 or 29 days a month")
else:
    print("30 days a month")
