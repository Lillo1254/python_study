""" def calcolo_quadrato(n):
    quadrato = n * n
    print(f"il quadrato di {n} vale {quadrato}")
calcolo_quadrato(int(input("inserisci un numero: ")))

def calcolo_quadrato_due(n):
    quadrato = n * n
    return quadrato

calcolo_del_quadrato_due = calcolo_quadrato_due(int(input("inserisci un numero: ")))
print("questo è il calcolo della seconda funzione ",calcolo_del_quadrato_due)
 """

def calcolo_prezzo_iva(prezzo, iva = 1.22):
    iva_calcolata = prezzo * iva
    return iva_calcolata

prezzo_auto = calcolo_prezzo_iva(10000)
print(prezzo_auto)
prezzo_pane = calcolo_prezzo_iva(2, 1.04)
print(prezzo_pane)

def lista_spesa(*n):
    for x in n:
        print(x , end="-")
    print()

lista_spesa("pane", "latte", "uova")
lista_spesa("pane", "latte", "uova", "pasta", "carne", "zucchero", "acqua")

def crea_profilo_auto(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")
    return kwargs

prova_return = crea_profilo_auto(marca="Ford", modello="Mustang", anno=2021, prezzo=799.99)
print(prova_return)

specifiche_au = {
    "marca": "Ford",
    "modello": "Mustang",
    "anno": 2021,
    "prezzo": 799.99,
}
crea_profilo_auto(**specifiche_au)
