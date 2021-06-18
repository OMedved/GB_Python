class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def to_int(cls, date):
        str_list = date.split('-')
        day = int(str_list[0])
        mnth = int(str_list[1])
        year = int(str_list[2])
        return day, mnth, year

    @staticmethod
    def valid_date(day, mnth, year):
        if day == 31:
            if mnth == 4 or mnth == 6 or mnth == 9 or mnth == 11:
                print('Вэтом месяце не бывает 31 дня')
        elif day > 29 and mnth == 2:
            print('В феврале не бывает больше 29 дней')
        elif day < 0 or day > 31:
            print('Таких дней не бывает')
        elif mnth < 0 or mnth > 31:
            print('Таких месяцев не бывает')


user_date = input('Введите дату в формате дд-мм-гггг, разделяя значения дефисом: ')
Date.to_int(user_date)
print(user_date)
