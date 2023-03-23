#5- Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.
import numpy  as np 
b = []

while True:
    numeros = np.array(input("Insira um números para criar uma lista"))
    b.append(numeros)
    c =input("Mais algum número? (s/n)")
    if c == 'n':
        break
lista_ordenada = sorted(b, reverse = True)
print(lista_ordenada)