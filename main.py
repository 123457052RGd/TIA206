

#importaciones
from fastapi import FastAPI

#Inicalizacion
app=FastAPI()

#Endpoints
@app.get("/inicio")
async def hola_mundo():
    return{"mensaje":"hola mundo FastAPI"}


@app.get("/bienvenidos")
async def bienvenidos():
    return{"mensaje":"bienvenidos a mi API con FastAPI"}



# importaciones
from fastapi import FastAPI
import asyncio
from typing import Optional

# Inicialización o Instanvia de la API
app = FastAPI(
    title='mi primer API con FastAPI',
    description='DESARROLLADOR DIEGO RUBIO GUERRERO',
    version='1.0.0'
    
)
#diccionario
usuarios= [
    {"id":1,"nombre":"Diego","Edad":22},
    {"id":2,"nombre":"Badillo","Edad":20},
    {"id":3,"nombre":"Manuel","Edad":22},

]
# Endpoints
@app.get("/", tags=['Inicio'])
async def hola_mundo():
    return {"mensaje": "hola mundo FastAPI"}


@app.get("/bienvenidos", tags=['Inicio'])
async def bienvenidos():
    return {"mensaje": "bienvenidos a mi API con FastAPI"}


@app.get("/v1/calificaciones", tags=["Asincronia"])
async def calificaciones():
    await asyncio.sleep(10)  # espera 10 segundos
    return {"mensaje": "tu calificacion es 10"}


@app.get("/v1/usuario/{id}", tags=["Parametro obligatorio"])
async def consultarusuario(id: int):
    await asyncio.sleep(3)  # espera 10 segundos
    return {"usuario encontrado": id}



@app.get("/v1/usuario_Op/", tags=["Parametro opcioanal"])
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(3)
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Usuario encontrado": id,"Datos": usuario}
        return {"usuario no encontrado"}
    else:
        return {"Aviso":"No se proporcionó un ID"}

    

