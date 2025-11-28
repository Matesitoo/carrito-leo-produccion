from pydantic import BaseModel
from typing import Optional

class PedidoModel(BaseModel):
    id_producto: int
    id_cliente: int

class ClienteModel(BaseModel):
    nombre: str

class ProductoModel(BaseModel):
    nombre: str
    precio: int

class ProductoUpdateModel(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[int] = None