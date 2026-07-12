import random
import secrets
numero_dato = random.randint(1,9)
print(numero_dato)
token_sicuro = secrets.token_hex(16)
print(token_sicuro)

# random usa lo schema di Mersenne Twister
lista_auto= ["bmw","ferrari","porsche","audi","jaguar","mercedes", "lamborghini", "alfa romeo", "bugatti", "tesla", "mclaren", "fiat", "peugeot", "volkswagen", "maybach", "aston martin", "mazda"]
auto_random = random.choice(lista_auto)
print(auto_random)

auto_sicura = secrets.choice(lista_auto)
auto_sicura_token = secrets.token_hex(8)
print(auto_sicura)
print(auto_sicura_token)

numero_decimale_casuale = random.random()
print(numero_decimale_casuale)

numero_sicuro = secrets.randbelow(100)
print(numero_sicuro)

lista_casuale = random.shuffle(lista_auto)
print(lista_casuale) # ---> restituisce none perche non crea una nuova lista

random.shuffle(lista_auto) # senza generare una nuova lista semplicemente modifichiamo la lista esistente
print(lista_auto)