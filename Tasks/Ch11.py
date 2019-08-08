import time
def kaz_eng():
    print('Welcome to Kaz-Eng Dictionary!')
    d = dict()
    d = {'алма': 'apple', 'алмурт': 'pear', 'кулпынай': 'strawberry', 'ананас': 'pineapple', 'сабиз': 'сarrot', 'кызанак': 'tomato', 'карбыз': 'watermelon', 'кауын': 'melon', 'кырыккабат': 'cabbage', 'кияр': 'cucumber', 'пияз': 'onion'}
    while True:
        print('=====================================')
        print('Choose one:')
        print('1 - Search')
        print('2 - Add')
        print('3 - List')
        print('4 - Exit')
        print('--------------------')
        n = input('Number of option: ')
        if n == '1':
            n = input('Search: ')
            if n in d:
                print( d[n] )
            else:
                raise LookupError('No such word in the dictionary')
                print('Your word didn`t find')
        elif n == '2':
            n = input('Enter a word (Kaz): ')
            m = input('Enter a translation: ')
            d[n] = m
        elif n == '3':
            for a in d:
                print(a + ' '*(10-len(a)), d[a])
        elif n == '4':
            print('Goodbye!')
            break

def most_used(word):
    word = word.lower()
    c = ''
    d = dict()
    for letter in word:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
        c = c + str(d[letter])
    for letter in d:
        if max(c) == str(d[letter]):
            return letter

def fibonacci_time(n):
    known = {0: 0, 1: 1}
    def recurse_fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recurse_fib(n-1) + recurse_fib(n-2)
    def dict_fib(n):
        if n in known:
            return known[n]
        res = dict_fib(n-1) + dict_fib(n-2)
        known[n] = res
        return res
    s = time.clock()
    print(recurse_fib(n), time.clock() - s)
    print(dict_fib(n), time.clock() - s)
    
def grading():
    n, m = 0, 0
    python_grading = dict()
    math_grading = dict()
    c = ['Quiz-1', 'Quiz-2', 'Midterm exam', 'Tasks', 'Quiz-3', 'Quiz-4', 'Final exam']
    d = ['Midterm-1', 'Midterm-2', 'Final']
    print('Enter your marks for Python')
    for i in sorted(c):
        print(i)
        python_grading[i] = int(input())
        if i == 'Final exam' or i == 'Tasks':
            n = n + python_grading[i]*30
        elif i == 'Midterm exam':
            n = n + python_grading[i]*20
        else:
            n = n + python_grading[i]*5
    print('Enter your marks for Math')
    for i in sorted(d):
        print(i)
        math_grading[i] = int(input())
        if i == 'Midterm-1' or i == 'Midterm-2':
            m = m + math_grading[i]*30
        else:
            m = m + math_grading[i]*40
    print('Python:', n/100)
    print('Math:', m/100)
