def ripeti(volte):
    def decoratore(funzione):
        def wrapper(*args, **kwargs):
            for i in range(volte):
                print(f"tentativo: {i + 1}")
                funzione(*args, **kwargs)
        return wrapper
    return decoratore

@ripeti(3)
def genera_immagine(prompt):
    print(f"Generazione in corso per: {prompt}\n")

genera_immagine("Gatto spaziale")


def ripeti(volte):
    def decoratore(funzione):
        def wrapper(*args, **kwargs):
            
            for i in range(volte):
                print(f"Tentativo {i + 1}...")
                funzione(*args, **kwargs) # Esegue la funzione
        return wrapper
    return decoratore

@ripeti(3)
def genera_immagine(prompt):
    print(f"Generazione in corso per: {prompt}\n")

# Chiamata di test
genera_immagine("Gatto cyberpunk")