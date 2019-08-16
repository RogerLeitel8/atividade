# nome = input('Digite o seu nome')
idade = int(input('Digite a sua idade'))
saldo = float(input('Informe seu saldo'))

def inicio():
    valores = input(''''
        Digite (1) para saque
        Digite (2) para deposito
        Digite (3) para emprestimo
        Digite (4) para visualizar seu saldo
        Digite (Qualquer outro texto ou número) para sair
    ''')
if inicio() == 1:
    print(saque())
elif inicio() == 2:
    print(deposito())
elif inicio() == 3:
    print(emprestimo())
elif inicio() == 4:
    print(visu())
else:

def saque():
    values = float(input('Informe o valor'))
    if values >= 1000 and saldo >= values:
        saldo = saldo - values
        print('Operação realizada com sucesso')
    else:
        print('O valor não pode ser retirado')
    print(saldo)

def deposito(saldo):
    valued = float(input('Informe o valor do deposito'))
    if valued <= 5000:
        saldo = saldo + valued
        print('Operação realizada com sucesso')
    else:
        print('O valor total permitido é de R$5000.00')
print(deposito(saldo))
print(saldo)

def emprestimo(saldo):
    valuee = float(input('Informe o valor do emprestimo'))
    if idade > 21:
        if saldo >= 1000 and valuee >= 2000 and 15*saldo >=valuee:
        saldo = saldo + valuee
    else:
        print('o valor nao pode ser emprestado')
print(emprestimo(saldo))
print(saldo)

def visu():
    print(saldo)

