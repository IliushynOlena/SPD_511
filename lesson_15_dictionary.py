#student
import json
name = "Oleg"
surname = "Ivanchuk"
spetialization = "programming"
course = 1
average_mark = 9.3
email = "oleg_ivanchuk@gmail.com"

#dictionary 
# key : value
#key - string type
#value - any type
student = {
    "name":"Oleg",
    "surname":"Ivanchuk",
    "spetialization":"programming",
    "course":1,
    "average_mark":9.3,
    "email":"oleg_ivanchuk@gmail.com",
    "marks": [11,12,5,7,8,9],
    #"address":"Rivne, Soborna 16a"
    "address ": {
        "city":"Rivne",
        "street":"Soborna",
        "building":"16a",
    }
}
print(student)
print(student["name"])
print(student["marks"])

#get all keys
for key in student.keys():
    print(f"Key : {key} . Value : {student[key]}")

for key in student.keys():
    print(f" {key} - {student[key]}")

#get all values
for value in student.values():
    print(f"\t {value}")

for key, value in student.items():
    print(f"{key} -- {value}")

print(student)
del student['address ']

print(student)

# #delete last key
# student.popitem()
# print(student)

student.pop("course")
print(student)


i = 1
for mark in student["marks"]:
    print(f"[{i}]- {mark}")
    i+=1

# with open("student.txt", 'w') as file:
#     file.write(str(student))

# with open("student.txt", 'r') as file:
#     print(file.read()["marks"])

with open("student.json", 'w') as file:
    file.write(json.dumps(student))

with open("student.json", 'r') as file:
    obj = file.read()
    print(json.loads(obj))
    print(json.loads(obj)["marks"])