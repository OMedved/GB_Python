class MyError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

first_number = input("Введите число, которое надо разделить: ")
second_number = input("Введите число, на которое будем делить: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    if second_number == 0:
        raise MyError("В нашей программе на 0 делить нельзя!")
except MyError as err:
    print(err)
else:
    print(f'Результат деления {first_number / second_number}')