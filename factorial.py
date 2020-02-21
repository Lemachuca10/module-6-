#Luis Machuca
#In this program the user can calculate the factorial of a user input x value

import math

number = int(input("enter the number: "))
fac = 1

for i in range(1,number + 1):
    fac = fac * i
print ("factorial of", number , " is ", fac) 
