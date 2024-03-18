'''
---Comparativos Bouleanos---

print(f'A comparação {n1} > {n2} dá {n1>n2}'
      f'\nA comparação {n1} < {n2} dá {n1<n2}'
      f'\nA comparação {n1} == {n2} dá {n1==n2}'
      f'\nA comparação {n1} >= {n2} dá {n1>=n2}'
      f'\nA comparação {n1} <= {n2} dá {n1<=n2}'
      f'\nA comparação {n1} != {n2} dá {n1!=n2}')
      n1 = 2

n2 = 3
n3 = 4
n4 = 5
print(f'A comparação {n1} > {n2} ou {n3} > {n4}, ou seja: {n1>n2} ou {n3>n4} dá {n1>n2 or n3>n4}'
      f'\nA comparação {n1} != {n2} ou {n3} < {n4}, ou seja: {n1!=n2} ou {n3<n4} dá {n1!=n2 or n3<n4}'
      f'\nA comparação {n1} > {n2} ou {n3} != {n4}, ou seja: {n1>n2} ou {n3!=n4} dá {n1>n2 or n3!=n4}'
      f'\nA comparação {n1} < {n2} ou {n3} > {n4}, ou seja: {n1<n2} ou {n3>n4} dá {n1<n2 or n3>n4}')
print('-'*100)
print(f'A comparação {n1} > {n2} e {n3} > {n4}, ou seja: {n1>n2} e {n3>n4} dá {n1>n2 and n3>n4}'
      f'\nA comparação {n1} != {n2} e {n3} < {n4}, ou seja: {n1!=n2} e {n3<n4} dá {n1!=n2 and n3<n4}'
      f'\nA comparação {n1} > {n2} e {n3} != {n4}, ou seja: {n1>n2} e {n3!=n4} dá {n1>n2 and n3!=n4}'
      f'\nA comparação {n1} < {n2} e {n3} > {n4}, ou seja: {n1<n2} e {n3>n4} dá {n1<n2 and n3>n4}')
 
---IF e ELSE / Condicionais---

a = str(input('Você é idoso?: '))
if a == 'sim' or a == 'Sim':
    print('Você pode estacionar!')
else:
    print('SAI DAQUI MENÓ')
 
letra = str(input('Digite uma letra: '))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('A sua letra é uma vogal')
else:
    print('A sua letra não é uma vogal')

letra = str(input('Digite uma letra: '))
if letra == 'a':
    print(f'A letra {letra} é uma vogal')
elif letra == 'e':
    print(f'A letra {letra} é uma vogal')
elif letra == 'i':
    print(f'A letra {letra} é uma vogal')
elif letra == 'o':
    print(f'A letra {letra} é uma vogal')
elif letra == 'u':
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} não é uma vogal')

salario = float(input('Diga seu salário: '))
if salario < 1903.98:
    ali = 0
elif salario <= 2826.65:
    ali = 0.075
elif salario <= 3751.05:
    ali = 0.15
elif salario <= 4664.68:
    ali = 0.225
else:
    ali = 0.275
print(f'Seu desconto é {salario*ali:.2f} e seu novo salário é: {salario - (salario*ali):.2f}')

---EXERCÍCIOS---
 
#1
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
if numero1 > numero2:
    print(f'O primeiro número: {numero1} é maior que o segundo número {numero2}')
else:
    print(f'O primeiro número: {numero1} é menor que o segundo número {numero2}')
 
#2
ano = int(input('Diga o ano em que você nasceu: '))
if (2024 - ano) > 16:
    print('Você já pode votar esse ano!')
else:
    print('Você não pode votar esse ano!')
 
#3
senha = str(input('Digite a sua senha: '))
if senha == '1234':
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')
 
#4
maca = int(input('Qual a quantidade de maçãs que você irá comprar? '))
if maca < 6:
    valortotal = maca * 0.30
elif maca >= 6:
    valortotal = maca * 0.25
print(f'O valor total da compra é R${valortotal}')
 
#5
--FORÇA BRUTA--
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1>n2 and n1>n3 and n2>n3:
    print(f'Os números em ordem crescente é: \n{n3} \n{n2} \n{n1}')
elif n1>n3 and n1>n2 and n3>n2:
    print(f'Os números em ordem crescente é: \n{n2} \n{n3} \n{n1}')
elif n2>n1 and n2>n3 and n1>n3:
    print(f'Os números em ordem crescente é: \n{n3} \n{n1} \n{n2}')
elif n2>n3 and n2>n1 and n3>n1:
    print(f'Os números em ordem crescente é: \n{n1} \n{n3} \n{n2}')
elif n3>n1 and n3>n2 and n1>n2:
    print(f'Os números em ordem crescente é: \n{n2} \n{n1} \n{n3}')
elif n3>n2 and n3>n1 and n2>n1:
    print(f'Os números em ordem crescente é: \n{n1} \n{n2} \n{n3}')

--MENOS FORÇA BRUTA #5--
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1>n2 and n1>n3:
    valorn3 = n3
    n3 = n1
    if valorn3>n2:
        print(f'A ordem crescente é: \n{n2} \n{valorn3} \n{n3}')
    else:
        print(f'A ordem crescente é: \n{valorn3} \n{n2} \n{n3}')
elif n2>n3:
    valorn3 = n3
    n3 = n2
    if valorn3>n1:
        print(f'A ordem crescente é: \n{n1} \n{valorn3} \n{n3}')
    else:
        print(f'A ordem crescente é: \n{valorn3} \n{n1} \n{n3}')

--CÓDIGO FINAL #5--
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1>n2 and n1>n3:
    vn3 = n3
    n3 = n1
    n1 = vn3
elif n2>n3:
    vn3 = n3
    n3 = n2
    n2 = vn3
if n1>n2:
    vn1 = n1
    n1 = n2
    n2 = vn1
print(f'A ordem crescente é: \n{n1} \n{n2} \n{n3}')

#6
altura = float(input('Digite sua altura: '))
genero = int(input('1 - Feminino  | 2 - Masculino \nEscolha seu gênero: '))
if genero == 1:
    formula = (62.1*altura) - 44.7
elif genero == 2:
    formula = (72.7 * altura) - 58
print(f'O seu peso ideal é {formula}')

#7 e #8
lados = int(input('Digite o número de lados do polígono: '))
tamanho = float(input('Digite o tamanho dos lados do polígono: '))
if lados < 3:
    print ('NÃO É UM POLÍGONO!')
elif lados == 3:
    perimetro = tamanho * 3
    print(f'TRIÂNGULO \nValor do perímetro: {perimetro}')
elif lados == 4:
    perimetro = tamanho * 4
    print(f'QUADRADO \nValor do perímetro: {perimetro}')
elif lados == 5:
    perimetro = tamanho * 5
    print(f'PENTÁGONO \nValor do perímetro: {perimetro}')
elif lados > 5:
    print ('POLÍGONO NÃO IDENTIFICADO!')

#9
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1>n2 and n1>n3:
    print(f'O maior valor é: {n1}')
elif n2>n3:
    print(f'O maior valor é: {n2}')
else:
    print(f'O maior valor é : {n3}')


#10
lado1 = int(input('Digite a medida do primeiro lado: '))
lado2 = int(input('Digite a medida do segundo lado: '))
lado3 = int(input('Digite a medida do terceiro lado: '))
if lado1==lado3 and lado2==lado1:
    print('Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print('Isósceles')
else:
    print('Escaleno')

#11
ang1 = int(input('Digite o primeiro ângulo: '))
ang2 = int(input('Digite o segundo ângulo: '))
ang3 = int(input('Digite o terceiro ângulo: '))
if ang1 == 90 or ang2 == 90 or ang3 ==90:
    print('Triângulo Retângulo')
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('Triângulo Obtusângulo')
else:
    print('Triângulo Acutângulo')

#EXTRA
radar = float(input('Qual era a velocidade do carro?: '))
if radar <= 100:
    print('Isento de multa')
elif radar <= 120:
    multa = radar*0.2
elif radar <= 150:
    multa = (120*0.2) + (radar*0.3)
else:
    multa = (120*0.2) + (150*0.3) + (radar*0.4)
print(f'A sua multa é de R${multa}')
'''
