def questionnaire(name, surname, birtyear, locality, email, phone):
    return f'Имя: {name}, Фамилия: {surname}, Год рождения: {birtyear}, Населённый пункт: {locality}, e-mail: {email},' \
           f' Телефон: {phone}'


a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("Введите год рождения: ")
d = input("Введите населённый пункт: ")
e = input("Введите e-mail: ")
f = input("Введите номер телефона: ")
print(questionnaire(a, b, c, d, e, f))

