wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(i) for i in a]


if len(wpp) < 2:
    print('A lista deve ter pelo menos dois números.')
else:
    oi = sorted(wpp, reverse=True)
    dpum = oi[1]

    print('O segundo número mais alto é:', dpum)