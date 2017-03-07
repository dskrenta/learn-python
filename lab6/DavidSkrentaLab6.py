'''
CIS 117 Python Programing: Lab 6
David Skrenta
'''

def get_data(filename):
    data_file = open(filename, encoding='utf-8')
    data = data_file.read().split('\n')[:-1]
    return data

def is_valid(line):
    return line.isalpha() or line.isdigit() or '_' in line

def main():
    results = {}
    data = get_data('t6.py')
    for item in data:
        if is_valid(item):
            if item in results:
                results[str(item)] = [data.index(item)]
            else:
                results[str(item)].append(data.index(item))
    print(results)


main()

'''
'''
