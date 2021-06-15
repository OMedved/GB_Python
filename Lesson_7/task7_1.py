class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        new_matrix = ''
        for i in self.lists:
            a = '\t\t'.join(map(str, i)) + '\n'
            new_matrix = new_matrix + a
        return new_matrix

    def __add__(self, other):
        temp = []
        for line in range(len(self.lists)):
            temp.append([])
            for val in range(len(self.lists[line])):
                temp[line].append(int(self.lists[line][val]) + int(other.lists[line][val]))
        return Matrix(temp)

start_mtrx1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 2, 1], [6, 5, 4], [9, 8, 7]]
start_mtrx2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7], [3, 2, 1], [6, 5, 4], [9, 8, 7]]
start_mtrx5 = [[9, 9, 9], [9, 9, 94], [-99, 98, 97], [-93, 92, 91], [96, 95, 94], [-99, 98, 0]]

# print(mtrx3)
mtrx1 = Matrix(start_mtrx1)
# print(mtrx1)
mtrx2 = Matrix(start_mtrx2)
# print(mtrx2)
target_mtrx = mtrx1 + mtrx2
print(target_mtrx)
mtrx5 = Matrix(start_mtrx5)
three_mtrx = mtrx1 + mtrx2 + mtrx5
print(three_mtrx)
