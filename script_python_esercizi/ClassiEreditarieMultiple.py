import re
from dataclasses import dataclass

class GeneratoreTesto:

    def genera(self):
        print("sto generando testo...")

class GeneratoreImmagini:

    def genera(self):
        print("sto generando immagini...")

class AssistenteAI(GeneratoreImmagini,GeneratoreTesto):
    pass

mio_assistente = AssistenteAI()
mio_assistente.genera()
print(AssistenteAI.mro())

class SanitizzatoreTesto:
    def sanitizza(self, testo): 
        return testo.lower()

class SanitizzatoreRegex:
    def sanitizza(self, testo): 
        return re.sub(r"\d+", "X", testo)

def prepara_prompt(sanitizzatore_generico, testo_originale):
    risultato = sanitizzatore_generico.sanitizza(testo_originale)
    print(f"Risultato elaborato: {risultato}")
prompt_utente = "PROMPT CON NUMERI 1234 E LETTERE MAIUSCOLE"

pulitore_testo = SanitizzatoreTesto()
pulitore_regex = SanitizzatoreRegex()

prepara_prompt(pulitore_testo, prompt_utente)
prepara_prompt(pulitore_regex, prompt_utente)

class ConnessioneDatabase:
    def __enter__(self):
        print("Connessione al database in corso...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Connessione al database terminata.")

    def invia_dati(self, dati):
        print("[DB] invio dati in corso...")

with ConnessioneDatabase() as db:
    db.invia_dati("Dati da inviare al database")


@dataclass
class Auto:
    marca: str = "marca non definito"
    modello: str = "modello non definito"
    prezzo: float = 0
    anno: int = 0

@dataclass
class ConfigurazioneIA:
    prezzo: float = 0
    anno: int = 0
    modello: str = "modello non definito"
    temperatura: float = 0
    token_max : int = 1024

mia_config = ConfigurazioneIA("Llama-3", 9.99, 2023, 0.2, 1000000)
print(mia_config)

@dataclass(kw_only=True)
class Auto:
    marca: str = "marca non definito"
    modello: str = "modello non definito"
    prezzo: float = 0
    anno: int = 0

auto_uno = Auto(marca="Ford",modello="Mustang",prezzo=11799.99, anno=1990)
print(auto_uno)
