import math
x = float(input('Введите значение х: '))
a = float(input('Введите значение а: '))
l = int(input('Введите сколько считать:'))
s = float(input('Введите шаг:'))
temp = float(input('Введите шаблон: '))
xlist = []
alist = []
glist = []
flist = []
ylist = []
gmass = []
fmass = []
ymass = []


for i in range(l):
    try:
        G = (9*(7*a**2-19*a*x+10*x**2))/(25*a**2+30*a*x+9*x**2)
        xlist.append(x)
        alist.append(a)
        glist.append(G)
        gmass.append((x,a,G))
    except ZeroDivisionError:
        G = ('ERROR')
        xlist.append(x)
        alist.append(a)
        glist.append(G)
        gmass.append((x,a,G))
    F = math.cos(9*a**2-13*a*x-10*x**2)
    xlist.append(x)
    alist.append(a)
    flist.append(F)
    fmass.append((x,a,F))
    try:
        Y = math.log(-80*a**2-46*a*x+21*x**2+1)/math.log(10)
        ylist.append(Y)
        xlist.append(x)
        alist.append(a)
        ylist.append(Y)
        ymass.append((x,a,Y))
    except ValueError:
            Y = ('ERROR')
    x += s
    a += s

w = int(input('1 - вывести функцию G, 2 - вывести функцию F, 3 - вывести функцию Y: '))
op = str(input('Способ вывода? (таблица/строка): '))
if op == 'строка':
    if w == 1:
        print(glist)
        print('Максимальное число: ' + str(max(glist)))
        print('Минимальное число: ' + str(min(glist)))
    if w == 2:
        print(flist)
        print('Максимальное число: ' + str(max(flist)))
        print('Минимальное число: ' + str(min(flist)))
    if w == 3:
        print(ylist)
        print('Максимальное число: ' + str(max(ylist)))
        print('Минимальное число: ' + str(min(ylist)))

elif op == 'таблица':
    q = 0
    if w == 1:
        for i in glist:
            print('a = {} x = {} G = {}'.format(str(alist[q]),str(xlist[q]),str(glist[q])))
            i += 1
            q += 1
    elif w == 2:
        for i in flist:
            print('a = {} x = {} F = {}'.format(str(alist[q]),str(xlist[q]),str(flist[q])))
            i += 1
            q += 1
    elif w == 3:
        for i in ylist:
            print('a = {} x = {} Y = {}'.format(str(alist[q]),str(xlist[q]),str(ylist[q])))
            i += 1
            q += 1
    else:
        print('ERROR')
if w == 1:
    print('Количество совпадений с шаблоном: ' + str(glist.count(temp)))
elif w == 2:
    print('Количество совпадений с шаблоном: ' + str(flist.count(temp)))
elif w == 3:
    print('Количество совпадений с шаблоном: ' + str(ylist.count(temp)))
else:
    print('ERROR')

File1=open('Факап1.txt','w')
for i in glist:
    File1.write(str(i) + '\n')
File1.close()
File2=open('Факап2.txt','w')
for i in flist:
    File2.write(str(i) + '\n')
File2.close()
File3=open('Факап3.txt','w')
for i in ylist:
    File3.write(str(i) + '\n')
File3.close()

filedata1 = open('Факап1.txt','r')
numbers1 = [line for line in filedata1.readlines()]
filedata1.close()
for i in numbers1:
    print(i)

filedata2 = open('Факап2.txt','r')
numbers2 = [line for line in filedata2.readlines()]
filedata2.close()
for i in numbers2:
    print(i)

filedata3 = open('Факап3.txt','r')
numbers3 = [line for line in filedata3.readlines()]
filedata3.close()
for i in numbers3:
    print(i)

