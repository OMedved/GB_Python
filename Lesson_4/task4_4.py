start_list = [969, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 0]
opty_dict = {}
for val in start_list:
    if val in opty_dict:
        opty_dict[val] += 1
    else:
        opty_dict[val] = 1
result = [val for val in opty_dict if opty_dict[val] == 1]
print(result)