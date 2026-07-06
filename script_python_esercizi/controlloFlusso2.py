eta_persona = int(input("quanti anni hai?"))
biglietto_minimo = "gratuito"
biglietto_medio = "10 euro"
biglietto_massimo = "20 euro"
if eta_persona < 12:
    print(f"il biglietto per la persona x di anni inferiore a 12 è {biglietto_minimo}")
elif eta_persona >= 12 and eta_persona < 18:
    print(f"il biglietto per la persona x di anni compresi tra 12 e 18 è {biglietto_medio} €")
else:
    print(f"il biglietto per la persona x di anni superiore a 18 è {biglietto_massimo} €")
