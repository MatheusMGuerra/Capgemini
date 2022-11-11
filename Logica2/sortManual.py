numeros = []
ordenados = []
aux = 0

#Alimentar
for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
for i in range(0, len(numeros)):
    ordenados.append(numeros[i])

#ordenar
#OBS: Utilizar o debug nas proximas 6 linhas
for i in range(0, 5):
    for j in range(0, 5):
        if ordenados[j] > ordenados[i]:
            aux = ordenados[i]
            ordenados[i] = ordenados[j]
            ordenados[j] = aux

#main
print(numeros)
print(ordenados)