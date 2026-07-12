import csv

dati_auto = [
    ["Marca", "Modello", "Prezzo"],
    ["Ford", "Mustang", "11799.99"],
    ["Ferrari", "LaFerrari", "1500000.00"],
    ["Tesla", "Model 3", "45000.00"]
]

with open("automobili.csv", mode="w" , newline="", encoding="utf-8") as file:
    scrittore = csv.writer(file, delimiter=";")
    scrittore.writerows(dati_auto)

with open("automobili.csv", mode="r", encoding="utf-8") as file:
    lettore = csv.reader(file)
    for riga in lettore:
        print(riga)