import asyncio
import time

async def chiama_ia_asincrona(utente):
    print(f"[Async] Chiamata IA avviata per {utente}...")
    await asyncio.sleep(2)
    print(f"[Async] Risposta inviata a {utente}!")

async def main():
    await asyncio.gather(
        chiama_ia_asincrona("giovanni"),
        chiama_ia_asincrona("mario"),
        chiama_ia_asincrona("luigi")
    )

asyncio.run(main())

async def carica_componente(nome, secondi):
    print(f"Avviato caricamento componente {nome}")
    await asyncio.sleep(secondi)
    print(f"Caricamento componente {nome} completato")

async def main():
    await asyncio.gather(
        carica_componente("Home.jsx", 1),
        carica_componente("Footer.jsx", 2),
        carica_componente("Section.jsx", 3)
    )

asyncio.run(main())