import math
x = float(input('Введите значение х: '))
a = float(input('Введите значение а: '))
l = int(input("Введите сколько считать:"))
s = float(input("Введите шаг:"))
w = int(input('1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y: '))
xlist = []
alist = []
glist = []
flist = []
ylist = []
if w == 1:
    for i in range(l):
        if (25*a**2+30*a*x+9*x**2) == 0:
            print('ERROR')
        else:
            G = (9*(7*a**2-19*a*x+10*x**2))/(25*a**2+30*a*x+9*x**2)
            print('G = ' + str(G))
            xlist.append(x)
            alist.append(a)
            glist.append(G)
            a += s
            x += s
elif w == 2:
    for i in range(l):
        F == math.cos(9*a**2-13*a*x-10*x**2)
        if (math.cos(9*a**2-13*a*x-10*x**2) < -1) and (math.cos(9*a**2-13*a*x-10*x**2) > 1):
            print('ERROR')
        else:
            print('F = ' + str(F))
            xlist.append(x)
            alist.append(a)
            flist.append(F)
            x += s
            a += s
elif w == 3:
    for i in range(l):
        if (-80*a**2-46*a*x+21*x**2+1 <= 0):
            print('ERROR')
        else:
            Y = math.log(-80*a**2-46*a*x+21*x**2+1)/math.log(10)
            print('Y = ' + str(Y))
            ylist.append(Y)
            xlist.append(x)
            alist.append(a)
            x += s
            a += s
else:
    print('ERROR')

op = str(input('Способ вывода? (таблица/строка): '))

if op == 'строка':
    if w == 1:
        print(glist)
        print(max(glist))
        print(min(glist))
    if w == 2:
        print(flist)
        print(max(flist))
        print(min(flist))
    if w == 3:
        print(ylist)
        print(max(ylist))
        print(min(ylist))


elif op == 'таблица':
    q = 0
    if w == 1:
        for i in glist:
            print('a = {} x = {} G = {}'.format(str(alist[q]),str(xlist[q]),str(glist[q])))
            i += 1
            q += 1
    if w == 2:
        for i in flist:
            print('a = {} x = {} F = {}'.format(str(alist[q]),str(xlist[q]),str(flist[q])))
            i += 1
            q += 1
    if w == 3:
        for i in ylist:
            print('a = {} x = {} Y = {}'.format(str(alist[q]),str(xlist[q]),str(ylist[q])))

            i += 1
            q += 1

