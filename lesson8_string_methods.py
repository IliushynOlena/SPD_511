# print(chr(121))

# print(ord('y'))

# print(f"{chr(9556 )}{chr(9552 )*40}{chr(9559 )}")

string = "football"
print(string[0])
print(string[1])
print(f"Lenght : {len(string)}")
print(string[len(string)-1])
print(string[-1])
print(string[-3])

#конкантенація рядків  - додавання
str1 = "Hello, "
str2 = "word! "
print(str1 + str2)

res = str1 + str2
print(res)
print(str1)
print(str2)

#ДУБЛЮВАННЯ рядків   оператор *
myStr = "hello"
print(myStr*5)

myBigStr = myStr*6
print(myBigStr)

#len(object) - визначає довжинку рядка
print(f"Lenght myBigStr = {len(myBigStr)}")

#name text .... name text ... age ... name text ....
name = "Nazar"
age = 18

#formatLine = name + "text ....." + name + "text...." + age + name + "text...."//error
#formatLine = name , "text ....." ,name , "text...." , age, name , "text...."
#formatLine = "NAme: {}    text ..... {} text....AGe : {}  {} text....".format(name,name,age,name)
#formatLine = "NAme: {0}    text ..... {0} text....AGe : {1}  {0} text....".format(name,age)
formatLine = f"NAme: {name}    text ..... {name} text....AGe : {age}  {name} text...."
print(formatLine)

salary = 100.256564645
#strMsg = "Your salary is {0:9.2f}".format(salary)
strMsg = F"Your salary is {salary:20.1f}"
print(strMsg)

myStr1 = f"The temperature is in range from {-10:-} to {+10:+}"
print(myStr1)

point = 150
myStr2 = f"You have {point} points"
print(myStr2)

myStr2 = f"You have {point:25} points"
print(myStr2)

myStr2 = f"You have {point:<25} points"
print(myStr2)

myStr2 = f"You have {point:>25} points"
print(myStr2)

myStr2 = f"You have {point:^25} points"# (^) + Shift+6
print(myStr2)


myStr2 = f"You have {point:^25.2f} points"# (^) + Shift+6
print(myStr2)

#str - immuteable - набір незмінних символів
line ="some "
print(line)
print(id(line))
line = "hello"
print(line)
print(id(line))
line = "How are you today?"
print(line)
#line[0] = 'R' #c error
print(id(line))

# method string
# #       0 1 2 3 4 5 6 7 
# line = "s o m e t e x t"
# #       -8-7-6-5-4-3-2-1
line = "some text"
print(line)

#зріз рядків  line[start:end:step = +1]
print(line[0:5] + "|")
print(line[-4:-1] + "|")
print("|" + line[-4:5] + "|")

# str[:end]  --> start = 0, end = end : step = 1
print(line[:5])
print(line[:7])
print(line[:3])

# str[start:]  --> start = start, end = len(line): step = 1
print(line[5:])
print(line[7:])
print(line[0:])

#str[:]  start = 0 ,end = len step = 1
print(line[:])

#str[start:end:step]
print(line[0:5:2])
print(line[:7:3])
print(line[2::1])
print(line[::2])

number = "123456789"
letters = "abcdefg"
line="Lorem ipsum dolor sit emet"
word = "Fruit Apple"
word2 ="BANANA"
letterDigigt = "1225dddd555"

#перевіряє рядок на існування букв або чисел
print("============ isalnum() =======================")
print(f"\t{number:26} ----> {number.isalnum()}")
print(f"\t{letters:26} ----> {letters.isalnum()}")
print(f"\t{line:26} ----> {line.isalnum()}")
print(f"\t{word:26} ----> {word.isalnum()}")
print(f"\t{word2:26} ----> {word2.isalnum()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.isalnum()}")


#перевіряє рядок на існування тільки букви
print("============ isalpha() =======================")
print(f"\t{number:26} ----> {number.isalpha()}")
print(f"\t{letters:26} ----> {letters.isalpha()}")
print(f"\t{line:26} ----> {line.isalpha()}")
print(f"\t{word:26} ----> {word.isalpha()}")
print(f"\t{word2:26} ----> {word2.isalpha()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.isalpha()}")

#перевіряє рядок на існування тільки цифри
print("============ isdigit() =======================")
print(f"\t{number:26} ----> {number.isdigit()}")
print(f"\t{letters:26} ----> {letters.isdigit()}")
print(f"\t{line:26} ----> {line.isdigit()}")
print(f"\t{word:26} ----> {word.isdigit()}")
print(f"\t{word2:26} ----> {word2.isdigit()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.isdigit()}")


