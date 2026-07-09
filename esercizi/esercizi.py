numeri = [1,2,3,4,5]

for x in numeri:
    print(f"numero: {x}")
    
lista_citta = ("roma", "londra", "torino")
print(lista_citta[0])
print(len(lista_citta))
 
for x in lista_citta:
     print(f'città: {x}')
     
studente = {
    "nome" : "alessandro" , 
    "eta" : 32 ,  
    "corso" : "infromatica"
}
print(studente["nome"])

for x,y in studente.items():
    print(x,y)
    
class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def saluta(self) :
       print(f"ciao sono {self.nome} ed ho {self.eta} anni")
       
       
persone = [Studente("Marco", 32), Studente("filippo", 14)]
for persona in persone:
    persona.saluta()

class StudenteUniversitario(Studente):
  def __init__(self,nome,eta,matricola):
    super().__init__(nome,eta)
    self.matricola = matricola
    
  def info_universita(self):
    print(f"ho la matricola numero: {self.matricola}")
  def saluta(self):
    print(f"sono lo studente universitario {self.nome} di anni {self.eta} e matricola universitaria {self.matricola}")
    
studente_uno = StudenteUniversitario("marco",32,"283uehw")
studente_uno.saluta()
studente_uno.info_universita()

registro = {}

s1 = StudenteUniversitario("Marco", 22, "A123")
s2 = StudenteUniversitario("Luca", 25, "B456")
s3 = StudenteUniversitario("Giulia", 21, "C789")

registro["Marco"] = s1
registro["Luca"] = s2
registro["Giulia"] = s3

for nome, stud in registro.items():
    print(f"Nome: {nome}, Età: {stud.eta}, Matricola: {stud.matricola}")

class Macchine:
  def __init__(self,marchio, anno):
    self.marchio = marchio
    self.anno = anno
  
  def accendi(self):
    print(f"motore acceso dell'auto {self.marchio} ddell' anno {self.anno}")


garage = {}

car1 = Macchine("ferrari",1990)
car2 = Macchine("Aston martin",2010)
car3 = Macchine("BMW",2021)
garage["macchina1"] = car1
garage["macchina2"] = car2
garage["macchina3"] = car3

for x,y in garage.items():
  print(x ,y.marchio, y.anno)

dati = [("Marco", 20), ("Luca", 22), ("Giulia", 19)]
lista = []

for x,y in dati:
   stud = Studente(x,y)
   lista.append(stud)

for x in lista:
    x.saluta()

macchinari = [("ferrari", 1990), ("porsche", 2010), ("bmw", 2021)]
listaAuto = []

for x,y in macchinari:
   auto = Macchine(x,y)
   listaAuto.append(auto)

for x in listaAuto:
    x.accendi()

class ProgettoStud:
    def __init__(self, nome, eta, voti):
        self.nome = nome
        self.eta = eta
        self.voti = voti
    
    def media(self):
       return sum(self.voti) / len(self.voti)

    def saluta(self):
        print(f"ciao sono {self.nome} ed ho {self.eta} anni")
class ProgettoUni(ProgettoStud):
    def __init__(self, nome, eta, voti, matricola):
       super().__init__(nome, eta, voti)
       self.matricola = matricola

    def infoMatricola(self):
        print(f"ho la matricola numero: {self.matricola}")
    
    def saluta(self):
        print(f"sono lo studente universitario {self.nome} di anni {self.eta} e matricola universitaria {self.matricola}")

registrazione = {}

matricola1 = ProgettoUni("Marco", 22, [10, 9, 8], "A123")
matricola2 = ProgettoUni("Luca", 25, [9, 8, 7], "B456")
matricola3 = ProgettoUni("Giulia", 21, [8, 7, 6], "C789")

registrazione["Marco 1"] = matricola1
registrazione["Luca 2"] = matricola2
registrazione["Giulia 3"] = matricola3

def aggiungiStudente():
    nome = input("Inserisci il nome dello studente: ")
    eta = int(input("Inserisci l'eta dello studente: "))
    voti = list(map(int, input("Inserisci i voti dello studente: ").split()))
    matricola = input("Inserisci la matricola dello studente: ")
    studente = ProgettoUni(nome, eta, voti, matricola)
    registrazione[nome] = studente

def cercaStudente(matricola):
    for studente in registrazione.values():
        if studente.matricola == matricola:
            return studente

def stampaStudenti():
    for studente in registrazione.values():
        print(f"Nome: {studente.nome}, Eta: {studente.eta}, Voti: {studente.voti}, Matricola: {studente.matricola}")

while True:
    print("1. Aggiungi studente")
    print("2. Cerca studente")
    print("3. Stampa studenti")
    print("4. Esci")
    scelta = int(input("Scelta: "))
    if scelta == 1:
        aggiungiStudente()
    elif scelta == 2:
        matricola = input("Inserisci la matricola dello studente: ")
        studente = cercaStudente(matricola)
        if studente:
            print(f"Nome: {studente.nome}, Eta: {studente.eta}, Voti: {studente.voti}, Matricola: {studente.matricola}")
        else:
            print("Studente non trovato")
    elif scelta == 3:
        stampaStudenti()
    elif scelta == 4:
        break
