import datetime

def tracciatore_login(function):
    def wrapper(*args,**kwargs):
        avvio = datetime.datetime.now()
        print(f"[LOG] AVVIO DEL PROCESSO IN CORSO... {avvio.strftime('%H:%M:%S:%f')}")
        print("[LOG] AVVIO DEL PROCESSO IN CORSO...")
        risultato = function(*args,**kwargs)
        print("[LOG] PROCESSO TERMINATO CON SUCCESSO")
        termine = datetime.datetime.now()
        print(f"[LOG] PROCESSO TERMINATO CON SUCCESSO {termine.strftime('%H:%M:%S:%f')}")
    return wrapper
def avvio_sistema():
    print("avvio sistema riuscito con successo tramite decoratore")

@tracciatore_login
def imposta_prezzo_auto(marca,modello,prezzo):
    print(f"auto {marca} {modello} con prezzo {prezzo}")

imposta_prezzo_auto("Ford","Mustang",11799.99)