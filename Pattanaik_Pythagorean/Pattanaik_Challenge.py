
from math import sqrt

from math import sqrt
a = int(input('Input the length of side a: '))
b = int(input('Input the length of side b: '))
c = int(input("Input the length of side c: "))

if c == sqrt(a * a + b * b):
    print ("This is a right triangle")
elif c < sqrt(a * a + b * b):
    print ("this is an acute angle")
elif c > sqrt(a * a + b * b):
    print ("this is an obtuse angle")
else:
    print ("This is not a triangle")
	

