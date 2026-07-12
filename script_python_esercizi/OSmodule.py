import os

cartella_lavoro__attuale = os.getcwd()

print(cartella_lavoro__attuale)

if(os.path.exists("cartella_lavoro_attuale")):
    print("la cartella esiste")
else:
    print("la cartella non esiste")
    print("creazione nuova cartella")
    os.mkdir("cartella_lavoro_attuale")

print(os.listdir())