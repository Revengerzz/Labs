import math
a = int(input())
x = int(input())
w = int(input())
if w == 1:
    print('G = ' + str(9*(7*a**2-19*a*x+10*x**2)/(25*a**2+30*a*x+9*x**2)))
elif w == 2:
    print('F = ' + str(math.cos(9*a**2-13*a*x-10*x**2)))
else:
    print('Y = ' + str(math.log(-80*a**2-46*a*x+21*x**2+1)/math.log(10)))

