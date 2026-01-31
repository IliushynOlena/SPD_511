# message = "madam"
# reversed = message[::-1]
# # print(message[6])
# # print(message[5])
# # print(message[4])
# # print(message[3])
# # print(message[2])
# # print(message[1])
# # print(message[0])


# reversed = ""#eemadam
# for i in range(len(message)-1, -1, -1):
#     reversed += message[i]

# if message== reversed:
#     print("palindrome")
# else:
#     print("not palindrome")
    

# # print(message)
# # print(reversed)
# # for i in range(1,10):
# #     print(i)

#Regular expression - regex - детальну перевірку тго, що ввів користувач
#ми маємо вказати шаблон введеного рядка

name = "a"
phone = "+3809655jsdjsdg5445"

import re

line1 = "123"
line2 = "234"
line3 = "Lorem ipsum 21 dolor sit emet some text for the test"

print("============== re.search(template, line)")
print(f"{line1} ----> {re.search('12', line1)}")
print(f"{line2} ----> {re.search('12', line2)}")
print(f"{line3} ----> {re.search('12', line3)}")

print("============== re.search(template, line)   operator [symbols]")
print(f"{line1} ----> {re.search('[12]', line1)}")
print(f"{line2} ----> {re.search('[12]', line2)}")
print(f"{line3} ----> {re.search('[12]', line3)}")


print("============== re.search(template, line)   operator [0-9]")
print(f"{line1} ----> {re.search('[0-9]', line1)}")
print(f"{line2} ----> {re.search('[0-9]', line2)}")
print(f"{line3} ----> {re.search('[0-9]', line3)}")

print("============== re.search(template, line)   operator [a-z]")
print(f"{line1} ----> {re.search('[a-z]', line1)}")
print(f"{line2} ----> {re.search('[a-z]', line2)}")
print(f"{line3} ----> {re.search('[a-z]', line3)}")

# message = input("Enter message : ")
# match = re.search('[A-Za-z0-9]',message)
# if match:
#     print("Find some letter ....")
# else:
#     print("Not found letter")


print("============== re.search(template, line)   operator [a-z]{start, end}")
print(f"{line1} ----> {re.search('[a-zA-Z]{5}', line1)}")
print(f"{line2} ----> {re.search('[a-zA-Z]{5}', line2)}")
print(f"{line3} ----> {re.search('[a-zA-Z]{5,6}', line3)}")

print("============== re.search(template, line)   operator [a-z]{start, end}")
print(f"{line1} ----> {re.search('[a-zA-Z]+', line1)}")
print(f"{line2} ----> {re.search('[a-zA-Z]+', line2)}")
print(f"{line3} ----> {re.search('[a-zA-Z]+', line3)}")

print("============== re.search(template, line)   operator [a-z]{start, end}")
print(f"{line3} ----> {re.search('[a-zA-Z]+', line3).group(0)}")

print("============== re.findall(template, line)   operator [a-z]{start, end}")
print(f"{line3} ----> {re.findall('[a-zA-Z]+', line3)}")
print(f"{line3} ----> {re.findall('[a-zA-Z]+', line3)[0]}")
print(f"{line3} ----> {re.findall('[a-zA-Z]+', line3)[1]}")
print(f"{line3} ----> {re.findall('[a-zA-Z]+', line3)[2]}")

match = re.findall('[a-zA-Z]+', line3)
for item in match:
    print(item)
print(line3)
res = re.sub('\w+',"white",line3)
print(res)

#\+380\d{9}
pattern = "^\+38\(0\d{2}\)\d{3}\-\d{2}\-\d{2}$|^\+380\d{9}$"
phone = input("Enter number : ")
match = re.search(pattern,phone)
#match = Match.group()  ---- > None
if match:
    #print(f"Phone is good {match.group(0)}")
    #group()   group(0) - повертає підрядок, який підлягає шаблону
    print(f"Phone is good {match.group()}")
else:
    print("Phone is incorect")
