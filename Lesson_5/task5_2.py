with open('for_task2.txt', 'r', encoding='utf-8') as temp_file:
    lines = 0
    words = 0
    for line in temp_file:
        lines += 1
        words = len(line.split(' '))
        print(f'В строке {lines} содержится {words} слов')
    print(f'Итого в файле содежится строк: {lines}')