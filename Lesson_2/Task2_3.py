calendar_dict = dict([(1, 'winter'), (2, 'winter'), (3, 'spring'), (4, 'spring'), (5, 'spring'), (6, 'summer'),
                      (7, 'summer'), (8, 'summer'), (9, 'autumn'), (10, 'autumn'), (11, 'autumn'), (12, 'winter')])
calendar_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
                     'autumn', 'autumn', 'winter']
mnth_nmbr = int(input("Введите номер месяца: "))
if mnth_nmbr > 0 and mnth_nmbr < 13:
    print(calendar_dict.get(mnth_nmbr))
    print(calendar_list[mnth_nmbr - 1])
else:
    print("Пока не дожили мы до таких месяцев")