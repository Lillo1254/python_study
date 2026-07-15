# Ogni singola informazione che un'Intelligenza Artificiale elabora viene convertita in una serie di numeri ordinati in tabelle multidimensionali anche chiamate Tensori
""" Le 4 dimensioni dei DATI IN IA 
Scalare ( 0 dimensioni) un singolo numero
Vettore ( 1 dimensioni) una serie di numeri in una lista
Matrice ( 2 dimensioni) una serie di numeri in una matrice (una tabella di numeri con righe e colonne)
Tensore (3 o piu dimensioni) una serie di matrici sovrapposte 
"""

import numpy as np
# creazione di un vettore
# np.array() converte una lista python in un array Numpy
vettore = np.array([1.0, 2.0, 3.5])


# ogni lista è un campione di dati ed ogni elemento è una caratteristica di quel campione questa è una matrice con 3 campioni e 3 caratteristiche ognuno
# np.array() converte una lista python in un array Numpy

matrice = np.array(
    [[1.0, 2.0, 3.5], 
    [4.0, 5.0, 6.0], 
    [7.0, 8.0, 9.0]]
    )
print(f"Dimensioni (rank) matrice: {matrice.ndim}") # ci specifica le dimensioni del nostro tensore

print(f"Forma (Shape) matrice: {matrice.shape}") # .shape dice esattamente la geometria del tuo tensore. Se la forma dell'input non combacia millimetricamente con la forma accettata dai neuroni della tua rete, il sistema si blocca con un RuntimeError

print(f"tipo dati matrice: {matrice.dtype}") # .dtype specifica il tipo di precisione numerica. Di default in NumPy è float64, ma nel Deep Learning useremo quasi sempre float32 o bfloat16 per risparmiare memoria sulla GPU durante i calcoli complessi

matrice_immagine = np.array([
    [0,0.1,0.2],
    [0.3,0.4,0.5],
    [0.6,0.7,0.8],
    [0.9,0.9,1.0]
    ])
print(f"Dimensioni (rank) matrice immagine: {matrice_immagine.ndim}")
print(f"Forma (Shape) matrice immagine: {matrice_immagine.shape}")
print(f"tipo dati matrice immagine: {matrice_immagine.dtype}")

immagine_scalata = matrice_immagine * 255
# Broadcasting esecuzione di un numero per tutti i valori della matrice generando una nuova matrice senza utilizzare un ciclo for
print(f"immagine scalata: {immagine_scalata}")

# Flattening trasformare una matrice in un vettore a 1 dimensione senza perdere i valori  bisogna conoscere il numero totale di elementi nella matrice è possibile anche modificare la struttura della matrice stessa (3x4 a 6x2) purche il totale elementi sia uguale per farlo si utilizza il comando .reshape() 

matrice_immagine_flat = matrice_immagine.reshape(2,6)
print(f"matrice immagine flat: {matrice_immagine_flat}")

matrice_immagine_flattening = matrice_immagine.reshape(12)
print(f"matrice immagine flat: {matrice_immagine_flat}")

# passando il parametro " -1 " a .reshape(-1) si ottiene la stessa matrice immagine_flat facendo fare in automatico i clacoli a NumPy

matrice_immagine_flattening_auto = matrice_immagine.reshape(-1)
print(f"matrice immagine flat: {matrice_immagine_flattening_auto}")

# Neurone artificiale - Un neurone artificiale riceve in ingresso dei dati e applica a ciascuno di essi un'importanza diversa(variabile X ), un peso elettrico (variabile W) ). Per calcolare il suo segnale interno, il neurone moltiplica ogni input per il suo rispettivo peso e somma tutti i risultati insieme. In matematica e in NumPy, questa operazione fondamentale (moltiplica e somma) si chiama Prodotto Scalare o Dot Product, e si esegue con il comando np.dot()
""" 
vettore_input = np.array([1, 2, 3])
vettore_peso = np.array([0.5,0.1,-0.2])
il prodotto scalare del vettore input e del vettore peso dа il segnale interno del neurone
risultato = (1*0.5) + (2*0.1) + (3*-0.2) => 0.5 + 0.2 - 0.6 => -0.1
NumPy permette di scriverlo in modo istantaneo senza eseguire questa funzione con il metodo np.dot(X,W)
La formula reale concreta per per la creazione di un neurone artificiale è (input * peso)+bias , quindi al metodo .dot() dobbiamo aggiungere anche il bias di conseguenza la reale funzione sarà np.dot(X,W)+b viene utilizzato per specificità e controllo sull'attivazione del neurone stesso per forzare un numero positivo (attivazione) o un numero negativo per non farlo attivare tranne in caso di input molto foti con pesi elevati
"""

