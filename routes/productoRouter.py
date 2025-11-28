import psycopg2
from fastapi import APIRouter, Depends
from managers.conexionManagerSupabase import getCursor
from managers.productosManager import ProductosManager
from models.models import ProductoModel, ProductoUpdateModel

ProdManager = ProductosManager()
router = APIRouter(prefix="/productos", tags=["Productos router"])

@router.get("/obtener_productos")
def getProductos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.getProductos(cursor)
    return res

@router.post("/crear_productos")
def postProductos(producto: ProductoModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.addProducto(producto, cursor)
    return {"msg": res}

@router.put("/modificar_producto/{id}")
def modificarProducto(id: int, producto: ProductoUpdateModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.modificarProducto(id, producto, cursor)
    return {"msg": res}

@router.delete("/eliminar_producto/{id}")
def eliminarProducto(id: int, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = ProdManager.eliminarProducto(id, cursor)
    return {"msg": res}