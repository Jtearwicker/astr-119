import numpy as np 

#integers

i=10	#integer
print(type(i))	#print out the data type of i

a_i=np.zeros(i,dtype=int)	#declare an array of ints
print(type(a_i))	#will return an n-dimensional array (ndarray)
print(type(a_i[0]))	#will return a 64 bit integer(int64)

#floats

x=119.0
print(type(x))	#prints out the data type of x

y=1.19e2
print(type(y))	#prints out the data type of y

z=np.zeros(i,dtype=float)	#declare an array of floats
print(type(z))				#will return ndarray
print(type(z[0]))			#will return int64