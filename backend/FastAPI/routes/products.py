from queue import Full
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

@router.get("/products")
async def users():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]