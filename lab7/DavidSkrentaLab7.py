'''
CIS 117 Python Programing: Lab 7
David Skrenta
'''

def is_valid(line):
    return line.isalpha() or line.isdigit() or '_' in line

def main():
    results = {}
    lines = 0
    with open('t6.py', encoding='utf-8') as data:
        for item in data:
            lines += 1
            item = item.rstrip()
            if is_valid(item):
                if item in results:
                    results[item].append(lines)
                else:
                    results[item] = [lines]
    for key in results.keys():
        print(key + ": " + str(results[key]))

main()

'''
stick: [20]
art: [5]
goodbye: [25]
ball: [4, 19]
orange: [15]
carrot: [13]
rat: [9]
4: [10]
dog: [6]
_: [22]
apple: [1, 11]
ant: [16, 17, 18]
pen: [8, 21]
1: [2, 3]
'''
