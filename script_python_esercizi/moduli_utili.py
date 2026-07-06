import requests
from colorama import Fore, Style, init
init()

def moltiplica_per_due(n):
    return n * 2

print(Fore.GREEN + "Questo testo è verde!")
print(Fore.RED + "Questo testo è rosso!")
print(Style.RESET_ALL + "Tornato al testo normale.")
print(Style.BRIGHT + "Questo testo bianco e brillante!")