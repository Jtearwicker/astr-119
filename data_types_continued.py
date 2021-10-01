#string

s="I am a string"
print(type(s)) #returns string

#boolean
yes=True
print(type(yes))

no=False
print(type(no))

#list - ordered and changeable

alpha_list=["a","b","c"]	#list initialization
print(type(alpha_list))		#will print 'tuple'
print(type(alpha_list[0]))	#will print 'string'
alpha_list.append("d")		#will add "d" to the end of the list
print(alpha_list)			#will print list

#tuple - ordered and unchangeable

alpha_tuple=("a","b","c")	#tuple initialization
print(type(alpha_tuple))	#will print 'tuple'

try:						#will attempt the following line
	alpha_tuple[2]="d"
except TypeError:
	print("We can't add elements to tuples!")  #print this message if TypeError
print(alpha_tuple)

