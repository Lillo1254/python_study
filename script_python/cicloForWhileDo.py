prezzi_prodotto = [23, 45, 12, 67, 34]

for prezzo in prezzi_prodotto:
    prezzo_scontato = prezzo * 0.9
    print(f"Prezzo originale: {prezzo}, Prezzo scontato: {prezzo_scontato}")

numero_iniziale = 5
for x in range(1 , 11):
    risultato = numero_iniziale * x
    print(f"{numero_iniziale} x {x} = {risultato}")

for x in range(0, 11, 2):
    risultato = numero_iniziale * x
    print(f"{numero_iniziale} x {x} = {risultato}")

contatore = 1
while contatore <= 5:
    print(f"Contatore: {contatore}")
    contatore += 1
print("Ciclo while terminato.")

""" password = "segreta"
tentativi = 0
while tentativi <= 3:
    inserimento = input("inserisci password ")
    if inserimento == password:
        print("Accesso consentito")
        break
    elif tentativi == 0:
        tentativi += 1
        print(f"Password errata. Tentativi rimasti: {3 - tentativi}")
    elif tentativi == 1:
        tentativi += 1
        print(f"Password errata. Tentativi rimasti: {3 - tentativi}")
    elif tentativi == 2:
        tentativi += 1
        print(f"Password errata. Tentativi rimasti: {3 - tentativi}")
    else:
        print("Accesso negato")
        break """

for i in range(1,11):
    if i == 3:
        print("Salto il numero 3")
        continue
    elif i == 8:
        print("interrompo al numero 8")
        break
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} è un numero pari")
    if i % 3 == 0:
        print(f"il numero {i} è un multiplo di 3")
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} è un numero pari")
    if i % 3 == 0:
        print(f"il numero {i} è un multiplo di 3")
print(i)

for riga in range(1,4):
    for colonna in range(1,4):
        print(f"Riga: {riga}, Colonna: {colonna}", end=" | ")
    print()

for x in range(1,4):
    for y in range(1,4):
        print(x * y, end="-")
    print()

smartphone = {
    "marca": "Samsung",
    "modello": "Galaxy S21",
    "anno": 2021,
    "prezzo": 799.99,
}

for chiave in smartphone.keys():
    print(chiave, " :")

for valore in smartphone.values():
    print(valore)

for chiave, valore in smartphone.items():
    print(chiave, ":", valore)

lista_prod = (
    ("Iphone", 599.99),
    ("Samsung", 799.99),
    ("Xiaomi", 499.99),
    ("Huawei", 699.99),
)

for prodotto, prezzo in lista_prod:
    print(f"Prodotto: {prodotto} Prezzo: {prezzo}")

numeri = [1,2,3,4,5]
quadrati = [n ** 2 for n in numeri]
print(quadrati)

voti_base = [18,20,22,24,26,28]
print("voti base " , voti_base)
voti_con_bonus = [ n + 2 for n in voti_base]
print("voti con bonus" ,voti_con_bonus)