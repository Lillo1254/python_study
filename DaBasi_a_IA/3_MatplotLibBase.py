import matplotlib.pyplot as plt
import pandas as pd
# crea una prima figura
plt.figure(1)
# Definizione dei dati da inserire negli assi X e Y
asse_x = ["P1", "P2", "P3", "P4", "P5", "P6"]
asse_y = [1000, 1500, 1800, 2000, 3000, 4000]

# Creazione del grafico basato su assi X e Y e sui punti indicati nella variabili precedenti
plt.plot(asse_x, asse_y, marker='x', color='black', linestyle='-')

# Aggiungere etichette e titolo per renderlo leggibile
plt.xlabel("Prompt") # aggiunge un titolo alla colonna X
plt.ylabel("Numero di Token") # aggiunge un titolo alla colonna Y
plt.title("Consumo Token per Prompt") # aggiunge un titolo al grafico da stampare a schermo
plt.grid(True) # Aggiunge una griglia di sfondo

# mostra un grafico in un interfaccia dedicata
""" plt.show() """
# crea una seconda figura
plt.figure(2)
dati_ia = {
    "Prompt": ["Prompt 1", "Prompt 2", "Prompt 3", "Prompt 4", "Prompt 5", "Prompt 6"],
    "token_utilizzati": [1000,1500,1800, 2000, 3000, 4000],
    "successo": [True, False, True, True, False, True]
}

df_ia = pd.DataFrame(dati_ia)

df_successo = df_ia[df_ia["successo"] == True]

asse_x_df = df_successo["Prompt"]
asse_y_df = df_successo["token_utilizzati"]

plt.bar(asse_x_df, asse_y_df, color='green', width=0.5)

plt.xlabel("Prompt") # aggiunge un titolo alla colonna X
plt.ylabel("Numero di Token") # aggiunge un titolo alla colonna Y
plt.title("Consumo Token per Prompt") # aggiunge un titolo al grafico da stampare a schermo
plt.grid(True) # Aggiunge una griglia di sfondo

# avendo dichiarato le figure da creare mostrera un grafico per ogni figura
plt.show()