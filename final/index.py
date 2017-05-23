'''
CIS 117 Python Programing: Final Exam
David Skrenta
'''

'''
import re

p = re.compile('a.b.')

print(p.match('ab'))
print(p.match('acb'))
print(p.match('acbd'))
print(p.match('acbc'))
'''

'''
x = 5
y = 7
print(abs(x - y) - 10)
print(int(x**2) + 1.4)
print(round(y + 3.14159, 2))
'''

'''
list1 = [1,2,3]
list2 = [ ]
for element in list1 :
    list2.append(element)
list1 = [4,5,6]
print(list2)
'''

'''
K = ["Larry", "Curly", "Mo"]
print(type(K))
'''

'''
def main():
    individual = Cowboy()
    individual.sayGreeting()
    individual = Aussie()
    individual.sayGreeting()
class Person:
    def __init__(self, salutation = "Hello"):
        self._salutation = salutation
    def sayGreeting(self):
        print(self._salutation)
class Cowboy(Person):
    def __init__(self, salutation = "Howdy"):
        self._salutation = salutation
    def sayGreeting(self):
        print(self._salutation)
class Aussie(Person):
    def __init__(self, salutation = "G'day mate"):
        self._salutation = salutation
    def sayGreeting(self):
        print(self._salutation)
main()
'''

'''
x = 7
def main() :
    x = 5
    f()
    print(x)

def f() :
    print(x)

main()
'''

'''
x= 7
def main() :
    global x
    x = 5
    f()
    print(x)

def f() :
    print(x)

main()
'''

'''
def bestFilm(year, film, star):
    return 0

bestFilm()
'''

# print(range(6))
'''
for i in range(-11,-7):
    print(i)
'''

'''
NE = {'CT':3.6, 'ME':1.3, 'MA':6.5, 'NH':1.5, 'RI':1.1, 'VT':0.6}
# print(list(NE.values()))
print(list(NE.items()))
'''

'''
infile = open('UN.txt', 'r')
outfile = open('NewFile.txt', 'w')
for line in infile :
    data = line.split(',')
    outfile.write(data[0] + ' is in ' + data[1] + '.\n')
infile.close()
outfile.close()
'''

for num in range(4) :
    print(num)

print('\n')

for num in range (1,5) :
    print(num)
