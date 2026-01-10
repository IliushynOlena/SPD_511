
# show hello 5 times
'''
i = 0 #лічильник

while i < 5:#лічильник має використовувати в умові
    print(f" {i}  - Hello")
    i+=1#зміна лічильника

print("---------------------------------")
i = 5
while i > 0:
    print(f" {i}  - Hello")
    i-=1

#show all number start = 5 ___ end = 20
i = 5
while i <= 20:
    print(i, end=" ")
    i+=1
print()
#show all number start = 10 ___ end = 0
i = 10
while i >= 0:
    print(i, end= " ")
    i-=1
print()

#show all number start  ___ end 
start =int(input("Enter start diapzon : ")) 
end = int(input("Enter end diapzon : "))

i = start
while i <= end:
    print(i, end=" ")
    i+=1
print()

#show all number start  ___ end 
start =int(input("Enter start diapzon : ")) #1
end = int(input("Enter end diapzon : "))#5


while start <= end:
    print(start, end=" ")
    start+=1
print()
print("---------------------show all number start  ___ 20-----------------------------------")

#show all number start  ___ 20
start =int(input("Enter start diapzon : ")) #1
if (start <= 20):
    while start <= 20:
        print(start, end=" ")
        start+=1
else:
    while start >= 20:
        print(start, end=" ")
        start-=1
print()
'''

#CTRL + F5 - швидкий запуск програми
# F9 -  поставити курсор на рядок та натиснути F9 - breakpoint (або ЛКМ перед номером рядка)
# F5 -  запуск програми через дебагер
# F10  або F11 -  рухаємось по рядочках

#користувач вводить число. Показати таблтцю множення на це число
number = int(input("Enter number : "))
if(number >=1 and number <=10):
    i = 1
    while i <= 10:
        print(F"{number} * {i} = {number*i}")
        i+=1
    else:
        print("="*35)
else:
    print("Number is incorrect")

#--------------- do while() ---------------цикл з післяумовою
# 1......5
i = 1
while True:
    print(i)
    i +=1
    if( i == 6):
        break

