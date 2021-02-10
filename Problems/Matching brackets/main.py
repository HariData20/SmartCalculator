# put your python code here
import sys

expression = input()
stack_braces = []
for i in expression:
    if i == '(':
        stack_braces.append(i)
    elif i == ')' and len(stack_braces) != 0:
        stack_braces.pop()
    elif i == ')' and len(stack_braces) == 0:
        print('ERROR')
        sys.exit()
print('OK' if len(stack_braces) == 0 else 'ERROR')


'''
Alternate Solutions
stacc=[]
try:
    for char in input():
        if char == '(':
            stacc.append('(')
        elif char == ')':
            stacc.pop()
    print("OK" if not stacc else "ERROR")
except IndexError:
    print("ERROR")

'''