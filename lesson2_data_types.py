#Літерали Python
print("2")
print(210)

print(210)
print("210")
print("hello")
print(2+2)
print(4*2)
# Data types  
#Числові , символьні і логічні
#numbers --> int (integer)(15), float (3.14)
#str
#boolean  --> True False

#Shift + Alt + arrow down
print(" int ", type(2))
print(" float ", type(2.35))
print(" str ", type('Hello'))
print(" str ", type('a'))
print(" str ", type('2'))
print(" bool ", type(True))
print(" bool ", type(False))


##Основні оператори  + - * / //  % ** бінарні(два значення)

print(5+2)
print(5-2)
print(5*2)
print(5/2)

print(5**2)#int
print(5**2.)#float
print(5.**2)#float
print(5.**2.)#float

print(6/3)# 2
print(8/3)#2.33

#ділення цілих чисел // - відкидає дробову частинку
print(6//3)# 2
print(8//3)#2.33

# % - ділення за модулем, з остачею
print(12/4)#3.0
print(12%4)# 12/4 =3   3*4=12  12-12 = 0
print(13/4)#3.25
print(13%4)# 13/4 =3.25   3*4=12  13-12 = 1


#  унірні  та  бінарні
print(4)
print(-4)
print(-4 - 4)
print(+2)
print(+2 + 2)
print(2 + 3 *5)#25  ..17

print(5 + 2.6)#7.6
#print(5 + "hello")#error   5hello
print(5 + False)#False = 0  5   error
print(5 + True)#6 True = 1
print(1_000_000)

# Змінна - ділянка пам*яті певного розміру, яка може
# зберігати інформацію певного типу даних 

number = 10
age = 15
AGE = 15
pi = 3.14
ageHuman = 65
age_human = 25
a = 1
a1 = 2
a2 = 3
# 3a = 4  #error
# 4a = 5 #error
_number = 4
#def = 7   #error
print("ageHuman")
print(ageHuman)
print("ageHuman", ageHuman)
print(f"Age of human : {ageHuman}")

first_number = 10
second_number = 22
result = first_number + second_number
print(result)
print("Result = ", result)
print(f"Result : {first_number} + {second_number} = {result }")

#конкантенація   --- оператор + для рядочків
line1 = "Hyper"
line2 = "Text"
line3 = "Markup"
line4 = "Language"
allLine = line1 + " " + line2 + " "+ line3+ " " + line4
print(allLine)
print("hello"*5)
print("="*30)
print(allLine*4)
#input ---> str
a = int(input("Enter first number : ")) 
b = float(input("Enter second number : ")) 
res = a + b
print(f"Result : {a} + {b} = {res}")