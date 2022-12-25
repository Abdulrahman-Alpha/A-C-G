#<<<<1>>>>>

# fahrenheit = float(input("Enter your temperature degree in Fahrenheit= "))
# celsius = (fahrenheit-32)/1.8

# print("\nYour temperature degree in celsius=",celsius )
#####################################################################################################################
####################################################################################################################
#<<<<2>>>>>

# km = float(input("Enter your distance in km= "))
# miles= km*0.62

# print("\nYour distance in miles=", miles)
####################################################################################################################
####################################################################################################################
# <<<<3>>>>>

# kg = float(input("Enter the weight in Kilograms: "))
# Ibs = kg * 2.20462

# print("\nThe weight in pounds=", Ibs)
####################################################################################################################
####################################################################################################################
#<<<<4>>>>>

# import math
# radius= float(input("Enter your sphere radius= "))
# volume= (4/3)*(math.pi)*(math.pow(radius,3))
# area= 4*math.pi*math.pow(radius,2)

# print('\nYour sphere volume=', volume)
# print('Your sphere area=', area)
####################################################################################################################
####################################################################################################################
#<<<<5>>>>>

# H_weight = 1.00794
# C_weight = 12.0107
# O_weight = 15.9994

# H_atoms = int(input("Enter the number of hydrogen atoms: "))
# C_atoms = int(input("Enter the number of Carbon atoms: "))
# O_atoms = int(input("Enter the number of Oxygen atoms: "))

# Molecular_Weight= ((H_atoms*H_weight) + (C_atoms*C_weight) + (O_atoms*O_weight))

# print("\nThe molecular weight=", Molecular_Weight)
####################################################################################################################
####################################################################################################################
#<<<<6>>>>>

# import math

# print("Enter the coordinates of the point P1(x1,y1):")
# x1= float(input("x1= "))
# y1= float(input("y1= "))

# print("\nEnter the coordinates of the point P2(x2,y2):")
# x2= float(input("x2= "))
# y2= float(input("y2= "))

# Slope = (y2-y1)/(x2-x1)
# print("\n\nThe slope of a line through the 2 points=",Slope)
####################################################################################################################
####################################################################################################################
#<<<<7>>>>>

# import math

# print("Enter the coordinates of the point P1(x1,y1):")
# x1= float(input("x1= "))
# y1= float(input("y1= "))

# print("\nEnter the coordinates of the point P2(x2,y2):")
# x2= float(input("x2= "))
# y2= float(input("y2= "))

# X= x2-x1
# Y= y2-y1

# distance = math.sqrt(math.pow(X,2) + math.pow(Y,2))
# print("\n\nThe distance between the 2 points=",distance)
####################################################################################################################
####################################################################################################################
#<<<<8>>>>>

# pounds= float(input("Enter the number of pounds: ")) 
# coffee_cost= 10.5 * pounds 
# shipping_cost= 1.50 + 0.86 * pounds
# total= coffee_cost + shipping_cost 
# print("\nTotal cost \"including shipping\"=",total)
####################################################################################################################
####################################################################################################################
#<<<<9>>>>>
# import math
# a= float(input("Enter the first side length of the triangle: "))
# b= float(input("Enter the first side length of the triangle: "))
# c= float(input("Enter the first side length of the triangle: "))

# s = (a+b+c)/2

# area= math.sqrt(s*(s-a)*(s-b)*(s-c))

# print("\nArea of the triangle= ", area)
####################################################################################################################
####################################################################################################################
#<<<<10>>>>>

# import math

# height= float(input("Enter the height: "))
# angle= float(input("Enter the angle: "))

# radians= ((math.pi/180)*angle)

# length = (height / math.sin(radians))

# print("\nThe length of ladder=",length)
####################################################################################################################
####################################################################################################################
# #<<<<11>>>>>
# n= int(input("Enter n \"natural numbers\": "))
# sum = 0
# sumCubes = 0

# for i in range(n+1):
#     sum += i

# for i in range(n+1):
#     sumCubes += pow(i,3)

# print("\nThe sum of the first", n ,"natural numbers=",sum)
# print("\nThe sum of the cubes of the first", n ,"natural numbers=",sumCubes)
####################################################################################################################
####################################################################################################################
#<<<<12>>>>>

# n = int(input("Enter the number of values: ")) 
# sum = 0 
# for i in range(n): 
#     sum += float(input("Next number: ")) 
# print("The sum=",sum)
####################################################################################################################
####################################################################################################################
#<<<<13>>>>>

# n = int(input("Enter  the number of values: ")) 
# sum = 0 
# for i in range(n): 
#     sum += float(input("Next number: ")) 
# print("The average=",sum/n)
####################################################################################################################
####################################################################################################################
#<<<<14>>>>>

####################################################################################################################
####################################################################################################################
#<<<<15>>>>>

nterm = int(input("Enter number of terms: "))

n1,n2 = 1, 1

count = 0

if nterm <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci sequence:")
   while count < nterm:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1