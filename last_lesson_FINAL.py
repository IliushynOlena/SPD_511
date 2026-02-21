import json

def createOneUser():
    id = int(input("Enter id --->"))
    name = input("Enter name --->")
    return {'id':id, 'name':name}
    

def createList(count):#count = 3
    users = []#0
    for i in range(count):
        u = createOneUser()
        users.append(u)
    return users

def printAll(users):
    print(users)

def writeToFile(users):
    with open("Users.json",'w') as file:
        file.write(json.dumps(users))

def readUserFromFile():
    with open("Users.json",'r') as file:
        return json.loads(file.read())
#flag = True
#while flag:

while True:
    choice = int(input('''
                1 - Fill Database
                2 - Show all users
                3 - Add user
                4 - Delete user
                5 -Sort user
                6 - Search user  
                0 - exit                     
            '''))
    if choice == 0:
        print("Goodbye!!! Have a nice day!")
        #flag = False
        break
    if choice == 1:
        count = int(input("Enter count users : "))
        users = createList(count)
        writeToFile(users)
    if choice == 2:
        users = readUserFromFile()
        printAll(users)
        users.sort(key = lambda u: u['name'])
        printAll(users)
    if choice == 3:
        pass
        # users = read all users
        # create new
        # add new to list
        # save to file
    if choice == 4:
        pass
        # users = read all users
        # seach element to delete index
        # delete element from list
        # save to file



