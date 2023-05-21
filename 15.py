
wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(i) for i in a]
unico = []

for i in wpp:
    if i not in unico:
        unico.append(i)

print('A nova lista de números sem duplicatas é:', unico)
