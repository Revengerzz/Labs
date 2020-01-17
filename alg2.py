from random import randint
def insertion_sort(list): 
    for i in range(1, len(list)): 
        value = list[i]
        j = i - 1 
        while j >= 0: 
            if list[j] > value: 
                list[j + 1] = list[j] 
                list[j] = value 
                j -= 1 
            else: 
                break 
N = 20 
a = [ ] 
for i in range(N): 
    a.append(randint(1,99))  
insertion_sort(a) 
print(a)
a.insert(4,27)
a.insert(9,24)
a.insert(13,8)
insertion_sort(a)
print(a)
