formu = input("Digite uma lista de palavras separadas por virgula: ").split(',')
nova_lista = []

for palavras in formu:
    if len(palavras) % 2 != 0:
        nova_lista.append(palavras)

print("Palavras com número ímpar de letras:", nova_lista)
