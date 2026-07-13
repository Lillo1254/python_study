import re
testo = "il prezzo della mustang è 11799 dollari dell'anno 1994"
risultato = re.search(r"\d+", testo)
if risultato:
    print(f"il risultato della ricerca e': {risultato.group()}")

prompt_utente = "codice segreto : ID-9942-0000-0000-0000-0000-0000-0000-0000 articolo numero 1234"
print(prompt_utente)
testo_censurato_ID = re.sub(r"ID-[\d-]+", "X", prompt_utente)
print(testo_censurato_ID)
testo_censurato = re.sub(r"\d+", "X" ,prompt_utente )
print(testo_censurato)