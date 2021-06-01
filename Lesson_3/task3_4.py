def neg_ext(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Нужно положительное действительное число и целая отрицательная степень')
        return
    if x <= 0 or int(y) >= 0:
        print('Нужно положительное число и целая отрицательная степень')
        return
    return x ** y


while True:
    a = input('Введите положительное число, которое надо ввести в степень: ')
    b = input('Введите целую отрицательную степень: ')
    if neg_ext(a, b) == None:
        continue
    else:
        print(neg_ext(a, b))
        break