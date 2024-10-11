n = int(input('digite o valor de n: '))

t1, t2 = 0, 1
t3 = 1

while t3 <= n-1:
    t1, t2 = t2, t1 + t2
    t3 = t3 + 1
print (t2)