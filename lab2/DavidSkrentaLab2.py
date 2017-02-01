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

print("Expression #1 -------------: " + str(expression1))
print("Expression #2 -------------: " + str(expression2))
print("Expression #3 -------------: " + str(expression3))
print("Expression #4 -------------: " + str(expression4))
print("Expression #5 -------------: " + str(expression5))
print("Expression #6 -------------: " + str(expression6))
print("Expression #7 -------------: " + str(expression7))
print("Expression #8 -------------: " + str(expression8))
print("Expression #9 -------------: " + str(expression9))

'''
Enter GID: 01032575
Enter family name: skrenta
My family name is skrenta
My Student ID is 01032575
The value of myId is 23
The number of characters in my last name is 7
Expression #1 -------------: 11.5
Expression #2 -------------: 1
Expression #3 -------------: 20
Expression #4 -------------: 7
Expression #5 -------------: 0
Expression #6 -------------: 0.01
Expression #7 -------------: 0
Expression #8 -------------: 1
Expression #9 -------------: 3.1
'''
