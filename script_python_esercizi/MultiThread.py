import time
from threading import Thread

def scarica_dati(sito):
    print(f"[Thread] inizio download dal sito {sito}")
    time.sleep(1)
    print(f"[Thread] Download dal sito {sito} COMPLETATO")

thread1 = Thread(target=scarica_dati, args=("www.google.it",))
thread2 = Thread(target=scarica_dati, args=("www.facebook.it",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Download completato")

def elabora_prompt(nome_utente, secondi):
    print(f"[IA] Avviata analisi per {nome_utente}...")
    time.sleep(secondi)
    print(f"[IA] Risposta inviata a {nome_utente}!")

t1 = Thread(target=elabora_prompt, args=("giovanni", 1.5))
t2 = Thread(target=elabora_prompt, args=("mario", 2.5))
t3 = Thread(target=elabora_prompt, args=("luigi", 3.5))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Analisi completate")

risultati = {}
def moltiplica_differita(nome, numero1, numero2):
    print(f"[Thread] Inizio moltiplicazione di {numero1} e {numero2}")
    time.sleep(2)
    risultato = numero1 * numero2
    print(f"[Thread] Risultato: {numero1} * {numero2} = {risultato}")
    risultati[nome] = risultato

tt1 = Thread(target=moltiplica_differita, args=("thread1", 2, 3))
tt2 = Thread(target=moltiplica_differita, args=("thread2",4, 5))

tt1.start()
tt2.start()

tt1.join()
tt2.join()

print(f"Moltiplicazioni completate risultato: {risultati}")
prodotto_finale = risultati["thread1"] * risultati["thread2"]

def ultima_molt():
    print(f"[Thread] Inizio moltiplicazione di {risultati['thread1']} e {risultati['thread2']}")
    time.sleep(2)
    risultato = risultati["thread1"] * risultati["thread2"]
    print(f"[Thread] Risultato: {risultati['thread1']} * {risultati['thread2']} = {risultato}")
    risultati["thread3"] = risultato

t3 = Thread(target=ultima_molt)
t3.start()
t3.join()

print(f"Moltiplicazioni completate risultato: {risultati}")