import random

geral = list ()
par = list ()
ímpar = list ()

for contador in range(0,20):
    x = random.randint(1,100)
    geral.append (x)
    if x % 2 == 0:
        par.append (x)
    else:
        ímpar.append(x)
print (f'A lista geral é {geral}')
print (f'A lista PAR gerada é {par}')
print (f'A lista Ímparr é {ímpar}')
    