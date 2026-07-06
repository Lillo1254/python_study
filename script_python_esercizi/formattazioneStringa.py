anno_corrente = 2026
anno_nascita = 1994
anni_persona = anno_corrente - anno_nascita
mex = f"siamo nell'anno {anno_corrente} e la persona è nata nel {anno_nascita} quindi ha {anni_persona} anni"
print(mex)
# stesso risultato usando il print(f"")
print(f"siamo nell'anno {anno_corrente} e la persona è nata nel {anno_nascita} quindi ha {anni_persona} anni")
# oppure possiamo concatenare le stringhe con il simbolo + e convertire i numeri in stringhe con str()
print("siamo nell'anno " + str(anno_corrente) + " e la persona è nata nel " + str(anno_nascita) + " quindi ha " + str(anni_persona) + " anni")
# oppure dichiarare stringhe e variabili separatamente
print("siamo nell'anno" , anno_corrente , "e la persona è nata nel", anno_nascita , "quindi ha", anni_persona , "anni")
# i risultati sono i medesimi ma il primo metodo è più leggibile e più semplice da scrivere.
# a seconda della necessità si puo usare uno o l'altro ricordandosi di gestire bene gli spazi poiche una variabile dichiarata all'interno di una stringa non ha spazi prima e dopo quindi se vogliamo che ci siano spazi dobbiamo inserirli noi manualmente mentre se usiamo la concatenazione con il simbolo + dobbiamo ricordarci di convertire le variabili in stringhe con str() e di inserire gli spazi manualmente tra le variabili e nell'ultimo metodo concatenando le stringe e variabile con " , " python aggiunge di base uno spazio tra le variabili e le stringhe quindi non dobbiamo preoccuparci di inserire gli spazi manualmente.