import math
x = float(input('Введите значение х: '))
a = float(input('Введите значение а: '))
l = int(input("Введите сколько считать:"))
s = float(input("Введите шаг:"))
w = int(input('1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y: '))
if w == 1:
    for i in range(l):
        if (25*a**2+30*a*x+9*x**2) ==0:
            print('ERROR')
        else:
            G = (9*(7*a**2-19*a*x+10*x**2))/(25*a**2+30*a*x+9*x**2)
            print('G = ' + str(G))
            print()
            a += s
elif w == 2:
    for i in range(l):
        F == math.cos(9*a**2-13*a*x-10*x**2)
        if (math.cos(9*a**2-13*a*x-10*x**2) < -1) and (math.cos(9*a**2-13*a*x-10*x**2) > 1):
            print('ERROR')
        else:
            print('F = ' + str(F))
            print()
            a += s
    print('F = ' + str(math.cos(9*a**2-13*a*x-10*x**2)))
elif w == 3:
    print('Y = ' + str(math.log(-80*a**2-46*a*x+21*x**2+1)/math.log(10)))
    a += s
else:
    print('ERROR')
