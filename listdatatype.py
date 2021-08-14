#extract all list
x=[1,2,'python',4,5,'list',7,'datatype',9,10]
print("list x:",x[:])

#extract index number 2 to 5
print("list x: 2 to 5", x[1:6]) 

#print list element reverse
print("list x in reverse:",x[::-1])

#using append, insert/add element in list
#append
x.append('java')
print("list x after appending:",x[:])
#insert
x.insert(5,'language')
print("list x after inserting:",x[:])

#using pop,remove,del element
#pop
x.pop(2)
print("list x after poping:",x[:])
#remove
x.remove('datatype')
print("list x after removing:",x[:])
#delete
del x[6]
print("list x after deleting:",x[:])

#clear a list
x.clear()
print("list x after clearing:",x[:])







