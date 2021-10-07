# This is a python comment

'''
This is a 
multi-line 
python comment
'''

import numpy as np

def main():
		i=0					#setting i to int 0
		n=10				#setting n to int 10
		x=119.0				#setting x to float 119.0 

		#use numpy to declare arrays quickly

		y=np.zeros(n,dtype=float) #declares 10(n) zeros as floats

		# we can use for loops to iterate with a variable

		for i in range(n):		#i in range [0,n-1]
				y[i]=2.0*float(i)+1.		#sets the components of y to 2i+1

		#iterate through a variable
		for y_element in y:
				print(y_element)

	#execute the main function
if __name__=="__main__":
	main()					

