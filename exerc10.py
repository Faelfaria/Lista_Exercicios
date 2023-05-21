wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = wpp.split(',')
wpp = [int(num) for num in wpp]

duplicadas = list(set(wpp))

print('A lista sem duplicatas é:', duplicadas)