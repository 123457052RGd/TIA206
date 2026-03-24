sqlalchemy import create_engine
from sqlalchemy
port os

1#,defindiendo la url de la conexion
DATABASE_URL=os.getenv(
    "DATABASE_URL",
    "postgresql:/admin:123456@postgres:5432/DB:miappi"
    
)
#2. creamos el motor de conexion

engine=create_engine(DATABASE_URL)

#3.agregamos sesion local
sesionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#4.Base declarativa para modelos

Base=declarative_base()

#5.funcion para el manejo en session en los request

def get_bd=sesionlocal()
try:
    yield bd
finally:
    bd.close()

