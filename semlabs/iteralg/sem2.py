import sys
print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
min = sys.float_info.max
for i  in range(a,b):
    if i < min:
        min = i
print(min)

