citta = ["roma","viterbo","napoli","milano","torino"]
# primo elemtno dell'indice è 0 quindi il primo elemento della lista è roma
print(citta[0])
print(citta[4])
# per aggiungere un elemento alle liste si utilizza il metodo .append()
animali = ["cane","gatto","coniglio"]
animali.append("cavallo")
print(animali)
animali.remove("gatto")
# il metodo len() restituisce il numero di elementi presenti in una lista
totale_animali = len(animali)
print(totale_animali)
animali.append("giaguaro")
animali.append("leone")
animali.append("stella marina")
print(animali)
print(len(animali))
# il metodo .pop() rimuove l'ultimo elemento della lista
animali.pop()
print(animali)
animali.pop(1)
print(animali)
# il metodo .insert() permette di inserire un elemento in una lista in una posizione specifica
animali.insert(1,"gatto")
print(animali)
# il metodo .sort() ordina la lista
animali.sort()
print(animali)
# il metodo .reverse() inverte l'ordine della lista
animali.reverse()
print(animali)
# il metodo .index() restituisce l'indice di un elemento della lista
indice_cavallo = animali.index("cavallo")
print(indice_cavallo)
# il metodo .count() restituisce il numero di volte che un elemento è presente nella lista
numero_cani = animali.count("cane")
print(numero_cani)
# il metodo .clear() rimuove tutti gli elementi della lista
animali.clear()
print(animali)
# il metodo .copy() crea una copia della lista
animali_copia = animali.copy()
print(animali_copia)
# il metodo .extend() permette di aggiungere gli elementi di una lista ad un'altra lista
animali_due = ["cavallo","giraffa","elefante"]
animali.extend(animali_due)
print(animali)

citta_due = ["roma", "viterbo", "napoli", "milano", "torino"]
print(citta_due[1:3])
print(citta_due[1] , citta_due[2])