# importaciones
from fastapi import FastAPI
from app.routers import usuarios, misc
from app.data.bd import engine
from app.data import usuario


usario.Base.metadato.create_all(bind=engine)


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


v



