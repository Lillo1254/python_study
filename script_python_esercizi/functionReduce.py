from functools import reduce

""" numeri = [1,2,3,4,5,6]

prodotto_totale = reduce(lambda x,y: x * y, numeri)
print(prodotto_totale)

prezzi_singoli = [1.99,0.99,0.99,5.99,10.99]
somma_prezzi = reduce(lambda x,y: x + y, prezzi_singoli)
print(somma_prezzi)

def somma_tutto(*args):
    totale = 0
    for n in args:
        totale += n
    return totale

print(somma_tutto(1,2,3,4,5,6))
print(somma_tutto(1.99,0.99,0.99,5.99,10.99)) """

def creaListaSpesaPrezzi(*args):

    totale_spesa = 0
    for n in args:
        totale_spesa += n
    print(totale_spesa)

def creaListaSpesa(*args):
    totale_spesa = reduce(lambda x,y: x + ", " + y , args)
    print(totale_spesa)
    


creaListaSpesaPrezzi(1.99,0.99,0.99,5.99,10.99)
creaListaSpesa("cetrioli", "pane", "latte", "pane", "latte")

def creaProfiloProdotto(nome, **kwargs):
    print(f"nome: {nome}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
    print("fine")

creaProfiloProdotto("pane", prezzo = 1.99, quantita = 5)
creaProfiloProdotto("Maglietta", taglia="M", colore="Blu")
creaProfiloProdotto("Laptop", ram="16GB", ssd="512GB", processore="i7")