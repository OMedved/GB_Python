mess = input("Напишите несколько слов о себе (не меньше двух): ").split(' ')
for pos, el in enumerate(mess, 1):
    print(f'{pos} {el[:10]}')