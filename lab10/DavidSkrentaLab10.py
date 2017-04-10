'''
CIS 117 Python Programing: Lab 10
David Skrenta
'''

VOWELS = ['a', 'e', 'i', 'o', 'u']

def middle(string):
    stringList = list(string)
    middleIndex = round((len(stringList) - 1) / 2)
    return stringList[middleIndex]

def countVowels(string):
    times = 0
    for vowel in VOWELS:
        times += string.count(vowel)
    return times

def reverse(string):
    return string[::-1]

def isPalindrome(string):
    return reverse(string) == string

def main():
    times = 0
    while times < 5:
        string = input('Enter a string: ')
        print('The middle character(s) is/are: ' +  middle(string))
        print('The string reversed is: ' + reverse(string))
        print('The string contains ' + str(countVowels(string)) + ' vowels.')
        if isPalindrome(string):
            print('That\'s a palindrome.\n')
        else:
            print('That\'s not palindrome.\n')
        times += 1

main()

'''
Enter a string: racecar
The middle character(s) is/are: e
The string reversed is: racecar
The string contains 3 vowels.
That's a palindrome.

Enter a string: apple
The middle character(s) is/are: p
The string reversed is: elppa
The string contains 2 vowels.
That's not palindrome.

Enter a string: civic
The middle character(s) is/are: v
The string reversed is: civic
The string contains 2 vowels.
That's a palindrome.

Enter a string: bottle
The middle character(s) is/are: t
The string reversed is: elttob
The string contains 2 vowels.
That's not palindrome.

Enter a string: noon
The middle character(s) is/are: o
The string reversed is: noon
The string contains 2 vowels.
That's a palindrome.
'''
