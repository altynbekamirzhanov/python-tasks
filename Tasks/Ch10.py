from random import *
def most_used(word):
    t = []
    word = word.lower()
    for letter in word: t.append(word.count(letter))
    for letter in word:
        if max(t) == word.count(letter):
            print(letter)
            word = word.replace(letter, '')

def maxmin(a):
    t = []
    while len(a) != 1:
        if a[0] >= a[1]:
            t.append(a[1])
            del a[1]
        else:
            t.append(a[0])
            del a[0]
    print('max:', a[0])
    while len(t) != 1:
        if t[0] <= t[1]:
            del t[1]
        else:
            del t[0]
    print('min:', t[0])

def list_sum(a):
    n = 0
    for number in a:
        n = n + number
    print('Sum:', n)

def nested_sum(a):
    n = 0
    for i in a:
        for j in i:
            n = n + j
    print('Sum:', n)

def mixed_sum(a):
    n = 0
    for i in a:
        if isinstance(i, int): n = n + i
        else:
            for j in i: n = n + j
    print(n)

def cumsum(a):
    i = 0
    while len(a) - i != 1:
        i = i + 1
        a[i] = a[i] + a[i - 1]
    print(a)

def word_sort():
    a = input('Enter your words seperated by comma (no spaces) :\n')
    b, s = '',a.split(', ')
    b = ', '.join(sorted(s))
    print('Your words sorted out:', '\n' + b)

def is_anagram(a, b):
    if len(a) == len(b):
        for letter in a:
            if letter not in b: return False
        return True
    else: return False

def has_duplicates(a):
    for element in a:
        if a.count(element) >= 2:
            return True
    return False

def remove_duplicates(a):
    t = []
    for element in a:
        if element not in t:
            t.append(element)
    print(sorted(t))

def birthday():
    t = []
    for i in range(23): t.append(randint(1,365))
    for i in t:
        if t.count(i) >= 2: return i
    return False

def word_count1(filename):
    n = 0
    file = open(filename)
    for line in file:
        word = line.split()
        for letter in word:
            n += 1
    print(n)

def word_count2(file):
    n = 0
    file = open(file)
    for line in file:
        word = line.split()
        for letter in word:
            if '0' <= letter <= '9':
                word.remove(letter)
            else:
                n += 1
    print(n)
