class MyError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


user_list = []
while True:
    a = input('Введите число для добавления, либо "stop": ')
    if a == 'stop':
        print(user_list)
        break
    try:
        if a.isnumeric() == False:
            raise MyError('У нас тут так не принято!')
    except MyError as err:
        print(err)
    else:
        user_list.append(a)

#как проверять на отрицательные и нецелые - осилить не смог. Гуглёж говорит,
# что такую проверку надо в отдельную функцию выносить и запускть её во время цикла.