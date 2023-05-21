
wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = a.split(',')
wpp = [int(num) for num in a]

dupla = []
unico = []

for num in wpp:
    if num in unico:
        dupla.append(num)
    else:
        unico.append(num)

print('Os números que aparecem mais de uma vez na lista original são:', dupla)