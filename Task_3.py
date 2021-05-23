n = input('Tell me The "N" Number!')
while n < '0':
    print ("I forgot to say: it must be positive. Try again.")
    n = input('Tell me The "N" Number!')
dn = int(n + n)
tn = int(n + n + n)
print(int(n) + int(dn) + int(tn))
