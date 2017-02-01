'''
CIS 117 Python Programing: Lab 2
David Skrenta
'''

gid = input("Enter GID: ")
name = input("Enter family name: ")

print("My family name is " + name)
print("My Student ID is " + gid)

myId = sum(list(map(int, str(gid))))
nLet = len(name)

print("The value of myId is " + str(myId))
print("The number of characters in my last name is " + str(nLet))

expression1 = myId / 2
expression2 = myId % 2
expression3 = sum(list(range(2, nLet)))
expression4 = myId = nLet
expression5 = abs(nLet - myId)
expression6 = round((myId) / (nLet + 1100), 2)
expression7 = (nLet % nLet) and (myId * myId)
expression8 = 1 or (myId / 0)
expression9 = round(3.14, 1)

print(expression1)
print(expression2)
print(expression3)
print(expression4)
print(expression5)
print(expression6)
print(expression7)
print(expression8)
print(expression9)
