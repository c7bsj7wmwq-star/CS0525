numeri = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
dimensione = 3

# for numero in numeri:
#     print(numero)

for indice in range(len(numeri) - dimensione + 1):
    gruppo =numeri[indice: indice + dimensione]
    media = sum(gruppo) / dimensione
    print(media)

