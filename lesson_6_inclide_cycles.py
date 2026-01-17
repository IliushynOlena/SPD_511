# a = 6
# print(a)

# print(a + 5)

# number = int(input("Enter number : ")) 
# for n in range(1,11):
#     # 1 * 1 = 1
#     print(f"{number} * {n} = {number*n}")


# for i in range(1, 11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

# print("-------------------")

floor = 1
enegry  = 70

print(f"I'm on the {floor}")

#while floor < 9:
while floor != 9:
    step = 0

    if floor == 3:
        print("I will take an elevator")
        break

    while step != 20:
        step +=1
        enegry -=1
        if enegry == 0:
            print("I'm tired! I will rest a little!")
            enegry +=70
    floor +=1
    print(f"I'm on the {floor}")

print("I am at home")
