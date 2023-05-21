wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = wpp.split(',')
wpp = [int(num) for num in wpp]
soma = 0

for num in wpp:
    if int(num) % 2 != 0:
        soma += int(num)

print('A soma de todos os números ímpares na lista é: ', soma)