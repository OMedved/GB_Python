print('Введите текст и нажмите Enter\nДва нажатия Enter подряд завершат работу программы.')
with open('for_task1.txt', 'w', encoding='utf-8') as temp_file:
    while True:
        line = input('вводить сюда: ')
        if not line:
            break
        temp_file.write(line + '\n')