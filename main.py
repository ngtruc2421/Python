# print("Hello world")
# firstName = "truc"
# lastName = "tran"
# fullName = firstName + " " + lastName
# print("Hello " + fullName)
# print(type(fullName))
# age = 23.6
# age += 1
# print("My age is: " + str(age))
# print(age - 5)
# print(type(age))
import time

# human, person, people = True, True, False
# if human == True:
#     print("This is a human")
# print(len(fullName))
# print(fullName.find("o"))
# print(fullName.islower())
# print(fullName.replace("t", "i"))
# b = "1"
# b = float(b)
# print(float(b))
# print(type(b))

#
# name: str = input("what is your name: ")
# print("Wellcome " + name)
# age: int(input("How old are you: "))
# print(name + str(age))

# import math
# a = -23.6
# b = 4
# c = 25
# print(math.ceil(a))
# print(round(a))
# print(abs(a))
# print(pow(a,2))
# print(math.floor(a))
# print(min(a,b,c))
# print(max(a,b,c))

# slicing
# name = "tran phuong ngoc truc"
# first_name = name[17:22]
# last_name = name[11:]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(reversed_name)

# slice()
# website = "https://google.com"
# protocol = website[slice(0, 5)]
# spe = website[slice(5, 8)]
# print(protocol)
# print(spe)

# if statement
# height = float(input("How old your height: "))
# if height == 100:
#     print("Vai ò")
# elif height > 120:
#     print("Qua du")
# elif height > 150:
#     print("So dep")
# else:
#     print("so bad")

# logical operators
# temp = int(input("number: "))
# if not(temp>=0 and temp<=5):
#     print("temp is 0 => 5 ")
# elif not(temp<0 or temp>5):
#     print("hehehe")

# while loop
# name = None
# while not name:
#     name = input("Your name: ")
# print("Hello " + name)
# print("MENU")
# print("1.Your name:")
# print("2.Your number:")
# print("3.Your phone:")
# print("Choose from 1 to 3 or 4 for beak")
# choose = int(input("Your choose"))
# name = " "
# number = " "
# phone = " "
# while choose < 5:
#     if choose == 1:
#         name = input("Name: ")
#         choose = int(input("Your choose"))
#
#     elif choose == 2:
#         number = input("Number: ")
#         choose = int(input("Your choose"))
#
#     elif choose == 3:
#         phone = input("Phone: ")
#         choose = int(input("Your choose"))
#
# print("Hello " + name + "num: " + number + " phone: " + phone)

# for loop
for i in range(19):
    print(i)
for i in range(0,10,2):
    print(i)
for i in "ngoc truc":
    print(i)
for i in range(5,0,-1):
    print(i)
    time.sleep(2)
print("You had a job!!!")