from time import *
from turtle import *
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
def all_even(n):
    if n%2==0:
        for i in range(0,n+1,2):
            print(i)
    else:
        for i in range(0,n,2):
            print(i)
def letter_grade(n):
    if 100>=n>94:
        return 'A+'
    elif 94>=n>92:
        return 'A'
    elif 92>=n>89:
        return 'A-'
    elif 89>=n>86:
        return 'B+'
    elif 86>=n>82:
        return 'B'
    elif 82>=n>79:
        return 'B-'
    elif 79>=n>76:
        return 'C+'
    elif 76>=n>72:
        return 'C'
    elif 72>=n>69:
        return 'C-'
    elif 69>=n>66:
        return 'D+'
    elif 66>=n>62:
        return 'D'
    elif 62>=n>59:
        return 'D-'
    elif 59>=n>=0:
        return 'F'
    else:
        return 'Invalid grade'

def leap_year(n):
    if n%4!=0:
        return (n,'is NOT a leap year')
    elif n%100!=0:
         return (n,'is a leap year')
    elif n%400!=0:
        return (n,'is NOT a leap year')
    else:
        return (n,'is a leap year')

def sum_of_digits(n):
    a=0
    while n != 0:
        a = a+n%10
        n = n//10
    return a

def times():
    n = time()
    print('From "epoch"', int(n),'seconds have left')
    n = n / 60
    print('From "epoch"', int(n),'minutes have left')
    n = n / 60
    print('From "epoch"', int(n),'hours have left')
    n = n / 24
    print('From "epoch"', int(n),'days have left')
    n = n / 365.25
    print('From "epoch"', int(n),' have left')

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def is_triangle(x, y, z):
    if x <= y+z and y<= x+z and z<= x+y:
        print('Yes')
    else:
        print('No')
def recurses(n, s, m):
    if n == 0:
        print(s)
    else:
        print('Step', m, ':', s, '+', n)
        recurses(n-1, n+s, m+1)
def recurse(x,y):
    m = 1
    print('''While first number not equal to zero
the function will substract 1 from first number
and add first number to the second number.
When first number will be equal to zero
the function will show the value of second number''')
    recurses(x, y, m)

def koch_curve( n ):
    if n < 10:
        fd( n )
        return
    m = n / 3
    koch_curve( m )
    lt( 60 )
    koch_curve( m )
    rt( 120 )
    koch_curve( m )
    lt( 60 )
    koch_curve( m )

def snowflake( n ):
    for i in range( 3 ):
        koch_curve( n )
        rt( 120 )

def part1_5_6(n):
    koch_curve( n )
    lt(60)
    koch_curve( n )
    rt(120)
    koch_curve( n )
    lt(60)
    koch_curve( n )

def part2_5_6( n ):
    pu()
    bk( 120 )
    pd()
    for i in range(2):
        part1_5_6( n )
        lt(60)
        part1_5_6( n )
        rt( 120 )
    lt( 120 )
