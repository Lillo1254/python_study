## Python è un linguaggio di programmazione dinamico, interpretato, multiparadigma , pensato per essere leggibile, veloce da sviluppare e versatile usato quando serve produttività, integrazione, analisi dati, automazione, prototipazione rapida, sviluppo web, machine learning e scripting di sistema.
#### Estensioni consigliate per vscode : Pylance(microsoft), Python(Microsoft), Python Debug(Microsoft), Python Enviroment(Microsoft), Indent-Rainbow(Oderwat)
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
  * ` (parametri obbligatori, *args, **kwargs) ` questo è lo schema di inserimento dei parametri obbligatorio da rispettare
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
* `.mro()` : metodo utilizzabile su una classe per verificare la sequenza di esecuzione delle funzioni interne ed ereditate
* ` __enter__ ` : permette alla classi di diventare un oggetto da usare con " with " il metodo enter fa l'apertura del blocco effettua un return
* ` __exit__ ` : permette alla classi di diventare un oggetto da usare con " with " il metodo exit termina e gestisce errori del blocco
* ` DECORATORE ` : un decoratore accetta come parametro una funzione...al suo interno aggiunge logica attorno a quella funzione e la restituisce completa e modificata
    * i decoratori al loro interno hanno la funzione wrapper " def wrapper(): " che di base non accetta parametri ma accetta i parametri speciali *args, **kwargs in piu il decoratore si attacca alla prima funzione al di sotto dello stesso che trova
* ` @property ` :
* ` @classmethod ` : decoratore per utilizzare le variabili di classe direttamente e svolgere funzioni specifiche per ogni singola classe
* `@staticmethod` : questo decoratore è una funzione indipendente serve per mantere una logica interna della classe stessa senza toccare i dati utile per svolgere funzioni interne
* ` variabili di classe` : è possibile dichiarare una variabile di classe universale per tutti gli oggetti di quella specifica classe semplicemente dichiarando la variabile prima del costruttore
* `metodi di paragone nelle classi` :
      * `__eq__(self, other):` : Gestisce l'uguale (==) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
      * `__lt__(self, other):` : Gestisce il minore di (<) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
      * `__gt__(self, other):` : Gestisce il maggiore di (>) Il parametro other rappresenta l'altro oggetto con cui stiamo facendo il paragone
* `.__mro__` : print(NomeSottoclasse.__mro __) stampera a schermo la linea di successione dell'ereditarietà dei comandi
* `di base l'importanza,la priorità delle classi genitori è data da come vengono richiata nella sottoclasse (es. class Sottoclasse(ClasseMaggiore, ClasseMinore) )`
* __PROTOCOLLI DI ITERAZIONE
      * `__iter__` : indica che la classe puo essere inserita in un ciclo for
      * `__next__` : contiene la logica per consegnare l'elemento successivo tenendo traccia del livello di iterazione tramite un contatore e quando non ci sono piu elementi eseguire il comando " raise StopIteration " per bloccare il ciclo iterativo
