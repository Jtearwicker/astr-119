def flow_control(k):
	if(k==0): 
		s="Variable k = %d equals 0." %k
	elif(k==1):
		s="Variable k = %d equals 1." %k
	else: 
		s="Variable k= %d does not equal 0 or 1." %k

		print(s)		#function takes in variable k and checks if it is 0, 1, or neither, then prints the result

def main(): #test each case (0,1,other)
	i=0 
	flow_control(i)
	i=1
	flow_control(i)
	i=5
	flow_control(i)

if __name__=="__main__":
	main()