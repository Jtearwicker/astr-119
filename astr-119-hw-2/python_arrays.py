x=[0.0,3.0,5.0,2.5,3.7]
print(type(x))

x.pop(2)	#will remove the third element (python starts counting at 0)
print(x) 

x.remove(2.5)	#will remove all elements with the value 2.5
print(x)

x.append(1.2)	#will add an element to the end
print(x)

y=x.copy()		#make a copy of x and save it in y
print(y)

print(y.count(0.0))	#will print	how many elements are in y

y.sort()	#will sort the array from lowest to highest
print(y)

y.reverse()	#will sort the arrya from highest to lowest
print(y)

y.clear()	#will remove all elements
print(y)