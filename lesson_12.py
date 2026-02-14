#Functions
import random
def showMessage():
    print("Hello")



showMessage()
a = 0
def sayHelloByUser(user_name):
    a = 0
    print(f"Hello : {user_name}")
    print(a)

sayHelloByUser("Irina")
sayHelloByUser("Petro")
sayHelloByUser("Mukola")
# name = input("Enter name : ")
# sayHelloByUser(name)

def summa(a,b):
    #result = a+b
    #print(result)
    #return result
    return a+b
a = 5
b = 7
s = summa(a,b)
print(f"Res = {s}" )

def sub(a,b):
    return a-b

def multy(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return#break
    return a/b

def calculator(a,b,op):
    if op == '+':
        return summa(a,b)
    if op == '-':
        return sub(a,b)
    if op == '*':
        return multy(a,b)
    if op == '/':
        return div(a,b)

def getOperation(line):
    if line.find('+') != -1:
        return '+'
    if line.find('-') != -1:
        return '-'
    if line.find('*') != -1:
        return '*'
    if line.find('/') != -1:
        return '/'


expression = input("Enter expesion 2+2 ---> ")
op = getOperation(expression)

print(expression)
print(op)
print(expression.split(op))
# num1 = float(expression.split(op)[0])
# num2 = float(expression.split(op)[1])
# result = calculator(num1,num2,op)
# print(f"Result = {result}")

'''
#defalt value 
def Fill_List(count , min=1, max=10):
    return [random.randint(min,max+1) for i in range(count)]#clear all info
    

numbers = []
print(numbers)
numbers = Fill_List(10,5,20)
print(numbers)

numbers = Fill_List(10)
print(numbers)
numbers = Fill_List(10,5)
print(numbers)
numbers = Fill_List(10,5,50)
print(numbers)
'''
