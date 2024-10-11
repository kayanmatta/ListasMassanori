n = input('Digite o seu nome de usuário: ')
s = input ('Digite a sua senha: ')
while n == s or s == n:
    print ('Erro, nome de usuário e senhas compativeis.Digite novamente!')
    n = input('Digite o seu nome de usuário: ')
    s = input ('Digite a sua senha: ')
print ('Login feito com sucesso!')    
