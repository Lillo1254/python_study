from fastapi import FastAPI
from routers.utenti import router as router_utenti # Importare gli oggetti router dai rispettivi file/moduli
from routers.ia import router as router_ia # Importare gli oggetti router dai rispettivi file/moduli
from routers.pagamenti import router as router_pagamenti

app = FastAPI(
    title="Primo titolo",
    description="Prova titolo",
    version="1.0.0"
)
# includiamo i moduli nel core dell'applicazione
app.include_router(router_utenti)
app.include_router(router_ia)
app.include_router(router_pagamenti)

@app.get("/")
async def root():
    return {"message": "Hello World"}