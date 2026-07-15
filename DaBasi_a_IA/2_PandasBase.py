# Pandas si utilizza per manipolare, analizzare e pulire dataset complessi prima di passarli ad un neurone i dati saranno dotati di indice, colonne e valori e si dividono in Series (una singola colonna di dati dotata di indice simile ad un vettore 1D) e DataFrame (un'intera tabella bidimensionale con colonne e righe gestibile tramite codice)
import pandas as pd

dati = {
    "Email": ["utenteA@gmail.com", "utenteB@yahoo.com", "utenteC@outlook.com"],
    "Eta": [25, 17, 34],
    "Acquisto_Premium": [True, False, True]
}
# pd.DataFrame(dizionario) si utilizza per trasformare un dizionario in un dataframe di pandas
df = pd.DataFrame(dati)
print(df ,end="\n\n")
# utilizzato per visualizzare solo le prime "n" righe del dataframe .head(n)
print(df.head(2),end="\n\n")
# utilizzato per visualizzare un riepilogo tecnico del dataframe .info()
print(df.info(),end="\n\n")
# si utilizza la sintassi del dizionario per estrarre una singola colonna del dataframe
print(df["Email"],end="\n\n")

dati_ia = {
    "Prompt": ["Prompt 1", "Prompt 2", "Prompt 3", "Prompt 4", "Prompt 5", "Prompt 6"],
    "token_utilizzati": [1000,1500,1800, 2000, 3000, 4000],
    "successo": [True, False, True, True, False, True]
}

df_ia = pd.DataFrame(dati_ia)
print(df_ia.head(2))
print()
print(df_ia["token_utilizzati"], end="\n\n")

# L'operazione di filtro booleano è utilizzata per estrarre dati che rispettano determinati criteri possiamo aggiungere una condizione per il filtraggio dove ci verra restituita una sequenza di valori boolenai True e False
condizione = df_ia["token_utilizzati"] > 2000
df_filtratro = df_ia[condizione]
print(df_filtratro, end="\n\n")
# possiamo anche far tornare i dati grezzi per essere restituiti a NumPy o PyTorch utilizzando l'attributo .values() o .to_numpy() che rimuove l'indice e l'intestazione di Pandas restituendo un array NumPy puro
vettore_token = df_ia["token_utilizzati"].values
print(vettore_token)
print()
condizione2 = df_ia["successo"] == True
df_filtrato2 = df_ia[condizione2]
print(df_filtrato2)
print()
df_successo = df_filtrato2["token_utilizzati"].values
print(df_successo)