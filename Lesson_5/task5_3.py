with open('text_3.txt', 'r', encoding='utf-8') as temp_file:
    count = 0
    unhappy_employees = []
    income_sum = 0
    for line in temp_file:
        count += 1
        employee, income = (el for el in line.split(' '))
        income = float(income)
        income_sum += income
        if income < 20000:
            unhappy_employees.append(employee)
    average_inc = income_sum / count
print(f'Следующие сотрудники получают менее 20000 евро в год:\n{unhappy_employees}.\nСредний оклад сотрудников компании'
      f' составляет {average_inc} евро в год')
