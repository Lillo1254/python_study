patente = True
macchina = False
guidare = patente and macchina
print(guidare)
guidare_due = patente or macchina
print(guidare_due)
guidare_tre = not patente
print(guidare_tre)
guidare_quattro = not macchina
print(guidare_quattro)
guidare_cinque = not patente and macchina
print(guidare_cinque)
