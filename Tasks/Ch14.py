import os
'''cd = os.getcwd()
print(cd)
file = open('output.txt')
fout = open('output.txt','w')
line1 = "This here's the wattle,\n"
print(len(line1))
print(fout.write(line1))
print(os.path.isdir('C:\\Users\\Алтынбек\\Desktop\\Python'))
print(os.path.isfile('NEWS.txt'))
print(os.listdir(cd))
'''

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path): print(path)
        else: walk(path)

def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        print('*',root,'<->', dirs, '<->', files)
        for filename in files: print(os.path.join(root, filename))

def form(filename):
    t = input('Тегі (Фамилия): ')
    a = input('Аты: ')
    print('Факультеті:')
    f1 = '1 - Экономика жəне əкімшілік-басқару ғылымдары'
    f2 = '2 - Филология жəне педагогикалық ғылымдар'
    f3 = '3 - Заң жəне əлеуметтік-гуманитарлық ғылымдары'
    f4 = '4 - Инженерлік жəне жаратылыстану ғылымдары'
    print(f1 + '\n' + f2 + '\n' + f3 + '\n' + f4)
    f = int(input())
    k = int(input('Курсы: '))
    newfile = t + '_' + filename
    file1 = open(newfile, 'w')
    for line in open(filename, encoding = 'utf-8'):
        if '[Text1]' and '[Text2]' in line:
            line = line.replace('[Text1]', t)
            line = line.replace('[Text2]', a)
            file1.write(line)
        elif '[Text3]' and '[Text4]' in line:
            line = line.replace('[Text3]', str(k))
            if f == 1: line = line.replace('[Text4]', f1.replace('1 - ', ''))
            elif f == 2: line = line.replace('[Text4]', f2.replace('2 - ', ''))
            elif f == 3: line = line.replace('[Text4]', f3.replace('3 - ', ''))
            elif f == 4: line = line.replace('[Text4]', f4.replace('4 - ', ''))
        print(line)

def file(filename):
    newfile = 'newfile_' + filename
    file = open(newfile, 'w')
    for line in open(filename):
        file.write(line)
