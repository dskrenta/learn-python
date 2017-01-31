'''
CIS 117 Python Programing: Lab 2
David Skrenta
'''


'''
expression1:             myId / 2

expression 2:            myId % 2

expression 3:            2 + 3 + … + nLet

expression 4:            myId + nLet

expression 5:            abs(nLet – myId)

expression 6:            (myId) / (nLet + 1100)

expression 7:            (nLet % nLet) and (myId * myId)

expression 8:            1 or (myId / 0)

expression 9:            round(3.14, 1)
'''

myId = sum([0, 1, 0, 3, 2, 5, 7, 5])
nLet = len("skrenta")

expression1 = myId / 2
expression2 = myId % 2
expression3 = sum(list(range(2, nLet)))
expression4 = myId = nLet
expression5 = abs(nLet - myId)
expression6 = (myId) / (nLet + 1100)
expression7 = (nLet % nLet) and (myId * myId)
expression8 = 1 or (myId / 0)
expression9 = round(3.14, 1)

print(myId)
print(nLet)

print(expression1)
print(expression2)
print(expression3)
print(expression4)
print(expression5)
print(expression6)
print(expression7)
print(expression8)
print(expression9)
