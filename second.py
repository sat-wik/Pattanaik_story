print("Hello. What is your name?")
x = input()
print("How old are you " + x)
a = input()
if a.isdigit():
	y = int(a)
	print ("You are " + a)
	b=15
	if y <= b:
    	print("Wow you are pretty young")
	elif y > b:
    	print("Thats tough")
else:
	print("That's not an int!")



