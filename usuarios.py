from fastapi import status, HTTPException, Depends, APIRouter
from models.usuario import UsuarioBase
from app.data.database import usuarios
from app.security.auth import verificar_Peticion

from sqlalchemy import Session
from app.data import get_bd
from app.data.usuario import Usuario

router = APIRouter(
    prefix= "/v1/usuarios",
    tags= ['CRUD Usuarios']
    )

#Endpoints CRUD usuarios
@router.get("/")
async def consultaUsuarios():
    return{
        "status":"200",
        "total": len(usuarios),
        "data":usuarios
    }
    
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def leer_usuario(bd:session=Depends(get_bd), id: int):
consultausuarios = bd.query(Usuario).all()

        if usuario["id"] == id:
            return{
                "status": "200",
                "Total":
                "data": usuario
            }

    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
@router.post("/{id}", status_code=status.HTTP_201_CREATED)
async def agregar_usuarios(usuario:UsuarioBase):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail= "El id ya existe"
            )
            
            
            
nuevousuarioBD=Usuario(nombre=usuario.nombre,edad=usuarioP.edad)
    
    bd.add(nuevo_usuario)
    bd.commit()
    bd.refresh(nuevo_usuario)
    
    return{
        "Mensaje": "Usuario agregado",
        "datos":usuario,
        
    }


@router.put("/{id}",status_code=status.HTTP_200_OK)
async def actualizar_usuarios(id: int, usuario_actualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado
            return {
                "mensaje": "Usuario actualizado correctamente",
                "datos": usuario_actualizado
            }
    
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def eliminar_usuario(id: int, usuarioAuth:str= Depends(verificar_Peticion)):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {
                "message": f"Usuario eliminado correctamente por {usuarioAuth}"
            }
    
    raise HTTPException(
        status_code=404,
        detail="El Usuario no existe"
    )
