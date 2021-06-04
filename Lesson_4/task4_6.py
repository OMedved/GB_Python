from itertools import count, cycle

for val in count(x := int(input("Введите стартовое число: "))):
   print(val)
   if val > x + 1:
       break

id_count = 0
for val in cycle(input("Введите трёхзначный код с обратной стороны банковской карты: ")):
    print(val)
    id_count += 1
    if id_count == 30:
        break