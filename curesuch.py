while True:
    ans = str(input('Хотите начать со вступления?(да/нет): '))
    print()
    if (ans == 'Да') or (ans == 'да'):
        print('Тут будет вступление')
        break
    elif (ans == 'Нет') or (ans == 'нет'):
        name = str(input('Введи своё имя: '))
        print()
        break
    else:
        print('Можно писать только "Да" или "Нет" ')
        print()
