""" class Tecnologia:

    def avvia(self):
        print("Sistema operativo in avvio")

class VeicoloGrezzo:

    def avvia(self):
        print("Veicolo in avvio")

class Autotesla(Tecnologia, VeicoloGrezzo):
    pass

miaTesla = Autotesla()
miaTesla.avvia()
print(Autotesla.mro())

class Nonno:
    def saluta(self):
        print("Ciao sono Nonno")
class Mamma:
    def saluta(self):
        print("Ciao sono Mamma")
class Padre:
    def saluta(self):
        print("Ciao sono Padre")
class Figlio(Padre, Mamma):
    pass

f = Figlio()
f.saluta() """

class SistemaAudio:
    def riproduci_musica(self):
        print("canzoni in riproduzione")

class Automotive:
    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Prezzo: {self.prezzo}"
    def __init__(self,marca,modello,prezzo):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.stereo = SistemaAudio()

quattro = [Automotive("Ferrari", "LaFerrari", 150000) , Automotive("Alfa Romeo", "Giulietta", 100000), Automotive("Lamborghini", "Aventador", 150000)]

quattro[0].stereo.riproduci_musica()

class Concessionario:
    def __init__(self,lista_auto):
        self.lista_auto = lista_auto
        self.indice = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice < len(self.lista_auto):
            auto_da_ritornare = self.lista_auto[self.indice]
            self.indice += 1
            print(self.indice)
            return auto_da_ritornare
        else:
            print(f"siamo arrivati al ciclo numero {self.indice} e sono terminati gli oggetti da iterare")
            raise StopIteration
        
mie_auto = ["ferrari", "lamborghini", "audi"]
concessionario = Concessionario(mie_auto)

for auto in concessionario:
    print(auto)

class Prodotti:
    contatore_articoli = 0
    def __init__(self,nome = "prodotto" ,prezzo= 10):
        self.nome = nome
        self.prezzo = prezzo
        Prodotti.contatore_articoli += 1

    def __str__(self):
        return f"Nome: {self.nome}, Prezzo: {self.prezzo}"

    def __repr__(self):
        return f"Nome: {self.nome}, Prezzo: {self.prezzo}"
    def generatore_prodotti(massimo):
        numero_prodotti = 0
        while numero_prodotti < massimo:
            prodotto = Prodotti()
            yield prodotto
            numero_prodotti += 1
            print(numero_prodotti)

for prodotto in Prodotti.generatore_prodotti(12):
    print(f"prodotto numero {prodotto.contatore_articoli}: {prodotto}")

prezzi_base = [10,20,30,40,50,60,70,80,90,100]
prezzi_ivati = [prezzo * 1.22 for prezzo in prezzi_base]
print(prezzi_base, prezzi_ivati, sep="|" )

prezzi_mezzi = [prezzo * 0.5 for prezzo in prezzi_base if prezzo >= 60]
print(prezzi_mezzi)