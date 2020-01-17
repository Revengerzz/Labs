while True:
    ans = str(input('Хотите начать со вступления?(да/нет): '))
    if (ans == 'Да') or (ans == 'да'):
        print('Тут будет вступление\n')
        break
    elif (ans == 'Нет') or (ans == 'нет'):
        name = str(input('Введи своё имя: \n'))
        break
    else:
        print('Можно писать только "Да" или "Нет" ')
