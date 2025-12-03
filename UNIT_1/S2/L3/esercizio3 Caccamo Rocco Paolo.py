import string

def analizza_testo(testo):
    testo = testo.lower()
    trad = str.maketrans('', '', string.punctuation)
    testo_pulito = testo.translate(trad)
    parole = testo_pulito.split()

    conteggi = {}
    for parola in parole:
        if parola in conteggi:
            conteggi[parola] += 1
        else:
            conteggi[parola] = 1

    return conteggi


testo = "Ciao, ciao! Come stai? Stai bene?"
risultato = analizza_testo(testo)
print(risultato)