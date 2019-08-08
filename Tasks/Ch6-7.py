from math import *
def sort(x,y,z):
    if x<=y<=z: print('Ordered:',x,y,z)            
    elif x<=z<=y: print('Ordered:',x,z,y)
    elif y<=x<=z: print('Ordered:',y,x,z)
    elif y<=z<=x: print('Ordered:',y,z,x)
    elif z<=x<=y: print('Ordered:',z,x,y)
    else: print('Ordered:',z,y,x)

def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

def power(x, y):
    n = -1
    z = y/x*x
    while z != 0:
        z = z // x
        n = n + 1
    if x**n == y:
        return True
    else:
        return False

def gcd(a, b):
    if isinstance(a and b, int):
        if a>b:
            while b != 0:
                a, b = b, a%b
            return a
        else:
            while a !=0:
                b, a = a, b%a
            return b
    else:
        print('Your input is wrong!')

def sqr_root():
    print('a   mysqrt(a)          math.sqrt(a)       diff')
    print('-   ---------          ------------       ----')
    for a in range(1, 10):
        x = 5
        while True:
            y = (x + a/x)/2
            if y == x:
                break
            x = y
        x= str(y)
        b = str(sqrt(a))
        print(float(a), x+' '*(18-len(x)), b+' '*(18-len(b)), fabs(float(x)-float(b)))

def eval_loop():
    word = str(input('Input smth: '))
    while word != 'done':
        n = eval(word)
        print(n)
        word = str(input('Input again: '))
    return 'Done!'


def pin():
    n=1234
    index=0
    m=int(input('Enter your PIN: '))
    while m!=n:
        index+=1
        if index>2:
            return 'Your card has been blocked'
        m=int(input('Enter your PIN again: '))
    return 'Correct!'

def total():
    n=int(input('Enter a number: '))
    total=0
    while n!=0:
        total=total+n
        n=int(input('Enter another number: '))
    print('Total:',total)

def divisibles(n):
    m = 0
    if isinstance(n, int):
        for i in range(1, n+1):
            if n%i == 0:
                m = m+1
        if m == 2:
            print(i,'\n')
    else:
        print('You wrote wrong!')

def prime():
    for j in range(1,101):
        divisibles(j)
