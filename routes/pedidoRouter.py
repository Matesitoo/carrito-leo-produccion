import psycopg2
from fastapi import APIRouter, Depends
from managers.conexionManagerSupabase import getCursor
from managers.pedidosManager import PedidosManager
from models.models import PedidoModel

PedidoManager = PedidosManager()
router = APIRouter(prefix="/pedidos", tags=["Pedidos router"])

@router.post("/crear_pedido")
def postPedido(pedido: PedidoModel, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.addPedido(pedido, cursor)
    return {"msg": res}

@router.get("/obtener_pedidos")
def getPedidos(cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.getPedidos(cursor)
    return res

@router.get("/obtener_pedido/{id}")
def getPedidoForId(id: int, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.getPedidoForId(id, cursor)
    return res

@router.get("/obtener_pedido_por_cliente/{nombre}")
def getPedidoForCliente(nombre: str, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.getPedidoForCliente(nombre, cursor)
    return res

@router.get("/total_pedido/{id_pedido}")
def getTotalPedido(id_pedido: int, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.getTotalPedido(id_pedido, cursor)
    return res

@router.get("/pedidos_por_fecha/{fecha}")
def getPedidosPorFecha(fecha: str, cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = PedidoManager.getPedidosPorFecha(fecha, cursor)
    return res