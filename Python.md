## Python è un linguaggio di programmazione dinamico, interpretato, multiparadigma , pensato per essere leggibile, veloce da sviluppare e versatile usato quando serve produttività, integrazione, analisi dati, automazione, prototipazione rapida, sviluppo web, machine learning e scripting di sistema.
- Automazione per script ripetitivi, gestione file, processi, API
- Sviluppo web con utilizzo di django , flask, fastAPI
- Data science utilizzando librerie come NumPy, Pandas, Matplotlib, scikit-learn
- Machine learning librerie tensorFlow , Pytorch
- CyberSecurity per analisi log, exploit, automazione SOC
- Scripting di sistema interagendo con OS, processi e networking
<br>
Velocità di sviluppo piuttosto che velocità di esecuzione per prototipi di funzionalità o quando si lavora con dataaset, modelli ML, API, automazione <br>
Non adatto a sistemi di real-time, software grafici, kernel, driver <br>

#### L'estensione degli script python è sempre " .py " i programmi sono semplici file di testo si utilizza questa estensione per far capire all'elaboratore che si tratta di un comando python possiamo poi successivamente utilizzare il comando in terminale per far partire gli script oppure nell'IDE in alto a destra dovrebbe comparire un triangolino per play che farà partire lo script autamticamente nel terminale del'IDE stesso

* `print("testo")` : è il comando fondamentale per mostrare qualcosa a schermo tutto ciò che è all'interno delle "" nelle parentesi viene stampato in terminale
* `print()` : il print() vuoto si utilizza per andare a capo di una riga
* `print("text" , end=" ")`: il comando end=" " si utilizza all'interno di print per dire cosa fare alla fine della riga se lasciare uno spazio vuoto immettere un carattere speciale ecc.. poiche di default il print() termina con \n che serve per andare a capo
* `print("text" , sep="-")` : il comando sep="-" indica al comando print() di utilizzare un separatore tra le variabili che stampera
* `print("text" , file=" ")`
* `type()` : si utilizza il comando type per verificare il tipo di dati di una variabile
* `operatori` :
  * addizione + (utilizzato anche per concatenare stringe con str() e sommare valori di variabili )
  * sottrazione - restituisce type float o type int in base ai valori
  * moltiplicazione * restituisce la moltiplicazione di un valore numerico di una stringa ("abc" * 3 = "abcabcabc) o di una lista (list = [2,4,5] * 3 = [2,4,6,2,4,6,2,4,6])
  * divisione / (restituisce sempre un type float)
  * divisione arrotondando per difetto //
  * modulo restituisce il resto della divisione %
  * esponente (potenza) **
  * le operazioni vengono eseguite con le normali regole matematica quindi moltiplicazione->divisione->addizione o sottrazione
* `  ,  ` : utilizzato per separazione di variabili (es. variabileNumerica , "stringa" , variabileBooleana) 
* `formattazione di stringhe varaibile = f"" oppure print(f"text {variabile} text {variabile2}")` : questo comando puo essere usato in una variabile per scrivere del testo (stringa) con all'interno delle variabili o usato nel comando print()->print(f"") per far stampare una stringa comprensiva di variabili interne varaibile = f"text {mex} text {mex}" oppure print(f"questo è testo con {variabile})
* `input("")` : il comando input() ferma l'esecuzione del programma e aspetta che l'utente digiti qualcosa per proseguire, ogni inserimento nell'input sarà considerato da python come una variabile anche se viene inserito un numero o un valore booleano il valore di input() viene assegnato alla variabile in cui è stato utilizzato (nome_persona = input("inserisci nome") , dopo l'input dell'utente la variabile nome_persona avrà valore dell'input inserito )
* `metodo int()` : trasforma il valore se possibile in numeri interi se un numero contiene un decimale arrotonda per difetto
* `metodo str()` : trasfroma il valore in stringhe
* `metodo float()` : trasforma se possibile il valore in numeri con decimali
* `operatori di confronto` :
  * == indica l'uguaglianza tra due valori
  * != indica la diversità tra il primo e il secondo valore
  * ">" indica che il primo valore è maggiore del secondo
  * "<" indica che il primo valore è minore del secondo
  * ">=" indica che il primo valroe è maggiore o uguale al secondo
  * "<=" indica che il primo valore è minore o uguale al secondo
  * `una variabile che contiene questi operatori di confronto restituira un valore booleano true o false (var = 2 < 1 print(var) ---> false )`
