mark1 = 10
mark2 = 12
mark3 = 1
mark4 = 6
#list 
marks = [12,10,3,4,5,6,11,2]
print(marks)
print(marks[1])

for index in range(0, len(marks)):
    print(f"Mark [{index+1}] - {marks[index]}")

marks[7] = 12

for index in range(0, len(marks)):
    print(f"Mark [{index+1}] - {marks[index]}")
#масив - це набір однотипних комірок, які в пам*яті розташовані послідовно
#list - список, в якому комікрки розкидані
elements = [1,5,87,100,"hello", "green",True, [11,12,12,12]]
print(elements)

category = ["Drama","Comedy","Fantasy"]
print(category)

courses = list(("Math","Programming","Design"))
print(courses)

marks = [] #empty list
lines = list()#empty list
print(marks)
print(lines)