# importaciones
from fastapi import FastAPI, status, HTTPException, Depends
import asyncio
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


# Inicializacion
app = FastAPI(
    title='sistema de citas Medicas',
    description='examen 2 parcial TAI206',
    version='1.0'
)

# BD Ficticia
usuarios = [
    {"id": 1 ,"nombre":"martin","edad":21,"sexo":"masculino","fecha":"2026-01-09","activos":True,"sintomas":"dolor de espalda"},
    {"id":2,"nombre":"diego","edad":23,"sexo":"masculino","fecha":"2026-02-10","activos":True,"sintomas":"fiebre"},
    {"id":3,"nombre":"brenda","edad":20,"sexo":"femenino","fecha":"2026-03-12","activos":True,"sintomas":"dolor de cabeza"}
]


# Modelo de Validacion Pydantic
class UsuarioBase(BaseModel):
    id: int = Field(...,gt=0,description="Identificador de Usuario", example="1")
    nombre: str = Field(...,min_length=3,max_length=50,description="Nombre del paciente")
    edad: int = Field(...,ge=0,le=121,description="Edad valida entre 0 y 121")
    sexo: str = Field(...,min_length=3,max_length=50,description="Sexo del paciente")
    fecha: str = Field(...,description="Fecha de la cita")
    activos: bool = Field(...,description="Estado de activación del paciente")
    sintomas: str


# ****************************************************
# Seguridad con HTTP Basic
# ****************************************************
security = HTTPBasic()

def verificar_Peticion(credentials:HTTPBasicCredentials=Depends(security)):
    usuarioAuth = secrets.compare_digest(credentials.username,"root")
    contraAuth = secrets.compare_digest(credentials.password,"1234")
    
    if not (usuarioAuth and contraAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no validas"
        )
        
    return credentials.username


# Endpoints
@app.get("/",tags=['Inicio'])
async def inicio():
    return {"mensaje":"Hola bienvenido a tu sistema de citas medicas"}


@app.get("/v1/bienvenidos", tags=['Inicio'])
async def bienvenido():
    return {"mensaje":"aqui podra realizar su proxima cita medica"}


@app.get("/v1/crear citas/", tags=['CRUD citas'])
async def consultacitas():
    return{
        "status":"200",
        "total": len(usuarios),
        "data":usuarios
    }


@app.get("/v1/usuarios/{id}")
async def obtener_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/v1/listar citas/", tags=['CRUD citas'])
async def crear_citas(usuario:UsuarioBase, usuarioAuth:str= Depends(verificar_Peticion)):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail= "El id ya existe"
            )

    usuarios.append(usuario.dict())

    return{
        "Mensaje": "Usuario agregado",
        "datos":usuario,
        "status":"200"
    }


@app.put("/v1/listar/citas/{id}", tags=['CRUD citasmedicas'])
async def listar_citas(id: int, citas_medicas: UsuarioBase):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = citas_medicas.dict()
            return {
                "mensaje": "Usuario actualizado correctamente",
                "datos": citas_medicas
            }
    
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@app.delete("/v1/usuarios/{id}", tags=['CRUD citasmedicas'])
async def eliminar_citas(id: int, usuarioAuth:str= Depends(verificar_Peticion)):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            eliminado = usuarios.pop(index)
            return {
                "mensaje": "cita eliminada correctamente",
                "datos": eliminado
            }
    
    raise HTTPException(
        status_code=404,
        detail="El Usuario no existe"
    )