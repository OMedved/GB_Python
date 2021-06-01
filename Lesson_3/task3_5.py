def total_sum():
    temp = 0
    while True:
        user_list = input('Введите суммируемые числа через пробел или q для выхода: ').lower().split()
        for el in user_list:
            if el == 'q':
                print(f'Сумма чисел, введённых до символа выхода равна {temp}')
                break
            else:
                temp += float(el)
        else:
            print(f'Сумма введённых чисел равна {temp}')
            continue
        break
    return float(temp)

total_sum()
