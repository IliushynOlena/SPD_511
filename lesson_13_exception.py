
# try(спробувати) except(зловити) raise(кидає)
num1 = None
num2 = None

# while num1 == None or num2 == None:
#     try:
#         num1 = int(input("Enter number : ")) 
#         num2 = int(input("Enter number : ")) 
#         #print(num1/num2,num3)
   
#     except ValueError:
#         print("Value error")
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except Exception:
#         print("Unknow excepion")


# try:
#     age = int(input("Enter age : ")) #500  -5
#     if age < 0:
#         raise Exception("Age < 0. Error")
#     if age > 126:
#         raise Exception("Age > 126. Error")
# except ValueError:
#     print("Value error")
# except Exception as ex:
#     print(ex)
    

print("Continue.....")
print("Continue.....")
print("Continue.....")
print("Continue.....")
print("Continue.....")

colors = ['red','green','blue','yellow']
print(colors[2])

try:
    index  = int(input("Enter index : "))
    print(colors[index])
except ValueError:
    print("Value error")
except IndexError as e:
    print(e)
    print("Index must be in range 1....3 ")
except Exception as ex:
    print(ex)