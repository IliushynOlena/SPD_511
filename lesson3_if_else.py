
22
5
1000
"Hello"

number = 15
print(15)
print(number)

a,b,c = 1 ,2,3#------------------>
print(f"{a}  {b}  {c}")
d =f =e = 10#<-------------------
print(f"{d}  {f}  {e}")
# int a;
# a = 5;
#int a = 5;
#numbers
#str - strind
login = "user"
print(login)

#operators  5    -5
#binary operators : + - * / % // **
# 12/2 = 6
# 12%2 = 0     12/2 = 6.0   6*2 = 12  12-12 = 0
# 13%2 = 1      13/2 = 6.5   6*2 = 12  13-12 = 1
print(9//2)
print(2**4)
#logic operators : < > <= >= == !=

print(5 == 5)  #True
print(5 != 5)  #False
print(5 > 1)#True
print(1 > 14)#False
print(2 < 1)#False
print(1 < 100)#True
print(100 <= 100)
#   6 ....  17
# age ....17     17 >= 6 ... 17 <= 17

print("1 == 1:", 1 == 1)         #|  1 == 1: True
print("1 == 2:", 1 == 2)         #|  1 == 2: False
print("1 != 1:", 1 != 1)         #|  1 != 1: False
print("1 != 2:", 1 != 2)         #|  1 != 2: True
print("1 > 1:", 1 > 1)           #|  1 > 1: False
print("1 > 2:", 1 > 2)           #|  1 > 2: False
print("2 > 1:", 2 > 1)           #|  2 > 1: True
print("1 < 1:", 1 < 1)           #|  1 < 1: False
print("1 < 2:", 1 < 2)           #|  1 < 2: True
print("2 < 1:", 2 < 1)           #|  2 < 1: False
print("1 >= 1:", 1 >= 1)         #|  1 >= 1: True
print("1 >= 2:", 1 >= 2)         #|  1 >= 2: False
print("2 >= 1:", 2 >= 1)         #|  2 >= 1: True
print("1 <= 1:", 1 <= 1)      #   |  1 <= 1: True
print("1 <= 2:", 1 <= 2)     #    |  1 <= 2: True
print("2 <= 1:", 2 <= 1)   #      |  2 <= 1: False

print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool("2"))
print(bool("2 5v5dsv "))
print(bool("-5"))
print(bool("5"))

# and  or   not
# True and True = True
# True and False = False
# False and True = False
# False and False = False
competent = False
responsible = False
print("----------------and---------------------")
print(competent and responsible) 
print((5 > 7)and (4 < 8))

#  or
# True and True = True
# True and False = True
# False and True = True
# False and False = False
competent = False
responsible = False
print("----------------or---------------------")
print(competent or responsible) 
print((15 > 7)or (41 < 8))

# not (!) оператор інверсії
print("----------------!---------------------")
competent = True
print(not competent)

#  if else    switch
# age = int(input("Enter age : ")) #7

# #if age >= 6 and age <= 17:
# if  6 <= age  <= 17:
#     print("Child go to school...")
# else:
#     print("Incorrect age to go to school")

#Ctrl + K + C /comment code
#Ctrl + /
#if elif else
# day = int(input("Enter number day : "))#7

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#   print("Inccorect number day")

# print("some text")


# login = input("Enter login : ")
# if login == "admin":
#     password = input("Enter password : ")
#     if password == "itstep":
#         print("Welcome to the academy")
#     elif password =="exit":
#         print("Goodbye") 
#     else:
#         print("Incorrect password")
# elif login =="exit":
#     print("Goodbye") 
# else:
#     print("Error login")

# math та random
import math
print(math.ceil(2.5))#3
print(math.floor(2.5))#2
print(math.pow(2,5))#2
print(math.sqrt(16))#2

import random
print(random.random())# 0.....1
print(random.randint(0,1))# 0,1
print(random.randint(110,200))# 100...200
print(random.randint(10,20))# 10,..20

# Уявіть, що ви прийшли в магазин, де продають магічні карамельки по 270 монет за 1 кг.
# Зараз у магазині проходить акція: при покупці більше, ніж 500 г карамелек, 
# їхня вартість дорівнює 200 монетам за 1 кг..
# Напишемо програму, яка б вважала суму покупки і ще переводила одиниці з 
# грамів у кілограмми, причому в 1 кілограмі 1000 грам.
# price_1 = 290
# price_2 = 200
# gramm = int(input("Enter weight of candies : "))
# kg = gramm/1000
# if kg < 0.5:
#     total = kg * price_1
# else:
#     total = kg * price_2
# print("You need to pay : ", total)


day = int(input("Enter number day : "))#7

if day >= 1 and day <= 5:
    print("Work day")
elif day >= 6 and day <= 7:
    print("Weeked")

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
  print("Inccorect number day")

day = int(input("Enter number day : "))#7
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Incorrect day")

match day:
    case 1,2,3,4,5:
        print("Work day")
    case 6,7:
        print("Weeked")
    case _:
        print("Incorrect day")
