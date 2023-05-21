#9- Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.
wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = wpp.split(',')
wpp = [int(num) for num in wpp]

for num in wpp:
    if num < 5:
        print(num)