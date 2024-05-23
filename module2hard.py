while 1 > 0:
    n = int(input('Введите необходимое число от 3 до 20 включительно: '))
    list_ = []
    if 20 >= n >= 3:
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                s = j + i
                if n % s == 0:
                    g = str(i) + str(j)
                    list_.append(g)
        result = ''.join(list_)
        print('Ваш пароль:  ', result)
        break
    else:
        print('Ошибка! Неправильное значение')
