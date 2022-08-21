""" Write a python script to check whether a given quadratic equation
has two real & distinct roots, real & equal roots or imaginary roots """

print("Enter values of a,b and c: ")
a, b, c=int(input()),int(input()),int(input())
d = b**2 - 4 * a * c
if d > 0:
    print("Real & Distinct roots")
elif d == 0:
    print("Real & Equal roots")
else:
    print("Imaginary roots")
