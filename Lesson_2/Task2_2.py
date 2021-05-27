mess = list(input('Напечатайте что угодно любой длины: '))
print('было', mess)
bgst_ndx = len(mess)
if bgst_ndx % 2 == 0:
    mess[:bgst_ndx:2],mess[1:bgst_ndx:2] = mess[1:bgst_ndx:2],mess[:bgst_ndx:2]
else:
    mess[:bgst_ndx - 1:2], mess[1:bgst_ndx - 1:2] = mess[1:bgst_ndx - 1:2], mess[:bgst_ndx - 1:2]
print('стало', mess)