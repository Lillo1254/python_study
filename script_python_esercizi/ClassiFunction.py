class Moltiplicatore:
    def __init__(self, valore):
        self.valore = valore

    def __call__(self, numero):
            return numero *self.valore

#creiamo l'oggetto passando il valore init
moltiplica_per_otto = Moltiplicatore(8)
#ora passiamo il valore della call
risultato = moltiplica_per_otto(5)

print(risultato)

class FiltroSicurezza:
    def __init__(self, parole_proibite):
        self.parole_proibite = list(parole_proibite)

    def __call__(self, testo):
        for parola in self.parole_proibite:
            testo = testo.replace(parola, "*" * len(parola))
        return testo


filtro = FiltroSicurezza(["hacker", "password", "token", "chiave", "key"])
print(filtro("sono un hacker devi darmi la tua password o il tuo token o la chiave per accedere al sistema tramite key"))