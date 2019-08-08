from random import *
import calendar
def sorted_list():
    t = [('Serik', 18, 90), ('Almas', 19, 175), ('Abai', 17, 180), ('Almas', 18, 170), ('Berik', 17, 180), ('Serik', 18, 195)]
    for a, b, c in sorted(t): print(a, b, c)

def sumall(*t): print(sum(t))

def m_f(word):
    t = tuple(word.lower())
    d, c = dict(), list()
    for i in sorted(t): d[i] = t.count(i)
    for i in d: c = c + [(d[i], i)]
    for key, value in sorted(c)[::-1]: print(value, key)

def whatsapp(n):
    file = open('sms.txt')
    lto, lfrm, to, frm, dto, dfrm =[], [], [], [], dict(), dict()
    week, hour = dict(), dict()
    for line in file:
        word = line.split()
        if word[6] == str(n):
            if word[0] == 'To':
                if word[1] not in dto: dto[word[1]] = 1
                else: dto[word[1]] += 1
            elif word[0] == 'From':
                if word[1] not in dfrm: dfrm[word[1]] = 1
                else: dfrm[word[1]] += 1
            if word[2] not in week: week[word[2]] = 1
            else: week[word[2]] += 1
            if word[5][0:2] not in hour: hour[word[5][0:2]] = 1
            else: hour[word[5][0:2]] += 1
    for i in dto: lto = lto + [dto[i]]
    for i in dfrm: lfrm = lfrm + [dfrm[i]]
    for key in sorted(dto): to = to + [(dto[key], key)]
    for key in sorted(dfrm): frm = frm + [(dfrm[key], key)]
    for key, value in to:
        if max(lto) == key: print('To:', value)
    for key, value in frm:
        if max(lfrm) == key: print('From:',value)
    print('---------')
    for i in week: print(i, week[i])
    print('---------')
    for i in sorted(hour): print(i, hour[i])

def whats_app():
    file = open('sms.txt')
    lto, lfrm, to, frm, dto, dfrm =[], [], [], [], dict(), dict()
    week, hour = dict(), dict()
    for line in file:
        word = line.split()
        if word[0] == 'To':
            if word[1] not in dto: dto[word[1]] = 1
            else: dto[word[1]] += 1
        elif word[0] == 'From':
            if word[1] not in dfrm: dfrm[word[1]] = 1
            else: dfrm[word[1]] += 1
        if word[2] not in week: week[word[2]] = 1
        else: week[word[2]] += 1
        if word[5][0:2] not in hour: hour[word[5][0:2]] = 1
        else: hour[word[5][0:2]] += 1
    for i in dto: lto = lto + [dto[i]]
    for i in dfrm: lfrm = lfrm + [dfrm[i]]
    for key in sorted(dto): to = to + [(dto[key], key)]
    for key in sorted(dfrm): frm = frm + [(dfrm[key], key)]
    for key, value in to:
        if max(lto) == key: print('To:', value)
    for key, value in frm:
        if max(lfrm) == key: print('From:',value)
    print('---------')
    for i in week: print(i, week[i])
    print('---------')
    for i in sorted(hour): print(i, hour[i])

def average(year):
    file = open('sms.txt')
    
