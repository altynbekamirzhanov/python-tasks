def p1(word):
    for letter in word[::-1]:
        print(letter)
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

def find(word, letter):
    word = word.lower()
    print(word.find(letter))

def p8_1(word):
    n = word.capitalize()
    print(n)
    n = word.casefold()
    print(n)
    n = word.center(len(s)[ fillchar])
    print(n)
    n = word.count()
    print(n)
    n = word.encode(encoding='utf-8',errors='strict')
    print(n)
    
def p8_2():
    fruit = 'banana'
    print(fruit.count('a'))

def p8_3(word):
    if word == word[::-1]:
        return True
    return False

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False

def rotate_word(word, n):
    m = ''
    for letter in word:
        if ord(letter)+n<97:
            m = m + chr(ord(letter)+26+n)
        else:
            m = m + chr(ord(letter)+n)
    print(m)

def is_abecedarian(word):
    n = 1
    for letter in word:
        if chr(ord(letter)) > word[0+n]:
            return False
        n = n+1
        if n == len(word):
            break
    return True

def is_triple_double(word):
    n = 0
    index = 0
    while n < len(word)-1:
        if word[0+n] == word[1+n]:
            index += 1
            n += 2
        else:
            index = 0
            n += 1
        if index == 3:
                return True
    return False
