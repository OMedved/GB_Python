# Берём список [10, 20, 3, 410, 520, 63, 7410, 8520, 963, 0, 3, 23, 123, 63, 563, 4563, 963, 8963, 78963]
# Ожидаем получить [20, 410, 520, 7410, 8520, 3, 23, 123, 563, 4563, 8963, 78963]

start_list = [10, 20, 3, 410, 520, 63, 7410, 8520, 963, 0, 3, 23, 123, 63, 563, 4563, 963, 8963, 78963]
print([val for id, val in enumerate(start_list) if id != 0 and val > start_list[id - 1]])