#перевіряє рядок на існування тільки пробілів, табуляцій та переходів на новий рядок
print("============ isspace() =======================")
print(f"\t{number:26} ----> {number.isspace()}")
print(f"\t{letters:26} ----> {letters.isspace()}")
print(f"\t{line:26} ----> {line.isspace()}")
print(f"\t{word:26} ----> {word.isspace()}")
print(f"\t{word2:26} ----> {word2.isspace()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.isspace()}")

#перевіряє рядок на існування тільки малих букв
print("============ islower() =======================")
print(f"\t{number:26} ----> {number.islower()}")
print(f"\t{letters:26} ----> {letters.islower()}")
print(f"\t{line:26} ----> {line.islower()}")
print(f"\t{word:26} ----> {word.islower()}")
print(f"\t{word2:26} ----> {word2.islower()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.islower()}")

#перевіряє рядок на існування тільки великі букв
print("============ isupper() =======================")
print(f"\t{number:26} ----> {number.isupper()}")
print(f"\t{letters:26} ----> {letters.isupper()}")
print(f"\t{line:26} ----> {line.isupper()}")
print(f"\t{word:26} ----> {word.isupper()}")
print(f"\t{word2:26} ----> {word2.isupper()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.isupper()}")

#перевіряє рядок на існування перша буква кожного слова велика
print("============ istitle() =======================")
print(f"\t{number:26} ----> {number.istitle()}")
print(f"\t{letters:26} ----> {letters.istitle()}")
print(f"\t{line:26} ----> {line.istitle()}")
print(f"\t{word:26} ----> {word.istitle()}")
print(f"\t{word2:26} ----> {word2.istitle()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.istitle()}")


#перетворює всі літери на нижній регістр
print("============ lower() =======================")
print(f"\t{number:26} ----> {number.lower()}")
print(f"\t{letters:26} ----> {letters.lower()}")
print(f"\t{line:26} ----> {line.lower()}")
print(f"\t{word:26} ----> {word.lower()}")
print(f"\t{word2:26} ----> {word2.lower()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.lower()}")

#перетворює всі літери на верхній регістр
print("============ upper() =======================")
print(f"\t{number:26} ----> {number.upper()}")
print(f"\t{letters:26} ----> {letters.upper()}")
print(f"\t{line:26} ----> {line.upper()}")
print(f"\t{word:26} ----> {word.upper()}")
print(f"\t{word2:26} ----> {word2.upper()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.upper()}")


#перетворює першу літери речення на верхній регістр
print("============ capitalize() =======================")
print(f"\t{number:26} ----> {number.capitalize()}")
print(f"\t{letters:26} ----> {letters.capitalize()}")
print(f"\t{line:26} ----> {line.capitalize()}")
print(f"\t{word:26} ----> {word.capitalize()}")
print(f"\t{word2:26} ----> {word2.capitalize()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.capitalize()}")

#перетворює першу літери кожного слова на верхній регістр
print("============ title() =======================")
print(f"\t{number:26} ----> {number.title()}")
print(f"\t{letters:26} ----> {letters.title()}")
print(f"\t{line:26} ----> {line.title()}")
print(f"\t{word:26} ----> {word.title()}")
print(f"\t{word2:26} ----> {word2.title()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.title()}")

#змінює регістри навпаки великі на маленькі, маленькі на великі
print("============ swapcase() =======================")
print(f"\t{number:26} ----> {number.swapcase()}")
print(f"\t{letters:26} ----> {letters.swapcase()}")
print(f"\t{line:26} ----> {line.swapcase()}")
print(f"\t{word:26} ----> {word.swapcase()}")
print(f"\t{word2:26} ----> {word2.swapcase()}")
print(f"\t{letterDigigt:26} ----> {letterDigigt.swapcase()}")

line = "Lorem ipsum dolor sit emet dolor sit emet dolor sit emet dolor sit emet  dolor sit emet"

index = -1
while True:
    index = line.find("sit",index+ 1)
    if index == -1:
        break
    print(F"Find text in the line by index {index}")
    
# print(F"Find text in the line by index {line.find("sit",19)}")
# print(F"Find text in the line by index {line.find("sit",34)}")
# print(F"Find text in the line by index {line.find("sit",49)}")
# print(F"Find text in the line by index {line.find("sit",64)}")
print(F"Find text in the line by index {line.rfind("sit")}")
print(F"Find text in the line by index {line.index("sit")}")
print(F"Find text in the line by index {line.rindex("sit")}")
#print(F"Find text in the line by index {line.rindex("friend")}")
print( line.replace("sit", "SIT"))

line = "Python 2026"
print(line.center(30))
print(line.center(30,'-'))
print(line.center(5))

