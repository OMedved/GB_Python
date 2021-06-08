my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4.txt', 'r', encoding='utf-8') as source:
    with open('text_4_RU.txt', 'w', encoding='utf-8') as target:
        for line in source:
            en_word, *other_elements = line.split(' ')
            ru_word = my_dict[en_word]
            target.write(' '.join([ru_word] + other_elements) + '\n')