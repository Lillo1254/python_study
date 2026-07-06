import math #importazione di tutti i moduli math di python
""" from math import sqrt, pi """ #importazione di solo alcuni moduli da math
import random
from datetime import datetime

radice = math.sqrt(4)
print(radice)
print(math.pi)

Numero_random = random.randint(1, 100)
print(Numero_random)

adesso = datetime.now()

print("anno " , adesso.year)
print("mese ", adesso.month)
print( "giorno " , adesso.day)
print( "ora " , adesso.hour)
print( "minuto " , adesso.minute)
print( "secondo " , adesso.second)
print( "microsecondo " , adesso.microsecond)

data_italiana = adesso.strftime("%d/%m/%Y")
print(data_italiana)


print(adesso)
print(adesso.strftime("%H:%M:%S"))