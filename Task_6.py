first_dist = int(input("Сколько километров вы способны пробежать сейчас?"))
target_dist = int(input("Сколько километров вы хотите пробегать после нашей программы тренировок?"))
day_quant = 1
if target_dist <= first_dist:
    print("Вы уже способны на это")
else:
    while first_dist * 1.1 < target_dist:
        day_quant = day_quant + 1
        first_dist = first_dist * 1.1
    print(f'Вы достигнете результата {target_dist} км на {day_quant + 1}-й день.')
