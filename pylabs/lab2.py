import math
print('Введите числа, не равные нулю')
x = int(input('Введите значение х: '))
a = int(input('Введите значение а: '))
w = int(input('1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y: '))
if w == 1:
    print('G = ' + str(9*(7*a**2-19*a*x+10*x**2)/(25*a**2+30*a*x+9*x**2)))
elif w == 2:
    print('F = ' + str(math.cos(9*a**2-13*a*x-10*x**2)))
elif w == 3:
    print('Y = ' + str(math.log(-80*a**2-46*a*x+21*x**2+1)/math.log(10)))
else:
    print('Всё плохо')
