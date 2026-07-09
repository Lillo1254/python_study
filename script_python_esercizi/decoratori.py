def mio_decoratore(funzione_originale):
    def wrapper():
        print("Prima che la funzione venga eseguita....")

        funzione_originale()

        print("dopo che la funzione è stata eseguita")
    return wrapper
def saluta_tutti():
    print("Ciao a tutti")

saluta_tutti = mio_decoratore(saluta_tutti)
saluta_tutti()

def tracciatore_log(function):
    def wrapper():
        print("[LOG] AVVIO DEL PROCESSO IN CORSO...")
        function()
        print("[LOG] PROCESSO TERMINATO CON SUCCESSO")
    return wrapper
def avvio_sistema():
    print("avvio sistema riuscito con successo tramite decoratore")

avvio_sistema = tracciatore_log(avvio_sistema)
avvio_sistema()

def tracciatore_login(function):
    def wrapper(*args,**kwargs):
        print("[LOG] AVVIO DEL PROCESSO IN CORSO...")
        risultato = function(*args,**kwargs)
        print("[LOG] PROCESSO TERMINATO CON SUCCESSO")
    return wrapper
def avvio_sistema():
    print("avvio sistema riuscito con successo tramite decoratore")

@tracciatore_login
def imposta_prezzo_auto(marca,modello,prezzo):
    print(f"auto {marca} {modello} con prezzo {prezzo}")

imposta_prezzo_auto("Ford","Mustang",11799.99)