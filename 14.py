wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(i) for i in a]

ordem = sorted(a)
ordem2 = ordem[1]

print('O segundo número mais baixo é: {}').format(ordem2)