* `Dict comprehension` : la creazione di un dizionario sfruttando una sola riga di codice list = [1,-2,-3,4] valore_numeri
* `zip()` : il metodo zip unisce due liste accoppiando in una Tupla tutti gli elementi che trova con lo stesso indice se le liste hanno numero di indici diverso il metodo zip() si ferma all'indice piu corto durante l'iterazione il nome della lista iterando e creando una Tupla lista1 = [1,2,3,4] lista2 = [a,b,c,d] lista3 = [True,False,True,False] accoppiati = zip(lista1,lista2,lista3) il risultato saranno " n tuple per n indici " accoppiati = [(1,a,true), (2,b,False), (3,c,True), (4,d,False)]
* `function lambda` : permette di scrivere una funziona semplice su una sola riga nome_function = lambda parametro: parametro qualcosa l'utilizzo della parola lambda dentro la function è obbligatorio e possono contenere solo una singola espressione "calcola_media = lambda a, b: (a + b) /2 ---> print(calcola_media(15, 40))"
* `map()` : il metodo map prende due elementi "una funzione, un iterabile" esegue la funzione su ogni elemente dell'iterabile restituendo una nuova variabile modificata
* `upper()` : trasforma tutta la stringa in caratteri MAIUSCOLI
* `filter()` : il metodo filter è utile per mantenere solo gli elementi che soddisfano la condizione true quindi se la condizione è vera mantiene l'elemento altrimento lo scarta
* `reduce()` : questa funzione permette di collassare il primo parametro con il secondo parametro e cosi via non è una funzione nativa ha pertanto bisogno di essere importata tramite "functools" iserendo a inizio dello script "from functools import reduce"
* ` .join() ` : questo metodo serve ad unire elementi tramite un separatore dichiarato (es. tot = ", ".join(collezione) )
* ` datetime ` :modulo nativo di python utilizzato per la gestione oraria un modulo che essendo nativo basta importare con " import datetime " si utilizza il datetime.datetime.now() per restituire l'ora esatta corrente e il metodo " strftime("%H:%M:%S.%f") per la formattazione
* ` os ` : il modulo nativo " os " (Operation system) permette di utilizzare python per intervenire direttamente sul sistema
    * os.getcwd() : (operation system get current working directory) restituisce il percorso esatto della cartella in cui ci troviamo
    * os.listdir() : (operation system list directory) restituisce una lista con i nomi di tutti i file e le cartella presenti in quel percorso
    * os.mkdir("nome_directory") : (operation system make directory) crea una nuova cartella
    * os.remove("nome_file) : operation system remove file comando per cancellazione di file
    * os.rmdir("nome_directory) : operation system remove directory comando per cancellazione directory
    * os.path.join() : costruzione di un percorso per file o cartelle in modo da non errare con le barre \ / poiche automaticamente inserisce la barra a seconda del sistema
  * ` pathlib ` : import path modulo per gestire percorsi e concatenare comandi di os
    * pathlib.Path.cwd() : restituisce il percorso pathlib.Path.cwd()
    * pathlib.Path("percorso/file.txt").read_text() : segue il percorso e entra in lettura 
    * pathlib.Path("percorso/directory").mkdir() : segue il percorso ed esegue mkdir
    * pathlib.Path(".").glob("*.py") : quest comando è utilizzato per trovare all'interno di una directory tutti i file corrispondenti a quesll'estensione in questo caso .py
### MODULI JSON " import json " modulo nativo python
* `json.dumps()` : trasforma un dizionario python in una STRINGA JSON
* `json.loads()` : trasforma una STRINGA JSON in un dizionario python
* `json.dump()` : trasforma un dizionario pythonin un FILE JSON
* `json.load()` : trasforma un FILE JSON in un dizionario python
* ` Pretty Print import pprint o from pprint import pprint è un modulo per la formattazione dei dati complessi utilizzando parametri come "indent=? , sort_keys=true ,separators=(':' , '|') , default=funzione utilizzabile sui dati python come dizionari tuple liste ecc..`
* `importazione modulo nativo csv` : "import csv"
* `CSV comma-separated values` : file di gestione tabelle di dati, OGNI RIGA RAPPRESENTA UNA RIGA DELLA TABELLA E LE COLONNE SONO SEPOARATE DA " , o ; "
* `csv.reader()` : legge il file riga per riga restituendo ogni riga come una lista di stringhe
* `csv.writer()` : permette di scrivere liste di dati direttamente in formato tabellare
* `with open("nome_file",mode="w",newline="",encoding="utf-8)as file: write = csv.writer(file,delimiter=";") write.writerows(file_dati_da_scrivere)` : scrittura con separatore ; per separare colonne
* `with open("automobili.csv", mode="r", encoding="utf-8") as file: lettore = csv.reader(file, delimiter=";") for riga in lettore: print(riga)` : lettura con separatore ; separatore colonne
### moduli RANDOM e SECRETS
`random è usato per la generazione casuale di numeri utilizzati per simulazioni campionamento ma non è sicuro per scopi crittografici perche la sua randomizzazione p pseudo-casuale e quindi un hacker potrebbe prevederla. Per questo motivo è stato inserito il modulo Secrets per generare numeri e stringhe crittograficamente sicuri come password temporanee token e chiavi segrete`
* `random.randint(a,b)` :genera un numero intero casuale compreso tra a e b
* `random.choice(lista)` estrae un singolo elemento a caso da una lista
* `random.random` : genera un numero casuale decimale tra 0 e 1 utilizzato per float casuali e probabilità
* `random.shuffle` : utilizzato per mescolar eelementi all'interno di una lista, creare ordini casuali, randomizzare dataset
* ` secrets.choice(lista) ` : estrae un elemento a caso ma con un imprevedibilità maggiore utilizzando statistiche e fluttazioni di sistema
* ` secrets.token_hex(16) ` : genera una chiave esadecimale utilizzando come seed di partenze statistiche e fluttuazioni del pc stesso rendendo impossibile da prevedere
### modulo RE espressioni regolari
qeusto modulo serve a cercare , convalidare ed estrarre patter di testo complessi utilizzati per verificare se in un testo in un prmpt ci sono dati sensibili o se i dati sono stati scritti nella maniera corretta si usano i Regex. durante l'utilizzo per non incorrere in lettura codice da parte di python in maniera sconveniente dobbiamo mettere davanti al simboli speciale (r"simbolo_speciale")
* ``` le Regex usano dei simboli speciali
  - \d significa "un numero da 0 a 9"
  - + significa "uno o piu di quello precedente"
  - [a-zA-Z] significa "una lettera qualsiasi" ```
* `re.search ` : ricerca di un pattern ovunque nella stringa restituendo la prima occorrenza tramite metodo .group() restituisce oggetto `re.search(r"regex", "testo originale")`
* ` re.match ` : controlla se la stringa inizia con il pattern `re.match(r"regex", "testo originale")` restituisce un oggetto
* ` re.fullmatch() ` : controlla se la stringa combacia completamente `re.fullmatch(r"regex", "testo originale")`
* ` re.findall() ` : trova tutte le corrispondenze `re.findall(r"regex", "testo originale")`
* ` re.finditer() ` : restituisce tutte le occorrenze ma con iteratori specificando le posizioni contesti e gruppi `re.finditer(r"regex", "testo orgiinale")` restituisce un oggetto
* ` re.sub() ` sostituisce tutte le occorrenze del pattern `re.sub(r"regex" , "sostituzione" , "testo originale)`

### Utilizzo di dataclass module per istanziare un oggetto e creare una classe " from dataclasses import dataclass "
* `@dataclass` : questo decoratore dichiara l'inizio dell'utilizzo del dataclass subito sotto a se stesso
* ```@dataclass
      class Utente:
      nome: str = "non definito"
      eta: int
      ```
* è obbligatorio utilizzare il type per dichiararele variabili interne
* istanza dell'oggetto ----> user1 = Utente("alessandro", 32)
* usando il @dataclass poiche mischia la sequenza per la quale vengono inseriti i parametri obbligatori e di default è consigliabili creare classi con tutti parametri di default per evitare errori
* @dataclass(kw_only=True) costringe l'utente ad inserire i parametri con il nome esatto delle variabili (anno=1990) eliminando il problema dell'inserimento dei dati di default
### Modulo nativo itertools " import itertools "
* `itertools.combinations(lista, r)` : estrae tutte le combinazioni possibili di lunghezza r ignorando l'ordine
* `itertools.permutations(lista, r)` : estrae tutte le disposizioni possibili tenendo conto dell'ordine
* `itertools.product(lista1, lista2 o repeat=x)` : crea il "prodotto cartesiano" abbinando ogni elemento della prima lista con ogni elemento della seconda lista il repeat moltiplica la lista per se stessa
### Collezioni avanzate collections
* `modulo nativo collections ` : fornisce strutture dati potenziate from collections import Counter
* `variabile=Counter(lista)` : con il metodo counter di collections ci vengono restituiti gli elementi e il numero degli elementi uguali
* `.most_common(n)` : ci restituisce numero "n" elementi usato piu di frequente con il numero di volte presente nella lista
* ` .split ` : viene utilizzato per troncare la frase quando c'è uno "  spazio  " cosi da creare una lista di parole senza spazi aggiunti
### Introspezione " hasattr, getaatr, setattr capacità del programma di esaminare se stesso mentre è in esecuzione
* `hasattr(oggetto, "nome")` : (Has Attribute) restituisce True se l'oggetto possiede una variabile o un metodo con quel nome e False se invece no
* `getattr(oggetto,"nome")` :  (Get Attribute) estrae letteralmente quella variabile o quel metodo partendo dal suo nome in formato stringa
* `setattr(oggetto, "nome, valore)` : (Set Attribute) inietta una nuova variabile dentro un oggetto esistente
### Decoratori con argomenti
```I decoratori possono accettare argomenti e utilizzarli all'interno dei loro livelli interni tramite 1 livello 2 livello 3 livello di funzione compreso nel wrapper per creare funzioni strutturate e utilizzabili in base all'evenienza per far ripetere o inserire argomenti all'interno di una funzione esterna evitando di dover riscrivere codice piu volte ```
* ` __call__ ` : questo metodo all'interno di una classe permette di utilizzare le parentesi () sull'oggetto creato da quella classe per far si che assuma un comportamento come una funzione. Di norma se usassimo su un oggetto le () python andrebbe in errore poiche dovremmo usare il dot ma con il metodo `__call__` questo comportamento cambia

## blocco concorrenza
GIL global interpreter lock questo processo impedisce a python di utilizzare piu thread contemporaneamente per l'esecuzione di un programma quindi python utilizzera un solo core del processore per volta.<br>
* `Multi-threading(IO-Bound)` : adatto quando il programma deve attendere risposte esterne se è in attesa il thread si sposta e aspetta la risposta su un altro core lasciando libero il core per l'esecuzione di un altro programma
* `Multi-Processing(CPU-Bound)` : adatto quando il programma deve fare calcoli matematici complessi python creera processi separati ognuno con il proprio GIL idipendente sfruttando finalmente tutti i core del processore 
* ` from threading import Thread ` : modulo nativo per Multi-Threading, il modulo Thread è una classe che crea un'oggetto per creare oggetti Thread indipendenti
* `variabile = Thread(target=funzione, args=(tupla_parametri)) ` : creiamo un oggetto Thread con target la funzione da svolgere e una tupla di argomenti se abbiamo solo un parametro da passare aggiungia " , " dopo il primo parametro
* `variabile.start()` : usiamo il metodo .start sugli oggetti creati per farli partire in contemporanea
* `variabile.join()` : aspettiamo che l'esecuzione sia terminata prima di finire il processo
``` per far svolgere processi a diversi thread poiche occorrono risultati di thread precedenti dobbiamo utilizzare il comando .start() e il comando .join() come fossero dei semafori per creare e far passare in un secondo momento variabili generate dal primo thread chesaranno necessarie per l'esecuzione del secondo thread e via discorrendo ```
* ` from threading import Lock ` : questo modulo ci permette di inserire all'interno della funzione un " with Lock(): che premettera l'esecuzione di quella funzione attraverso i thread solo uno per volta evitando cosi di creare un errore nel calcolo (Race Condition)
* ` if __name__ == '__main__': ` : istruzione obbligatoria per creare i processi con il multi-processing per evitare loop infiniti di creazione di processi. un modulo python principale ha `__name__ == '__main__' ` un modulo importato ha `__name__ == 'nome_modulo' ` 
  * all'interno della " if " generare il processo e farlo partire
### async def await l'asincronia per gestire attese ed elaborazione
* `async def` : dichiarazione di una funzione asincrona
* ` await ` : specifica a python di aspettare qualcosa
* ` asyncio.gather() ` : lancia piu funzioni asincrone contemporaneamente attende che tutte finiscono le restituisce in ordine
* ` asyncio.run(funzioni) ` : metodo per l'esecuzione di funzioni asincrone di coroutine una solo per volta
### unit test nativi
il modulo unittest è lo standard di python per creare test unitari che erificano il corretto funzionamento di una singola specifica funzione o unità di codice. per usarlo si crea una classe che eredita da `unittest.TestCase` all'interno di questa classe ogni metodo che inizia con la parola `test_` viene visto da python come un test automatico e per verificarne il funzionamento si utilizzano le `asserzioni`
* creazione della funzione
* creazione della classe ereditiera di unittest.TestCase
* richiamare la funzione creata all'interno della classe unit ma con "test_" davanti al nome
* utilizzare assert per verifiche
* impostare if __name__ == '__main__': unittest.main()
<br>

* ` setUp(self) ` : Viene eseguito in automatico da Python PRIMA di ogni singolo test contenuto nella classe. Si usa per preparare l'ambiente (es. creare l'oggetto da testare)
* `tearDown(self)` : Viene eseguito in automatico DOPO ogni singolo test. Si usa per "pulire" (es. cancellare file temporanei o chiudere connessioni)

### utilizzare libreria esterna " coverage " per lanciare i file .py con " coverage run file.py e successivamente coverage report per stampare sul terminale una tabella contenente le informazioni sui file testati

### Architettura delle API con FastAPI e ASGI metodo .get per richiesta informaizoni .post per invio dati
FastAPI si basa su ASGI (Asynchronous Server Gateway Interface) ASGI permette la gestione nativa di connessioni asincrone, WebSocket e richieste a lungo termine senza bloccare il server, sfruttando l'Event Loop di asyncio FastAPI  è costruito sopra due pilastri fondamentali `Starlette` Un toolkit web ASGI ad altissime prestazioni per la gestione del routing e delle richieste HTTP e `Pydantic` Una libreria per la validazione dei dati e la gestione dei tipi (Data Parsing) tramite i Type Hints di Python visto che dovremo installare librerie esterne necessarie al funzionamento per prima cos per ogni progetto che richiede dipendenze per il suo funzionamente impostiamo una virtual enviroment
* ` python -m venv venv ` : questo comando usato nel terminale genera la cartella /venv poi va attivata la funzionalità tramite...
* ` venv\Scripts\activate ` : su terminale cmd o powershell per attivare venv se attivata correttamente sulla riga di comando ci sarà la parola venv
* ` source vevn/Scripts/activate ` : su terminale gitbash che non mostra la parola venv a riga di comando ma possiamo verificare la corretta attivazione inserendo...
* ` whick python ` : ci restituira un percorso se tutto è stato creato correttamente ci troveremo nella cartella venv " /questo/è/il/percorso/della/nostra_cartella/venv/Scripts/python
* ` pip install "fastapi[standard] ` : comadno per l'installazione della dipendenza fastapi
* ` fastapi dev nome_file.py ` comando per eseguire il server fastapi
* ` uvicorn nome_file_senza_estensione:app --host 127.0.0.1 --port 8000 --reload ` : attivazione del server tramite uvicorn per attivazione istanza ASGI 
* ` from pydantic import BaseModel, Field ` creazione rotte post con l'utilizzo della creazione di un istanza tramite una classe che eredita da BaseModel, Field ha lo stesso comportamento di Query per la validazione dati aggiungendo possibilità di confronto nei parametri come ge=17 ecc
### architettura modulare con APIrouter
APIRouter può essere pensato come una sorta di "mini-applicazione" indipendente. Permette di raggruppare rotte omogenee (es. tutte le rotte per la gestione degli utenti, tutte le rotte per i pagamenti, tutte le rotte per le inferenze IA) all'interno di file separati, per poi iniettarle e centralizzarle nell'applicazione principale FastAPI
``` 
struttura del progetto
mio_progetto/
│
├── routers/
│   ├── utenti.py      <-- Gestisce solo il modulo utenti
│   └── ia.py          <-- Gestisce solo il modulo IA
│
└── main.py            <-- Il punto di ingresso
```
* routers/utenti.py in questo file sara gestita solo la logico legata agli utenti
* importazione di APIRouter da fastapi e non di FastAPI





``` 
nota importante la sintassi di python non prevede la chiusura della riga con " ; " ma basta andare a capo al fine di ottenere l'interruzione di quella riga 
```
