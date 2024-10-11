import random 
nmenor = list ()
nmaior = list ()
for contador in range(0,10):
    x = random.randint(1,100)
    if contador == 0: 
      maior = x
      menor = x
    if x < menor:
      menor = x
    if x > maior:
      maior = x
nmaior.append (x)
nmenor.append (x)
print (f'O número maior é {nmaior}, e o menor é {nmenor}')

