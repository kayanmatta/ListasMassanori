n = int(input('Digite o número 1: '))
n2 = int(input('Digíte o número 2: '))

while n % n2 != 0:
    n, n2 = n2, n%n2
print (f'mdc = {n2}')
    