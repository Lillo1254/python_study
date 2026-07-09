from functools import reduce

def crea_ordine(id_ordine, *args, **kwargs):
    print(f"ordine: {id_ordine}")
    prodotti = reduce(lambda x,y: x + ", " + y , args)
    print(f"prodotti acquistati: {prodotti}")

    for k,v in kwargs.items():
        print(f"{k}: {v}")

crea_ordine("1232432", "penna", "carta", "gomma", "tavola", nome="alessandro", eta="32", corso="informatica", universita=True)

    