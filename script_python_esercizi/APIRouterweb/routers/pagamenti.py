from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/pagamenti",
    tags=["operazioni di sistema"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_pagamenti():
    return {"status": "successo", "output": "Elenco pagamenti"}