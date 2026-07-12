import pathlib
print(f"questa è la cartella corrente : {pathlib.Path.cwd()}")
percorso = "../"

testo =pathlib.Path(percorso,"test_python.txt").read_text()
print(testo)

def CreaCartella(percorso):
    pathlib.Path(f"{percorso}").mkdir(exist_ok=True)

CreaCartella(percorso)

for file in pathlib.Path(".").glob("*.py"):
    print(f"{file}")

