# Reverse a String and print it on console "Python Skills"
str = "Python Skills"
str = str[::-1]                             
print("reversing string: " + str)

# Assign String to x variable in DD-MM-YYYY format extract and print Year from String
x = '19-08-2021'
# Print Year from the string
print(x[6:])

# In a small company, the average salary of three employees is Rs1000 per week.If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn?

average = 1000
e1 = 1100
e2 = 500
e3 = (average - (e1 + e2)/3)*3                 
print("Salary of Third employee is: ", e3)

#Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)
per = 30
frac = per / 100
print ("Fraction of 30% is:")
print(frac)

# Write Program - A train 340 m long is running at a speed of 45 km/hr. What time will it take to cross a 160 m long tunnel?
trainlen = 340
tunnellen = 160
total = trainlen + tunnellen
speed = 45
mps = 5/18
time = total / (45 * mps)
print ("Total time taken by train to cross the tunnel is: ",time)