def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('В данной версии вселенной сегодня на 0 делить нельзя')


a = input('Какое число надо разделить? Введите: ')
b = input('На какое число делим? Введите: ')
print(division(int(a), int(b)))