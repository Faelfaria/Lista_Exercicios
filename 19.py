nossa = int(input('Digite o número pelo qual deseja dividir: '))
wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(num) for num in wpp]

lista = []

for num in wpp:
    if num % wpp == 0:
        lista.append(num)

print('Os números divisíveis por', nossa, 'são:', lista)