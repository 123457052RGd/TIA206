from fastapi import APIRouter
import asyncio
from typing import Optional
from app.data.database import usuarios

router = APIRouter(
    prefix="/misc",   #
    tags=["Varios"]
)

# Endpoint base
@router.get("/")
async def root():
    return {"mensaje": "Hola mundo FastAPI"}

# Endpoint simple
@router.get("/v1/bienvenidos")
async def bienvenido():
    return {"mensaje": "Bienvenidos a tu API REST"}

# Simulación de proceso lento
@router.get("/v1/calificaciones")
async def calificaciones():
    await asyncio.sleep(2)  #
    return {"mensaje": "Tu calificación en TAI es 10"}

# Parámetro obligatorio
@router.get("/v1/parametro/{id}")
async def consulta_usuarios(id: int):
    await asyncio.sleep(1)
    return {"usuario_encontrado": id}

# Parámetro opcional
@router.get("/v1/parametro-opcional/")
async def consulta_op(id: Optional[int] = None):
    await asyncio.sleep(1)

    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {
                    "usuario_encontrado": id,
                    "datos": usuario
                }
        return {"mensaje": "Usuario no encontrado"}
    
    return {"aviso": "No se proporcionó ID"}