x=[]
for i in range(1,11):
    x.append(i)
print ("Original list:",x)
d=x[0:5]
print ("Extracted first five elements:",d)
d.reverse()
print ("Reversed extracted element: ",d)