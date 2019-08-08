import string
from random import *

def book(filename, a):
    d, t, file = dict(), list(), open(filename)
    for line in file:
        line = line.replace('-',' ')
        for word in line.split():
            word = (word.strip(string.punctuation + string.whitespace)).lower()
            d[word] = d.get(word, 0) + 1
    for key, value in d.items(): t.append((value,key))
    t.sort()
    print('Total number of words:', sum(d.values()))
    print('Total number of different words:', len(d))
    print('10 most frequently used words:')
    for freq, word in t[::-1][:10]: print(word, freq, sep='\t')
    print('Words of book which are not in given list:')
    for word in sorted(d):
        if word not in a: print(word)

def guess_num():
    n = randint(0,100)
    while True:
        s = int(input('Guess a number: '))
        if n > s:
            if n - s <= 5: print('very hot')
            elif 5 < n - s <= 10: print('hot')
            elif 10 < n - s <= 20: print('warm')
            elif 20 < n - s <= 30: print('stable')
            elif 30 < n - s <= 40: print('cool')
            elif 40 < n - s <= 50: print('cold')
            else: print('very cold')
        elif n < s:
            if s - n <= 5: print('very hot')
            elif 5 < s - n <= 10: print('hot')
            elif 10 < s - n <= 20: print('warm')
            elif 20 < s - n <= 30: print('stable')
            elif 30 < s - n <= 40: print('cool')
            elif 40 < s - n <= 50: print('cold')
            else: print('very cold')
        else:
            print('Congratulations! You guessed it!')
            break

def histogram(s):
    d = dict()
    for c in s:
        if c not in d: d[c] = 1
        else: d[c] += 1
    return d

def probability(t):
    hist = histogram(t)
    m = sum(hist.values())
    for key in sorted(hist):
        n = hist[key]
        print(key + ':', n/m)
    print(hist.keys(),'\n',hist.values(),'\n',hist)

def count_type(*a):
    d = dict()
    for i in a:
        if type(i) not in d: d[type(i)] = 1
        else: d[type(i)] += 1
    for key in d: print(key, d[key])
