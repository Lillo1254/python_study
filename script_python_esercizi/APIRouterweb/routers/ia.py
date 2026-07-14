from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/ia",
    tags=["Modelli IA"]
)

# con il prefix /ia l'endpoint sara "baseurl/ia/genera"
@router.get("/genera")
async def genera_testo(
    prompt: str = Query(..., min_length=3, description="Prompt per l'LLM")
):
    return {"status": "successo", "output": f"Risultato IA per: {prompt}"}