vettore_input=([1,2,3])
vettore_peso=([0.5,0.1,-0.2])

output_neurone = np.dot(vettore_input, vettore_peso)
print(f"output neurone: {output_neurone}")

vettore_X = np.array([0.5, 0.8, 0.1])
vettore_W = np.array([0.2, 0.4, -0.1])
bias = 0.59
bias2= -1.5

attivazione = np.dot(vettore_X, vettore_W)+bias
attivazione2 = np.dot(vettore_X, vettore_W)+bias2
print(f"output neurone: {attivazione}")
print(f"output neurone: {attivazione2}")

"""  
funzione di attivazione ReLU (Rectified Linear Unit) la logica è molto semplice se il numero in ingresso è negativo o zero lo trasforma in 0 e spegne il neurone viceversa se il numero in ingresso è positivo lo lascia cosi com'è matematicamente f(z) = max(0,z) in NumPy si implementa in maniera istantanea utilizzando il comando np.maximum(0, valore)

"""
z1= -2.5
z2 = 1.0
print(np.maximum(0, z1)) # output: 0 neurone spento
print(np.maximum(0, z2)) # output: 1 neurone attivo

output_definitivo = np.maximum(0, attivazione)
output_definitivo2 = np.maximum(0, attivazione2)
print(f"output definitivo: {output_definitivo}")
print(f"output definitivo: {output_definitivo2}")

# I neuroni lavorona in gruppi chiamati Layer(Strati) in un singolo Layer abbiamo piu neuroni che ricevono lo stesso input(X) ma ognuno possiede un proprio set di pesi(W) e il proprio bias(b) quindi ognuno di essi estrarra un valore diverso dallo stesso input. Per rappresentare questo, ricordare che NumPy legge le matrici per verticale (colonna neurone) e poi per orizzontale (riga pesi dei diversi neuroni)

matrice_W = np.array([
    [0.1, 0.2, 0.3],  # Riga 1 (Pesi per la caratteristica 1 nei 3 neuroni)
    [0.4, 0.5, 0.6],  # Riga 2 (Pesi per la caratteristica 2 nei 3 neuroni)
    [0.7, 0.8, 0.9]   # Riga 3 (Pesi per la caratteristica 3 nei 3 neuroni)
])
vettore_b = np.array([0.1, 0.2, 0.3])
vettore_z = np.dot(vettore_X, matrice_W) + vettore_b


print(f"Valori calcolati per i 3 neuroni: {vettore_z}")
print(f"Valori calcolati per i 3 neuroni: {np.maximum(0, vettore_z)}")

# Una vera IA nell'addrestamento e nella produzione elabora i dati sfruttando la potenza della GPU e dei processori svolgendo miliardi di calcoli in parallelo per sfruttare questa potenza dobbiamo inviare al nostro strato di neuroni un blocco (Batch) di piu input contemporaneamente

x2 = np.array([
    [0.5, 0.8, 0.1],
    [0.2,0.8,0.4]
])
w2 = np.array([
    [0.1,0.2,0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
])
b2 = np.array([0.1, 0.2, 0.3])

z3 = np.dot(x2, w2)+b2
print(z3.shape)

matrice_x = np.array([
    [0.5, 0.8, 0.1],
    [0.2,0.8,0.4],
    [0.5, 0.8, 0.1]
])
matrice_w = np.array([
    [0.1,0.2,0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
])
vettore_b = np.array([0.2, 0.4, 0.6])
vettore_z2 = np.dot(matrice_x, matrice_w) + vettore_b

print(f"Valori calcolati per i 3 neuroni: {vettore_z2}")
print(f"Valori calcolati per i 3 neuroni: {np.maximum(0, vettore_z2)}")