'''
CIS 117 Python Programing: Lab 11
David Skrenta
'''

import urllib.request

URL = 'http://www.nasonline.org'
TOPICS = [
    'research',
    'climate',
    'evolution',
    'cultural',
    'leadership',
    'integrity'
]


def main():
    html = str(urllib.request.urlopen(URL).read())
    for topic in TOPICS:
        print(topic + ' appears ' + str(html.count(topic)) + ' times.')

main()

'''
research appears 9 times.
climate appears 9 times.
evolution appears 3 times.
cultural appears 4 times.
leadership appears 2 times.
integrity appears 1 times.
'''
