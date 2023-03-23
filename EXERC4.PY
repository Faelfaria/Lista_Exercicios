#4-Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.
import numpy as np
b = [int]

while True:
    a = int(input("Coloque um número para criar uma lista: "))
    b.append(b)
    c = input("Deseja colocar mais algum número? (s/n): ")
    if c == 'n':
        break

soma = sum (b)
quant = len (b)
print(soma / quant)