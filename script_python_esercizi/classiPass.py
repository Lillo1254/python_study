""" import inspect

class Automobile:
    pass
autosportiva = Automobile()
autoUtilitaria = Automobile()
print(type(autosportiva))

class Auto:
    def __init__(self,marca,modello = "non definito",prezzo = 10000):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo

auto_uno = Auto("Ford","Mustang",11799.99)
print(auto_uno.marca)
print(auto_uno.modello)
print(auto_uno.prezzo)
print(type(auto_uno))
print("la mia auto è di marca " , auto_uno.marca , " modello " , auto_uno.modello , " e costa " , auto_uno.prezzo , " euro")
parametri = inspect.signature(Auto.__init__)
print(parametri) """

class AutoCorsa:
    def __init__(self,marca,prezzo , modello = "non definito"):
        self.marca = marca
        self.modello = modello
        self.__prezzo = prezzo
        self.accesa = False

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Prezzo: {self.__prezzo}"

    def ottieni_prezzo(self):
        return self.__prezzo
    
    def accendi_motore(self):
        self.accesa = True
        print("motore acceso")
    
    def spegni_motore(self):
        self.accesa = False
        print("motore spento")

    def imposta_prezzo(self, nuovo_prezzo):
        if nuovo_prezzo > 0:
            self.__prezzo = nuovo_prezzo
            print(f"Prezzo aggiornato con successo a: {self.__prezzo}")
        else:
            print("Errore: Il prezzo deve essere maggiore di zero!")

    def applica_sconto(self,percentuale):
        prezzo_scontato = self.__prezzo - (self.__prezzo * (percentuale / 100))
        self.__prezzo = prezzo_scontato
        print("prezzo scontato", self.__prezzo)

auto_veloce = AutoCorsa("Ford",13000,"Mustang")
auto_veloce.accendi_motore()
auto_veloce.spegni_motore()
auto_veloce.applica_sconto(15)
auto_veloce.imposta_prezzo(15000)
auto_veloce.imposta_prezzo(-15000)
print(auto_veloce.ottieni_prezzo())
print(auto_veloce)

class Moto(AutoCorsa):
    def __init__(self,marca,modello,prezzo, cilindrata = 125, anno = 2000):
        super().__init__(marca, modello, prezzo)
        self.cilindrata = cilindrata
        self.anno = anno

    def accendi_motore(self):
        print("motore acceso brrrrruuuuuuummmmmmmmm")
    def impenna(self):
        print("impennata")

moto = Moto("Honda","CBR",10000)
print(moto.marca , moto.modello , moto.cilindrata , moto.anno)
moto.accendi_motore()
moto.spegni_motore()
moto.impenna()
auto_veloce.accendi_motore
moto.accendi_motore

class Cane:
    def suono(self):
        return "abbaia"

class Gatto(Cane):
    def suono(self):
        return "miagolio"
    
versi = [Cane(),Gatto()]

for verso in versi:
    print(verso.suono())

auto = AutoCorsa("Ferrari", 150000)
moto = Moto("Ducati", "Panigale V4", 100000)

garage = [auto , moto]

for veicolo in garage:
    veicolo.accendi_motore()


class Automotive:
    ruote = 4
    contatore_auto = 0

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Prezzo: {self.prezzo}, Ruote: {self.ruote}"
    
    def __init__(self, marca, modello, prezzo):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        Automotive.contatore_auto += 1

    def __eq__(self,other):
        return self.prezzo == other.prezzo
    def __gt__(self,other):
        return self.prezzo > other.prezzo
    def __lt__(self,other):
        return self.prezzo < other.prezzo
    
    @staticmethod
    def converti_valuta(euro, tasso_cambio = 1.09):
        return f" all'effettivo cambio valuta in dollari il valore è $ {euro * tasso_cambio} "

    @classmethod
    def contatore(cls):
        return f"sono presenti in garage {cls.contatore_auto} automobili"

class Motocicli:
    ruote = 2
    contatore_moto = 0

    def __init__(self, marca, modello, prezzo):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        Motocicli.contatore_moto += 1

    @classmethod
    def contatore(cls):
        return f"sono presenti in garage {cls.contatore_moto} motocicli"
    
    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Prezzo: {self.prezzo}, Ruote: {self.ruote}"

quattro = [Automotive("Ferrari", "LaFerrari", 150000) , Automotive("Alfa Romeo", "Giulietta", 100000), Automotive("Lamborghini", "Aventador", 150000)]
due = [Motocicli("Ducati", "Panigale V4", 100000), Motocicli("Honda", "CBR", 100000), Motocicli("Yamaha", "R1", 100000)]


for veicolo in quattro:
    print(veicolo)

for veicolo in due:
    print(veicolo)

print(Automotive.contatore_auto)
print(Motocicli.contatore_moto)

garageNuovo = [Automotive , Motocicli]

for veicoli in garageNuovo:
    print(veicoli.contatore())

print(Automotive.converti_valuta(1000))

print(quattro[0] == quattro[1])
print(quattro[0] < quattro[1])
print(quattro[0] > quattro[1])