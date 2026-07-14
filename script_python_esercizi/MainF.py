from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel, Field, SecretStr

app = FastAPI(
    title="Primo titolo",
    description="Prova titolo",
    version="1.0.0"
)

@app.get("/")
async def root_1(testo : str = Query(None, min_length=2, max_length=100, description="testo da riportare come messaggio")):
    
    if testo is None:
        return {"message": "Nessun testo fornito nella query string"}
        
    return {"message": testo}



class ConfigurazioneUtente(BaseModel):
    email : str = Field(..., description="Indirizzo email dell'utente")
    # utilizzo di gt=17 sull'eta
    eta : int = Field(..., gt=17, description="Eta dell'utente")
    # aggiungiamo un valore di default a tier = "free"
    tier : str = Field(default="free", description="Tier dell'utente")

@app.post("/registrazione", status_code=status.HTTP_201_CREATED)
async def registra_utente(dati: ConfigurazioneUtente):
    if dati.tier not in ["free", "premium"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Il tier '{dati.tier}' non è valido. Scegli tra 'free' o 'premium'."
        )
    
    return {
        "status": "successo",
        "utente_registrato": {
            "email": dati.email,
            "eta": dati.eta,
            "tier": dati.tier
        }
    }
    
    