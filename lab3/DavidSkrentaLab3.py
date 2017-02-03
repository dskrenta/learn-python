'''
CIS 117 Python Programing: Lab 3
David Skrenta
'''

months = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "November", "December"]

dateString = input("Enter a date (mm/dd/yyyy): ")
date = dateString.split('/')
monthIndex = int(date[0].strip('0')) - 1

print("The converted date is: " + months[monthIndex] + " " + date[1] + ", " + date[2])
