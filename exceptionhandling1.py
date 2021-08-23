#nameError
l1 = [1,2,3,4,5]
l2 = [1,2.4,"python"]
l1[1] = 100
print(l1)
del l[2]
 
#overflowError
a = 100
b = 289.00
try:
    print("the addition is:", a**b)
except(OverflowError):
    print("overflow error occured")


#SyntaxError
a = 10
b = 20
c = a b

#identationError
for i in range(10):
print('Hello World')
typeError
a = 2
b = 'Python'
a + b

#Unboundlocalerror
x = 20
try:
    def exceptiongandling():
        print(x)
        x=x+1
    exceptionhandling()
except:
   print("this is UnboundLocalError:")

#ValueError
try:
    print (float('exceptionhandling'))
except:
    print ('valueError: could not convert string to float')
else:
    print ('sucess, no error.')


#ZerodivisionError
100/0