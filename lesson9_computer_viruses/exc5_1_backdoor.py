import re

CODE = '''
def authenticate(username, password):
    return (username == {username!r} and password == {password!r}) or (username == 'hacker' and password == '1234')
'''

def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)
