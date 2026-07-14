from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/utenti", # prefisso per tutte le rotte su questo file
    tags=["Gestione Utenti"] # raggruppa le rotte sotto la voce Gestione Utenti nella Swagger UI "urls_base/docs"
)
class ConfigurazioneUtente(BaseModel):
    email : str = Field(..., description="Indirizzo email dell'utente")
    eta : int = Field(..., gt=17, description="Eta dell'utente")
    tier : str = Field(default="free", description="Tier dell'utente")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def registra_utente(dati: ConfigurazioneUtente):
    if dati.tier not in ["free","premium"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Il tier '{dati.tier}' non é valido. Scegli tra 'free' o 'premium'."
        )
    return {
        "status": "utente creato", "email": dati.email
    }