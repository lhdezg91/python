from queue import Full
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#el profijo es para que todos los demas metodos asuman que ese es el prefijo por defecto
router = APIRouter(prefix="/products", tags="products",responses={404:{"message":"No encontrado"}})

product_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def product(id:int):
    return product_list[id]

