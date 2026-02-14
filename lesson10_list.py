mark1 = 10
mark2 = 12
mark3 = 1
mark4 = 6
#list 
marks = [12,10,3,4,5,6,11,2]

summa = 0
for i in marks:
    print(i)
    summa += i
    
print(marks)
print(marks[1])

for index in range(0, len(marks)):
    print(f"Mark [{index+1}] - {marks[index]}")

marks[7] = 12

for index in range(0, len(marks)):
    print(f"Mark [{index+1}] - {marks[index]}")
#масив - це набір однотипних комірок, які в пам*яті розташовані послідовно
#list - список, в якому комікрки розкидані
elements = ['1000',1,5,87,100,"hello", "green",True, [11,12,12,12]]
print(elements)

#1 - create list
category = ["Drama","Comedy","Fantasy"]
print(category)


#2 - create list
courses = list(("Math","Programming","Design"))
print(courses)

marks = [] #empty list
lines = list()#create empty list
print(marks)
print(lines)

mylist = [1,55,-96,"true",[22,"String"]]
print(mylist)

customers = ["Bob","Anna","Joe","Nick","Mira", "Bob","Nick"]
print(customers)

mysymbols = list("abcdefg")
print(mysymbols)

#генератори списків
#newList = [expression for item in sequence]

# for i in range(6) - sequence
#for i in range(6) ----> 0 1 2 3 4 5 

#expression - one element
for i in range(6):
    print(i, end=" ")
#...........
list1 = [i  for i in range(6)]
print(list1)

list1 = [i*i  for i in range(6)]
print(list1)

list1 = [i+10  for i in range(6)]
print(list1)

import random
#for i in range(10) 0 1 2 3 4 5 6 7 8 9
list1 = [ random.randint(20,50)  for i in range(10)]
print(list1)

#for i in "abcdefg" ----> a b c d e f g 
list1 = [ i + '*'  for i in "abcdefg"]
print(list1)

list1 = [ let  for let in "language"]
print(list1)

print("_".join(list1))

line = "23 15 yellow white orange black green yellow white orange black"

line_colors = line.split(" ")
print(line_colors)

for color in line_colors:
    print(color)

##newList = [expression for item in sequence if condition]
#if condition -  True False умова, коли елемент нам підходить

# for i in range(1, 11)    --> 1 2 3 4 5 6 7 8 9 10
list2 = [i*i    for i in range(1, 11) if i%2==1]
print(list2)

customers = ["Bob","Anna","Joe","Nick","Mira", "Bob","Nick"]
#for i in customers  --> "Bob","Anna","Joe","Nick","Mira", "Bob","Nick"
list3 = [  i   for i in customers if i != "Bob" and i !="Joe" ]
print(list3)

# for x in range(1,4):#1 2 3
#     for y in range(1,4):#1 2 3
#         print(x*y , end=" ")
#     print()
# print()

list4 = [x*y for x in range(1,4) for y in range(1,4)]
print(list4)

list5 = ["user",12, 200.34, False, True]
print(list5)
print(list5[0])
print(list5[4])
print(list5[len(list5)-1])#len(list5) - 5 
print(list5[-1])

#зріз рядків  line[start:end:step = +1]
print(list5[0:3])
print(list5[-4:-2])
print(list5[1:-1])
print(list5[::-1])
print(list5[-4::-1])

print(list5)
list5[-1] = 'Action'
print(list5)

#standart function len(), max(), min(), sum(), sorted()
userLogs = ["admin","user","student","teacher","hr"]

prices = [100,500,47,56,123]

print(f"Lenght users: {len(userLogs)}")
print(f"Lenght prices : {len(prices)}")
print(f"Max users : {max(userLogs)}")
print(f"Max price : {max(prices)}")
print(f"Min users: {min(userLogs)}")
print(f"Min prices: {min(prices)}")

#print(f"Summa users: {sum(userLogs)}") # error
print(f"Summa prices {sum(prices)}")
print(f"Sorted prices {sorted(prices)}")
print(f"Sorted users {sorted(userLogs)}")

category1 = ["Drama", "Comedy"]
category2 = ["Action", "Fiction"]
print(category1+category2)
res = category1+category2
print(res)

for elem in res:
    print(elem)

for index in range(len(res)):
    print(res[index])

# functions ....
print(res)

#add to the end new element
res.append("Fantasy")
print(res)

#add to the end many new elements
res.extend(category1)
res.extend(["Action", "Fiction"])
print(res)

#add element by position
res.insert(2,"Action")
print(res)
res.insert(-1,"Romance")
print(res)

#remove element by value
res.remove("Action")
print(res)

#remove element from the end
res.pop()
print(res)
res.pop()
print(res)
#remove element by index
res.pop(2)
print(res)

#delete all elements
# res.clear()
# print(res)

#find element
print(f"Find element in index : {res.index("Action")}")
print(f"Find element in index: {res.index("Fiction")}")
#print(f"Find element in index : {res.index("Movie")}") // error

print(f"Count elements by value : {res.count("Comedy")}")

#sort arr 
res.sort()
print(res)

#sort arr 
res.sort(reverse=True)
print(res)

res.reverse()
print(res)


customers = ["Bob","Anna","Joe","Nick","Mira", "Bob","Nick"]
for i in customers:
    if i == "Mira":
        print("Mira is in list")

# in
print("Mira" in customers)
if "Mira" in customers:
    print("Mira is in list")
else:
    print("Mira is not in list")

list1 = [1,2,3,4,5]
print(list1)
#list2  = list1
list2 = list1.copy()
print(list2)

list2[0] = 1000
print(list1)
print(list2)

print(id(list1))
print(id(list2))