from collections import Counter
parole = ["IA", "Dati", "Python", "IA", "Codice", "IA", "Python", "IA", "Python"]
conteggio = Counter(parole)
print(conteggio)
print(conteggio["IA"])
print(conteggio["Python"])
print(conteggio["Dati"])
print(conteggio["Codice"])
print(conteggio.most_common(2))

prompt_utente = "voglio una foto di una mela verde vicino ad una mela rossa e la voglio ora"
parole = prompt_utente.split(" ")
print(parole)
analisi_frequenza = Counter(parole)
print(analisi_frequenza)
print(analisi_frequenza.most_common(3))

class StrumentoMeteo:

    def ottieni_meteo(self, citta):
        print(f"meteo di {citta} è soleggiato")

plugin = StrumentoMeteo()

azione_richiesta = "ottieni_meteo"

if hasattr(plugin, azione_richiesta):
    metodo = getattr(plugin, azione_richiesta)
    metodo("Roma")
else:
    print("metodo non trovato")