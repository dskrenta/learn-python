'''
CIS 117 Python Programing: Lab 13
David Skrenta
Please replace this lab with lab 12
'''

DATA_FILE = 'testabbrev.txt'
RUNS = 5

def main():
    times = 0
    abbrevMap = createMap()
    while(times < RUNS):
        key = input('Enter a message to be translated:\n')
        print('The translated text is:\n' + str(abbrevMap.get(key)) + '\n')
        times += 1

def createMap():
    abbrevMap = {}
    with open(DATA_FILE, encoding='utf-8') as data:
        for item in data:
            values = item.rstrip().split(':')
            abbrevMap[values[0]] = values[1]
    return abbrevMap

main()

'''
Enter a message to be translated:
ttyl
The translated text is:
talk to you later

Enter a message to be translated:
idk
The translated text is:
I don't know

Enter a message to be translated:
1ce
The translated text is:
once

Enter a message to be translated:
afk
The translated text is:
away from keyboard

Enter a message to be translated:
app
The translated text is:
application

'''
