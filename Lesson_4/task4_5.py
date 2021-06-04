from functools import reduce

items = [id for id in range(100, 1001, 2)]
mult_all = reduce(lambda x, y: x * y, items)

print(mult_all)