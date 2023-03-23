nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")
nome_longo = ""
nome_curto = nomes[0]

for nome in nomes:
    if len(nome) > len(nome_longo):
        nome_mais_longo = nome
    if len(nome) < len(nome_curto):
        nome_mais_curto = nome

print("O nome mais longo é:", nome_longo)
print("O nome mais curto é:", nome_curto)
