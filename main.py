# importaciones
from fastapi import FastAPI
from app.routers import usuarios, misc

# Inicialización de la API
app = FastAPI(
    title="Mi primer API",
    description="Diego RUBIO GUERRERO - TAI206 ",
    version="1.0"
)

# Registro de routers
app.include_router(usuarios.router)
app.include_router(misc.router)

# Ruta base
@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}



    
