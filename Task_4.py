start_num = int(input('Input positive integer:'))
current_max = start_num % 10  #последняя (либо единственная) цифра автоматически максимум
while start_num // 10 > 0:
    if start_num // 10 % 10 > current_max: #сравниваем вторую с конца (если она есть) с последней и перезаписываем
        current_max = start_num // 10 % 10
        start_num = start_num // 10
    else:
        current_max = current_max #либо не перезаписываем, и идём в начало цикла, отбросив последнюю цифру исходного числа
        start_num = start_num // 10
print('The maximum digit of your number is', current_max)