* `if condizione: ... else: ` : controllare il flusso di dati con condizioni specizifiche (if var1 > var2: ... else: ... ) l'uso degli spazi è fondamentale per il controllo dei blocchi di codice in esecuzione i due punti " : " identificano l'inizio del blocco di codice quando la riga torna all'inizio significa che quel blocco è terminato
* `elif condizione:` : aggiunta di piu condizioni in caso la prima non venga rispettata viene provata la seconda poi la terza e cosi via fino al termine con else
* `operatori logici` :
  * and restituisce un valore true se entrambe le condizioni sono vere
  * or restituisce un valore true se almeno una condizione è vera
  * not inverte il risultato trasforma un true in un false
* `list` : le liste sono una struttura di dati una collezione ordinata di elemnti racchiusa tra parentesi [] in cui gli elementi sono separati da " , " ogni elemento ha una posizione determinata da un indice l'indice di partenza è 0
* metodi delle list :
  * .append("elemento) aggiunge un elemento alla fine della lista list.append("qualcosa")
  * .remove() rimuove uno specifico elemento dalla lista list.remove("qualcosa")
  * .pop() rimuove l'ultimo elemento dalla lista list.pop("qualcosa")
  * .sort() ordina la lista list.sort()
  * .insert(insert,"elemento") inserisce un elemento in una specifica posizione di indice list.insert(4,"qualcosa")
  * .reverse() inverte l'ordine degli elementi nella lista list.reverse()
  * .count() restituisce il numero di elementi di uno specifico elemento presenti nella lista list.count("qualcosa)
  * .copy() copia la lista in un altra variabile list_uno = [1,2,3,4] list_due = lista_uno.copy()
  * .extend() unisce gli elementi di una lista ad un altra lista list_uno =[1,2,3,4] list_due=[5,6,7] list_uno.extend(list_due) list_uno = [1,2,3,4,5,6,7]
  * .clear() rimuovew tutti gli elementi da una lista
  * len(list) restituisce il numero di elementi presenti in una lista lista_uno = [1,2,3,4,5] numero_el = len(lista_uno) risultato 5
* `Tuple` :una tupla è identica ad una lista ma con due grandi differenze 
  * 1 si creano utilizzando le parentesi () (es var = () )
  * 2 è immutabile quindi una volta creata non è modificabile
  * viene utilizzata per mantenere dei dati che devono essere immutabili durante l'esecuzione del programma e python le gestisce molto piu velocemente rispetto alle liste in memoria
* `dizionari` : un dizionario è una raccolta di coppie " chiave:valore (key:value) " ed è racchiuso tra parentesi {} (es. var = {key:value, key:value}) i dizionari sono modificabili chiamando il nome del dict e la sua chiave (var[key] = "qualcosa") facendo cosi si modifica il valore associato a quella chiave se la key non esiste ne viene creata una nuova e inserita nel dizionario
* `ciclo for .. in ..` : un ciclo for si utilizza quando si sa quante volte dobbiamo ripetere un ciclo o se vogliamo iterare tutti gli elementi di una collezione come una lista
* `ciclo for i in range(n)` : quando sappiamo quanti cicli deve fare il nostro ciclo in maniera specifica possiamo specificare in range() il numero di volte che si deve ripetere il ciclo for
  * possiamo aggiungere fino a 3 numeri separati da " , " che rispettano "la partenza, la fine , e il passo da tenere (for i in range(0, 11, 2) = fai da 0 a 10 andando di due a due)
* `while` : il ciclo while si utilizza per far svolgere una funzione fino a che non viene soddisfatta una condizione, all'interno del ciclo while possono essere inserite altre condizioni con if elif e il ciclo può essere interrotto con il comando " break "
* `.items` : il metodo .items() si utilizza per estrarre sia le chiavi (key) che i valori (value) contemporaneamente da un dizionario il ciclo for è cosi strutturato utilizzando due variabili invece di una per l'iterazione (for chiave, valore in dict.items(): print() )
* `.keys()`: per estrarre solo le chiavi
* `.values()` : per estrarre solo i valori
* `list comprehension` : python permette di svolgere un operazione effettuata su una lista direttamente su una singola linea sfruttando la creazione di una variabile e l'operazione del ciclo for direttamente nella nuova lista numeri = [1,2,3,4] quadrati_numeri = [numero * 2 for numero in numeri] è possibile anche utilizzare una condizione if all'interno delle parentesi quadra specificatamente la frase sarebbe [espressione matematica for elemento in lista if condizione vera]
* `set` : il set è una collezione che ha tre caratteristiche uniche
  * 1 non accetta duplicati se vengono inseriti argomenti uguali python terrà conto solo del primo
  * 2 gli elementi non hanno un indice specifico
  * 3 vengono creati con {} come i dict ma non hanno una coppia chiave valore
  * l'abbinamento del comando set() unito al comando list() permette di ripulire una lista per eliminare duplicati list(set())
* `def` : questa parola viene utilizzata per la creazione delle funzioni
  * def nomeFunction():
  * def nomeFunction(parametri):
  * `return` : il return viene utilizzato per restituire qualcosa al di fuori della funzione stessa e interrompe l'esecuzione della funzione tutto ciò che è scritto dopo il return non viene eseguito
  * `valori di default` : i valori di default in python vanno scritti sempre per ultimi il loro posizionamento prima dei valori obbligatori genera un errore di sintassi " def nomeFunction(parametro, parametro = default) "
  * ` *args ` : utilizzare questo parametro speciale permette di inserire in una funziona infiniti parametri
  * `**kwargs` : utilizzare questo parametro speciale permette di inserire infiniti parametri per creare un dizionario chiave valore
* `try : .. except: .. ` : try esegue il codice potenzialmente "pericoloso" except esegue codice in caso di rottura del primo blocco 
  * all'interno del blocco try/except possono essere racchiusi altri due blocchi
    * `else` :questo blocco viene eseguito solo se il try non ha generato errori
    * `finally` : questo blocco viene eseguito a preiscindere dalla riuscita del blocco try come operazione di pulizia finale del blocco stesso
* `import` : importazione di funzioni gia pronte all'uso
  * `from` : viene utilizzato per importare un singolo modulo "from math import sqrt "
  * `from datetime import datetime` : importazione del modulo datetime per gestire le date per una corretta formattazione si utilizza il metodo .strftime() string format time
        * strftime() direttive speciali
          * %d giorni (01-31)
          * %m Mese (01-12)
          * %Y Anno (4 cifre)
          * %H Ore
          * %M Minuti
          * %S Secondi
        * strftime("%d/%m/%Y") giorno mese anno
* ogni file .py è un modulo che puo essere importato in un altro modulo tramite "import nome_modulo" o "from nome_modulo import funzione"
* `pip` : utilizzo di questo comando in terminale per installare una nuova libreria ( pip install nome_libreria )
* `venv : poiche a volte è necessario utilizzare diverse versioni della stessa libreria è altrettanto necessario creare degli ambienti virtuali per evitare conflitti tra versioni di libreria diverse il comando fondamentale per creare un ambiente virtuale è "python -m venv venv" dal momento in cui è attivo sulla riga del terminale comparira la scritta venv che indica che tutte le libreria installate da quel momento in poi saranno installate solo sul progetto in corso`
  <br>
* `with open("nome_file" , "w") as file:` : questo modulo si utilizza per scrivere in un file attenzione, se il file gia esiste verra sovrascritto 
* `with open("nome_file" , "r") as file:` : questo modulo si utilizza per leggere un file attenzione, se il file non esiste lancia errore FileNotFoundError
  * il file viene generato nella CWD la cartella di current working directory ovvero dove si trova il terminale al momento dell'esecuzione del codice
  * possiamo decidere dove creare il file inserendo dentro al nome_file il percorso assoluto del file stesso o usare il `modulo os` per far ricercare a python il file stesso
* `with open("nome_file" , "a") as file:` :questo modulo si utilizza per "appendere" in fondo al file qualcosa piuttosto che sovrascrivere o creare il file

#### Creazione istanze e oggetti (ereditarietà, incapsulamento e polimorfismo)
* `class` : la definizione class seguita da un Nome che per convenzione ha la prima lettera maiuscola è una definizione di regole struturali per creare un oggetto che le rispetti 
    * `pass` : è un placeholder dei blocchi di codice serve per non generare errori a livello sintattico viene utilizzo per temporeggiare quando non si sa ancora cosa far eseguire ad un blocco
  * `def __init__(self,key1,key2,...)` : la definizione di questa funzone costruttore " __init__ " e dei suoi parametri dove " self " viene utilizzato per indicare l'oggetto stesso che stiamo creando
    * `import inspect` : utilizzando il modulo nativo inspect si possono ottenere i parametri delle classi creando una variabile e poi stampanda a terminale il valore "parametri = inspect.signature(NomeClass.__ init__) cosi da poter vedere effettivamente quali parametri sono richiesti e quali sono di default
  * `self` : questo parametro sarà richiamato ogni volta poiche indichiamo che i metodi interni alla classe che abbimao creato sia riferiti all'istanza creata da quella classe specifica 
* `class genitore` : la classe genitore o superclasse è una classe principale utilizzata per passare metodi ad una classe figlio in modo da mantenere al minimo il codice
* `class figlio` : la classe figlio o sottoclasse è una classe che eredita metodi di una classe genitore da poter riutilizzare sulle sue istanze 
  * `class Sottoclasse(Superclasse):` : questa sintassi genera una classe comprensiva dei metodi della superclasse una classe figlia può ereditare anche metodi di piu classi genitori
<br>

* ```QUANDO CREIAMO UNA SOTTOCLASSE E UTILIZZIAMO IL METODO COSTRUTTORE I PARAMETRI DEL COSTRUTTORE DELLA SUPERCLASSE ANDRANNO PERSI PER MANTENERLI SI UTILIZZA UNA FUNZIONE SPECIALE "super(). __ init__(parametro1,parametro2,parametro3) POSSIAMO QUINDI DEFINIRE IL NOSTRO COSTRUTTORE CON I NOSTRI PARAMETRI E AGGIUNGERE PARAMETRI NUOVI E NELLA FUNZIONE INSERIRE LA FUNZIONE SPECIALE```
* `Overriding` : all'interno di una sottoclasse possiamo cambiare i valori di un metodo ereditato per renderlo esplicito per quella classe figlio cosi da poter utilizzare di base lo stesso metodo ma con risultati diversi a seconda dell'evenienza, basta ridefinire il metodo nella sottoclasse
* `` __ `` : l'utilizzo di due underscore davanti ad un attributo rende quell'attributo "privato" pertanto non sarà possibile leggerlo o modificarlo dall' esterno
* `getter` : metodo pubblico per leggere il dato protetto " def dato(self): return self.__dato_privato
* `setter` : metodo publico per modificare il dato ma con controlli " def dato(self, mod): if mod > 0 : self.__dato_privato  += mod else: print(non puoi modificare il dato) "
* ` __str__ ` : questo metodo è utilizzato per stampare una rappresentazione testuale dell'oggetto " def __str__(self): return f" tutti i dati dell'oggetto "
* ` ciclo for ` : è possibile utilizzare un ciclo for per far eseguire un comando presente nella superclasse e nella classe ereditaria creando una variabile contenente i diversi oggetti e inserendo nel ciclo for l'esecuzione del metodo comune
* ` @property ` :
* ` @classmethod ` : decoratore per utilizzare le variabili di classe direttamente e svolgere funzioni specifiche per ogni singola classe
* `@staticmethod` : questo decoratore è una funzione indipendente serve per mantere una logica interna della classe stessa senza toccare i dati utile per svolgere funzioni interne
* ` variabili di classe` : è possibile dichiarare una variabile di classe universale per tutti gli oggetti di quella specifica classe semplicemente dichiarando la variabile prima del costruttore
* `metodi di paragone nelle classi` :
      * `__eq __(self, other):` : Gestisce l'uguale (==) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
      * `__lt __(self, other):` : Gestisce il minore di (<) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
      * `__gt __(self, other):` : Gestisce il maggiore di (>) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
* `.__mro__` : print(NomeSottoclasse.__mro __) stampera a schermo la linea di successione dell'ereditarietà dei comandi
* `di base l'importanza,la priorità delle classi genitori è data da come vengono richiata nella sottoclasse (es. class Sottoclasse(ClasseMaggiore, ClasseMinore) )`
* __PROTOCOLLI DI ITERAZIONE
      * `__ iter__` : indica che la classe puo essere inserita in un ciclo for
      * `__ next__` : contiene la logica per consegnare l'elemento successivo tenendo traccia del livello di iterazione tramite un contatore e quando non ci sono piu elementi eseguire il comando " raise StopIteration " per bloccare il ciclo iterativo
``` 
nota importante la sintassi di python non prevede la chiusura della riga con " ; " ma basta andare a capo al fine di ottenere l'interruzione di quella riga 
```
