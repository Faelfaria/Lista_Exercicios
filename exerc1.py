b = []

while True:
    a = int(input("Insira um número para criar uma lista: "))
    b.append(a)
    c = input('Mais algum número? ')
    if c == 'n' :
        break 

d = []
for i in b:
    if i % 2 == 0:
        d .append(i)
print(d)