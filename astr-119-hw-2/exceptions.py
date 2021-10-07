#python exceptions let you deal with unexpected results

try:
	print(a)		#this will throw and exception since a is not defined
except:
	print("a is not defined")

#there are specific errors to help with cases
try:
	print(a)		#this will throw and exception since a is not defined
except NameError:
	print("a is still not defined")
except:
	print("Something else went wrong")

#this will break our program
print(a)