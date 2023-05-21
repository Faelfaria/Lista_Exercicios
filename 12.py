wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(num) for num in wpp]
cor = input('Digite o nome que deseja verificar na lista: ')

if cor in wpp:
    print('O nome está na lista')
else:
    print('O nome não está na lista')