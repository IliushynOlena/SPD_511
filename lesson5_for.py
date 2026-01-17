line = "Lorem Ipsum is simply dummy.Lorem Ipsum is simply dummy."
print(line)
print(line[0])
print(line[1])
print(line[2])
#show all text

for letter in line:#smart pointer
    print(letter, end="")
print()
#show all text
i = 0
while i < 56:
    print(line[i], end=" ")
    i+=1

# show diapzon [start = 6:end = 10]
print("\n--------------show diapzon [start:end]-----------------------")
for letter in line[6:10]:
    print(letter, end="")
print()

# show diapzon [start = 0:end = end of line]
print("\n--------------show diapzon [start:  ]-----------------------")
for letter in line[6:]:
    print(letter, end="")
print()

# show diapzon [start = 0:end = 10]
print("\n--------------show diapzon [:end]-----------------------")
for letter in line[:10]:
    print(letter, end="")
print()

# show diapzon [start:end:step = 3]
print("\n--------------show diapzon [:end]-----------------------")
for letter in line[1:25:3]:
    print(letter, end="")
print()

#---------------------------- range() ------------------
# for i in 1,2,3,4,5,6,7,8,9,10:
#     print(i, end=" ")
for i in range(1,11):#start = 1, end = 11
    print(i, end=" ")
print()

for i in range(11):#start = 0, end = 11
    print(i, end=" ")
print()


for i in range(1, 20, 2):#start = 1, end = 20, step = 2
    print(i, end=" ")

#------------- break , continue-----------
# while True:
#     res = int(input(" 2 + 2 = ? "))
#     if(res == 4):
#         print("Congratulation....")
#         break
print()

# i = 0
# while i <= 10:
#     if(i%3==0):
#         print(i, end= " ")
#     i+=1
summa = 0   
i = 0
while i <= 10:
    i+=1
    summa+=i
    if( i%2==1):
        continue
    print(i, end= " ")

number = int(input("Enter number : "))#10    10/1 10/2 10/3 10/4 10/6

flag = True
for i in range(2, number//2+1):
    if number %i == 0:
        flag = False
 
if not flag:
    print("складене число")
else:
    print("prime number")
# counter = 0

# for i in range(1, number+1):
#     if number %i == 0:
#         counter+=1

# if counter > 2:
#     print("складене число")
# else:
#     print("prime number")

#Користувач вводить із клавіатури два числа. Потрібно порахувати 
# суму чисел у вказаному діапазоні, а також середньоарифметичне.
a = int(input("Enter a :"))#10  
b = int(input("Enter b :"))#55

count = 0
summa = 0
while a <= b:
    print(a) #0 + 10 +11 +12 + 13 ...20
    count+=1
    summa += a
    a+=1

print("Summa", summa)
print("Count", count)

s = 0
c = 0
for num in range(a,b+1):
    print(num)
    s += num
    c +=1
print("Summa", s)
print("Count", c)