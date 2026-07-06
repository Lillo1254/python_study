try:
    anni_persona = int(input("quanti anni hai?"))
    print("la persona ha " , anni_persona , " anni")
    print(100 / anni_persona)
except ValueError:
    print("la persona non ha inserito un numero")
except ZeroDivisionError:
    print("la persona non ha inserito un numero diverso da zero")
else:
    print("numero inserito con successo e operazione avvenuto")
finally:
    print("la persona ha inserito un numero pertanto si puo eseguire la chiusura del blocco di codice")