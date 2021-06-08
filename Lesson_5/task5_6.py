target_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as source:
    clear_temp = []
    for line in source:
        subj, temp = line.split(':')
        for el in temp:
            if el in '0123465789' or el == ' ':
                clear_temp.append(el)
            elif el == '\n':
                hours_temp = ''.join(clear_temp).split()
                val_temp = sum(int(el) for el in hours_temp)
                target_dict[subj] = val_temp
                clear_temp = []
            else:
                continue
print(target_dict) #Не понимаю, почему последнюю строку не включает. Цикл обрывается на предпоследней сроке.
