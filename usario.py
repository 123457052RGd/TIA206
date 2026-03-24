from sqlalchemy import column,Integer,String
from app.data.db import Base

class Usuario(BaseModel):
    __Table__= "tb_usuarios"
    id= column(Integer,primary_key=True,index=True)
    nombre=column(String)
    edad=column(Integer)