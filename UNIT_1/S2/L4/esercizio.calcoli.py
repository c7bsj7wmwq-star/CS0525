import math  

print("Calcolo del perimetro")
print("1 Quadrato")
print("2 Cerchio")
print("3 Rettangolo")

scelta = input("Scegli la figura (1-3): ")

if scelta == "1":
    # Quadrato: perimetro = lato * 4
    lato = float(input("Inserisci il lato del quadrato: "))
    perimetro = (lato * 4 )
    print(perimetro) #calcola il perimetro del quadrato e stampalo
elif scelta == "2":
    # Cerchio: circonferenza = 2 * pi * r
    r = float(input("Inserisci il raggio del cerchio: "))
    circonferenza = 2 * math.pi * r 
    print(circonferenza)
    #calcola la circonferenza usando math.pi e stampala

elif scelta == "3":
    # Rettangolo: perimetro = base*2 + altezza*2
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro2 = float((base * 2) + (altezza * 2))#: calcola il perimetro del rettangolo e stampalo

else:
    print("Scelta non valida.")
