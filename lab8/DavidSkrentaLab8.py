'''
CIS 117 Python Programing: Lab 8
David Skrenta
'''

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.line = ''

    def append(self, line):
        self.line += line + '\n'

    def toString(self):
        return 'From: ' + self.sender + '\n' + 'To: ' \
        + self.recipient + '\n' + self.line

'''
From: Bob
To: Santa
For Christmas, I would like:
Video games
World peace
'''
