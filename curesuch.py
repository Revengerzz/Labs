import time
import os
points = 100
clear = lambda: os.system('clear')
print('Правила:')
print('1. Отвечайте односложно и конкретно.')
print('2. Получайте удовольствие от игрового процесса.')
print('Удачи!')
time.sleep(2)
while True:
    ans = str(input('Хотите начать со вступления?(да/нет): '))
    if (ans == 'Да') or (ans == 'да'):
        print('-Капитан, как слышите?\n')
        time.sleep(2)
        print('-...\n')
        time.sleep(2)
        print('-Капитан, слышите меня?\n')
        time.sleep(2)
        print('-Гд.. Где я?\n')
        time.sleep(2)
        print('-Вы в осаждённом замке.\n')
        time.sleep(2)
        print('-Что это за место?\n')
        time.sleep(2)
        print('-У вас есть видеосигнал?\n')
        time.sleep(2)
        print('*Включился монитор.')
        time.sleep(2)
        print(' Вы видите женщину лет сорока в военной форме.* \n')
        time.sleep(2)
        clear()
        print('-Кто вы?..\n')
        time.sleep(2)
        print('-У вас уже есть эта информация.')
        time.sleep(2)
        print(' Назовите сначала своё имя.')
        time.sleep(2)
        name = str(input('Введите своё имя: '))
        print('-Теперь вспомните, как меня зовут.\n')
        time.sleep(2)
        print('-...\n')
        time.sleep(2)
        print('-Вспомните моё имя. *Она пододвинулась поближе к камере*\n')
        time.sleep(2)
        print('-Г.. Гудвин. Ваша фамилия Гудвин.\n')
        time.sleep(2)
        print('Г: Правильно. С возвращением, капитан ' + name + '! *Лёгкая улыбка скользнула по её лицу*')
        time.sleep(3)
        print(' Теперь я хочу объяснить вам, какова ваша миссия. \n')
        time.sleep(2)
        clear()
        print(' Сегодня в 8:27 на чикагском мосту произошёл взрыв двух проезжающих рядом поездов.\n')
        time.sleep(3)
        print(' Было выявлено, что взрыв произошёл из-за бомбы, заложенной в одном из вагонов.\n')
        time.sleep(3)
        print(' Для того, чтобы взорвать одновременно оба поезда, нужно было видеть, когда они проезжали рядом.\n')
        time.sleep(3)
        print(' Соответственно, преступник был во время взрыва либо в самом поезде, либо неподалёку.\n')
        time.sleep(3)
        print(' Сейчас вы окажетесь в компьютерной симуляции в теле одного из пассажиров поезда, в котором оказалась бомба.\n')
        time.sleep(3)
        print(' Будьте предельно внимательны, ваша задача найти преступника и сообщить нам всю необходимую информацию по нему.\n')
        time.sleep(3)
        print(' На это вам даётся 8 минут, не справляетесь - запускаем симуляцию снова.\n')
        time.sleep(2)
        clear()
        print(name[0] + ': Но... Как я здесь оказался?.. Где мой отряд... Я же был на зада..\n')
        time.sleep(2)
        print('Г: Начните с бомбы. Скажите, где она, как выглядит.\n')
        time.sleep(2)
        print(name[0] + ': Ладно, ладно.. Найти бом.. Нет, стойте..\n')
        time.sleep(1)
        clear()
        break
    elif (ans == 'Нет') or (ans == 'нет'):
        name = str(input('Введите своё имя: '))
        break
    else:
        print('Можно писать только "Да" или "Нет" ')
