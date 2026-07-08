numeri = [1,2,3,4,5,6]
risultato_map = map(lambda x: x * 2, numeri)
def triplo(x):
    return x * 3

risultato_map_tre = map(triplo, numeri)
print(risultato_map)
print(list(risultato_map))
print(list(risultato_map_tre))

marchi = ["ferrari", "lamborghini", "audi", "bmw"]
upperCase = map(lambda x: x.upper(), marchi)
print(list(upperCase))