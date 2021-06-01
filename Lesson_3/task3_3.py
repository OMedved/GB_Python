def max_2_of_3(a, b, c):
    my_list = [a, b, c]
    try:
        return sum(sorted([a, b, c])[1:])
    except TypeError:
        print("Тут не везде цифры")


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
print(max_2_of_3(x, y, z))
