cont = 0
for k in range(1067, 3628):
    if k % 2 == 0 and k % 7 == 0:
        cont += 1
print (f'A quantidade de números pares e divisores por 7 são {cont}')