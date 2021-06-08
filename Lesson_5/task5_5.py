with open('for_task5.txt', 'w', encoding='utf-8') as temp_create:
    temp_create.write(' '.join(str(id) for id in range(1, 5)))

with open('for_task5.txt', 'r', encoding='utf-8') as temp_read:
    number_list = [int(val) for val in temp_read.read().split(' ')]
    print(sum(number_list))
