import random
import json
import io

# list1 = []#0

# count = int(input("Enter count numbers "))#5

# for i in range(count):#0 1 2 3 4 
#     list1.append(int(input("Enter number ")))

# print(list1)

# count_number = 0
# number = int(input("Enter some number "))
# for num in list1:
#     if number == num:
#         count_number+=1
# print(f"Number {number} is {count_number} ")

list = [1,2,3,4,5]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print()
for item in matrix:
    print(item)


for i in range(3):#0 1 2
    for j in range(3):#0 1 2
        print(matrix[i][j], end=" ")
    print()
print("------------------------------")

print(matrix[1][1])

new_matrix = [] #list
row = 3
col = 4

for i in range(row):#0 1 2
    numbers = []#0
    for j in range(col):
        numbers.append(random.randint(20,50))
    new_matrix.append(numbers)

print(new_matrix)

summa = 0
for i in range(row):
    for j in range(col):
        print(new_matrix[i][j], end=" ")
        summa += new_matrix[i][j]
    print()

print(f"Summa elements : {summa}")