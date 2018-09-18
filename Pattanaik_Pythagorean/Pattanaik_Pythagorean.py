"""
Write a program that will ask the user to
enter their name and respond with a greeting using this name.
"""
from math import sqrt
a = int(input('Input the length of side a: '))
b = int(input('Input the length of side b: '))

c = sqrt(a * a + b * b)
	
print('The length of side c is: ' + str(c))
