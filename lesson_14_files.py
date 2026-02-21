
# a = int(input("Enter number : "))
# print(a)

# open file
# read file
# write file
# close

#.txt
#.json

file = open("my_file.txt")
#print(file.read())
print(file.readlines())

file.close()

with open("my_file.txt") as file :
    print(file.readlines())# file.close()

#\n \t \' \'' \\
url = r"C:\Users\helen\Desktop\SPD_511\test.txt"
with open(url, 'a') as file:
    file.write('Hello friend')