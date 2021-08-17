#Find ASCII Value of a character 'X' and 'x'
a = 'x'
b = 'X'
print("the ASCII value of x",ord(a) )
print("the ASCII value of X",ord(b) )


#Swap two numbers using temporary variable
x=5
y=10
temp=x
x=y
y=temp
print('the value of x after swapping:{}'.format(x))
print('the value of y after swapping:{}'.format(y))

#Write Program to Compute Quotient and Remainder
x=5
y=10
q=x/y
print("Quotient is:",q)
r=x%y
print("Remainder is:",r)

#write whether the no is even or odd
num = int(input("Enter a number:"))
if(num % 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))

#Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

#Write Programm to calculate GST i.e. 18% on base price 34900/-
gst=34900
o=gst*(18/100)
print("\n GST on rs34900 is:",o)

#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

#Simple INterest
p=161258
r=5
t=1

si=p*r*t*0.01

print("Simple Interest : ",si)

#Compound Interest

Amount = p * (pow((1 + r / 100), t))
ci = Amount - p 
print("Compound interest is", ci)

#Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-
emi=161258
emi3=emi/(12*3)
emi5=emi/(12*5)
#print("\n Emi after 3 year without interest",emi3)
#print("\n Emi after 5 years",emi5)
emin3=emi3+((5/100)*emi3)
emin5=emi5+((5/100)*emi5)
print("\n Emi after 3 year with interest",emin3)
print("\n Emi after 5 years with interest",emin5)