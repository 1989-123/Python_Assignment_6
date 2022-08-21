""" Write a python script to print greater among three numbers.
Print number only once even if the numbers are the same. """

a ,b, c = 20, 30, 10

if a > b:
    if a > c:
        print("%d is greter" %(a))
    else:
        print("%d is greter" %(c))
elif b > c:
    print("%d is greter" %(b))
else:
    print(("%d is greter" %(c)))
