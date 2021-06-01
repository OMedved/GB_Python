def small_latin(smth):
    bank = 'qazwsxedcrfvtgbyhnujmikolp'
    for el in smth:
        if bank.count(el) != 1:
            print('Нам подходят только маленькие латинские буквы')
            break
        else:
            continue
    return smth.title()


result_list = []
user_text = input('Введите слова маленькими латинскими буквами: ').split()
for el in user_text:
    our_text = small_latin(el)
    result_list.append(our_text)
to_string = " ".join(result_list)
print(to_string)