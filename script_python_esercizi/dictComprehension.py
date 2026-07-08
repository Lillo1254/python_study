lista = [1,2,-3,-4,5, 0]
valore_numeri = {numValue: bool(numValue) for numValue in lista}
print(valore_numeri)

prodotti_nomi = ["Gomma","Matita","Penna","Carta","Tavola"]
prezzi_singoli = [1.99, 0.99, 0.99, 5.99, 10.99]
accoppiati = zip(prodotti_nomi, prezzi_singoli)

prodotti = {prodotti_nomi: prezzi_singoli for prodotti_nomi, prezzi_singoli in accoppiati}
print(prodotti)