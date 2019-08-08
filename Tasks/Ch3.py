def right_justify(s):
    print (" " * (70-len(s)) + s)
    while True:
        c = input()
        right_justify(c)

def do_twice(a):
    a()
    a()
def print_me():
    print('Altynbek')

def square():
    a=('+ ')
    b=('- ')
    c=('|'+' '*7+'|'+' '*7+'|')
    d=a+b*3+a+b*3+a
    f=c+'\n'+c+'\n'+c
    print(d)
    print(f)
def print_twice():
    square()
    square()
    a=('+ ')
    b=('- ')
    d=a+b*3+a+b*3+a
    print(d)
