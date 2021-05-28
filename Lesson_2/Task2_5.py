team_height = [190, 186, 172, 168, 150]
border = (len(team_height) * int(-1))
while True:
    new_el = int(input('Введите рост нового члена команды в сантиметрах или 0 для выхода: '))
    n = -1
    if new_el == 0:
        print(team_height)
        break
    elif new_el > team_height[int(border)]:
        team_height.insert(0, new_el)
        border -= 1
        print(team_height)
    elif new_el <= team_height[int(n)]:
        team_height.append(new_el)
        border -= 1
        print(team_height)
    else:
        n -= 1
        while n >= border:
            if new_el <= team_height[n]:
                team_height.insert(n + 1, new_el)
                n = int(border) - int(1) - 1
                border -= 1
                print(team_height)
            else:
                n -= 1
print("Хорошего дня!")