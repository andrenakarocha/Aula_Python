"""
##Pares e Ímpares (While)

repeticoes = 0
pares = 0
while repeticoes < 5:
    num = int(input('Diga um número: '))
    if num%2==0:
        pares += 1
    repeticoes += 1
impares = 5 - pares
print(f'O número de pares foi {pares} e o número de ímpares foi {impares}')

##Testando senha com While

senha = input('Digite a senha: ')
while senha != '1234':
    print ('Senha incorreta!')
    senha = input('Digite a senha: ')
print('Senha correta!')

##Bloqueando o acesso com 3 senhas incorretas

senha = input('Digite a senha: ')
tentativas = 1
while senha != '1234' and tentativas < 3:
    print (f'Senha incorreta! Você tem mais {3-tentativas} tentativas!')
    senha = input('Digite a senha: ')
    tentativas += 1
if senha == '1234':
    print('Senha correta!')
else:
    print('Acesso Negado!')

#Soma de 10 números pedidos com while

quant_num = 0
soma = 0
while quant_num < 10:
    num = int(input('Digite um número: '))
    quant_num += 1
    soma += num
print(f'A soma de todos os números é {soma}')

#Soma de 10 até 1 com while

i = 11
soma = 0
while i > 0:
    i -= 1
    soma += i
    print(soma)

#Frase com 10 palavras com while

i = 0
frase = ''
while i < 10:
    pal = input('Digite uma palavra: ')
    i += 1
    frase += ' ' + pal
    print(frase)

i = 0
vogais = 0
consoantes = 0
while i < 10:
    letra = input('Digite uma letra: ')
    i += 1
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vogais += 1
    else:
        consoantes += 1
print(f"A quantidade de vogais é {vogais} e a quantidade de consoantes é {consoantes}")
"""
