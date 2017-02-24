'''
CIS 117 Python Programing: Lab 5
David Skrenta
'''

PASSWORD_LENGTH = 8

def password_valid(password1, password2):
    return password1 == password2 and \
           len(password1) >= PASSWORD_LENGTH and \
           any(char.islower() for char in password1) and \
           any(char.isupper() for char in password1) and \
           any(char.isdigit() for char in password1)

is_valid = False
while not is_valid:
    password1 = input("Enter your password: ")
    password2 = input("Re-enter your password: ")

    is_valid = password_valid(password1, password2)

    if is_valid:
        print("That pair of passwords will work.")
    else:
        print("That password didn't have the required properties.")

'''
Enter your password: 1234567A
Re-enter your password: 1234567A
That password didn't have the required properties.
Enter your password: aaaaaaaA
Re-enter your password: aaaaaaaA
That password didn't have the required properties.
Enter your password: Ab1
Re-enter your password: Ab1
That password didn't have the required properties.
Enter your password: AAAAAAA1
Re-enter your password: AAAAAAA1
That password didn't have the required properties.
Enter your password: Ilikebears89
Re-enter your password: Ilikebears89
That pair of passwords will work.
'''