while True:
    print('-Шон, я сделала как ты сказал.')
    time.sleep(2)
    print(' Так что спасибо за совет!\n')
    time.sleep(2)
    print('-Да не за что..\n')
    time.sleep(1)
    print('-И я записалась на подготовительные в юридический.\n')
    time.sleep(2)
    print('Выберите действие:')
    while True:
        choice = str(input('Спросить насчёт пассажиров(1)    Выйти из купе(2)    Выйти вместе из поезда(3): '))
        if (choice == '1') or (choice == 'Спросить насчёт пассажиров') or (choice == 'спросить насчёт пассажиров'):
            print(name[0] + ': Хей, ты же ездишь на этом поезде каждый день? Можешь рассказать про всех пассажиров?\n')
            time.sleep(2)
            print('К: Странно, что ты это спрашиваешь, ты ведь видишь их чаще меня.. Но хорошо, я расскажу.\n')
            time.sleep(2)
            print('Майк - комик-любитель, занял третье место в Американских талантах. Два ареста за вождение в нетрезвом виде!\n')
            print('Хазми - иранский священник в мусульманской церкви. Появился около месяца назад, поэтому большего сказать не могу.\n')
            print('Дэниел - адвокат, с непривычной для его профессии импульсивностью. Сегодня явно не в духе.\n')
            print('Аврора - жена Дэниела, выезжает к парикмахеру каждый понедельник.\n')
            print('Стивен - молодой парень с ирокезом, неизменно сидит в своём ноутбуке, пока едет...\n')
            print('Найджел - обычный рабочий, сегодня всю поездку общается с кем-то по телефону.\n')
            print('Дерек - довольно умный и вежливый студент. Даже не знаю, что можно добавить.\n')
            print('Этот спящий великан - Рональд - довольно крупный парень, работает клерком в офисе и ненавидит свою работу.\n')
            time.sleep(5)
            print(' Поздравляю, вы потратили все 8 минут на разговоры с Кристиной! Надеюсь, это вам поможет! Поезд сделал BOOM.')
            break
        elif (choice == '2') or (choice == 'Выйти из купе') or (choice == 'выйти из купе'):
            print('Тут будет дохуя веток, я уже чувствую, как буду ебашить по клаве тапком')
            break
        elif (choice == '3') or (choice == 'Выйти вместе из поезда') or (choice == 'выйти вместе из поезда'):
            print(name[0] + ': Кристина, идём со мной!\n')
            time.sleep(2)
            print('К: Но это не наша остановка..\n')
            time.sleep(2)
            print(name[0] + ': Пойдём прогуляемся!\n')
            time.sleep(2)
            print('К: Нам не здесь выходить!\n')
            time.sleep(2)
            print(name[0] + ': Давай будем спонтанными!\n')
            time.sleep(2)
            print('К: Ты меня с ума свед...\n')
            time.sleep(2)
            print('*Вы резко пододвигаетесь и целуете её в губы\n')
            time.sleep(2)
            print(' После чего долго смотрите друг другу в глаза*\n')
            time.sleep(2)
            print(name[0] + ': Я знаю, что это звучит странно, но у меня очень дурное предчувствие.. Нам надо сойти с поезда.\n')
            time.sleep(2)
            print('*Вы выходите из поезда и идёте в близжайший кофе-бар.\n')
            time.sleep(2)
            print(' Всё идёт отлично, вам кажется, что вы нашли ту самую..\n')
            time.sleep(2)
            print(' Однако 8 минут истекли...*\n')
            time.sleep(2)
            clear()
            print('Г: Капитан ' + name + ', вы в порядке?\n')
            time.sleep(2)
            print(name[0] + ': Да, всё отлично! Я спас девушку, которая была со мной!\n')
            time.sleep(2)
            print(' Мы вместе вышли из поезда!\n')
            time.sleep(2)
            print('Г: ...\n')
            time.sleep(2)
            print(name[0] + ': Гудвин? Что-то не так?\n')
            time.sleep(2)
            print('Г: К сожалению, вы никого не спасли. Все, кто были в том поезде, уже умерли, и их жизни уже не вернуть.\n')
            time.sleep(2)
            print(' Симуляция, в которую мы вас отправляем, не имеет ничего общего с настоящим.\n')
            time.sleep(2)
            print(' Эта девушка выжила только в исходном коде.')
            time.sleep(2)
            print(name[0] + ': Что такое исходный код?')
            time.sleep(2)
            print('Г: Это квантовая механика, параболические исчисления.. Это очень сложно.\n')
            time.sleep(2)
            print(' У нас нет времени на объяснения, мы теряем драгоценные минуты.')
            time.sleep(2)
            break
        else:
            print('Напишите снова без ошибок')
    time.sleep(3)
    ans = str(input('Г: Капитан, вы поняли, кто является преступником?: '))
    if (ans == 'Да') or (ans == 'да'):
        ans = str(input('Г: Как зовут преступника?: '))
        if (ans == 'Дерек') or (ans == 'дерек'):
            ans = str(input('Г: Откуда он активировал детонатор?: из '))
            if (ans == 'фургона') or (ans == 'Фургона') or (ans == 'белого фургона') or (ans == 'Белого фургона'):
                ans = str(input('Г: Какой номер фургона?: '))
                if (ans == '194XGD') or (ans == '194xgd'):
                    ans = 1
    time.sleep(1)
    if ans == 1:
        print('Г: Спасибо за столь важную информацию! Вы оказали хорошую услугу своей стране!\n')
        time.sleep(3)
        print('Г: Преступник будет пойман в ближайшее время! Вы великолепны!\n')
        time.sleep(3)
        print('Ваши очки: ', points)
        break
    else:
        points -= 8
        print('Г: Недостаточно информации. Загружаем симуляцию снова.')
        time.sleep(2)
print('Тут будет эпилог')
