import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)		#return the numpy e^x function

def show_expo(n):
	for i in range(n):
		print(expo(float(i)))		#call the expo function

def main():
	n=10	#provide a default value for n

	#check if there is a command line argument provided 
	if(len(sys.argv)>1):
		n=int(sys.argv[1])		#if an argument was provided, use it for n

	show_expo(n)		#call the show_expo subroutine
	
#run the main funciton
if __name__=="__main__":
	main()				