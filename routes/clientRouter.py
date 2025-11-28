import psycopg2
from fastapi import APIRouter, Depends
from managers.clientesManager import ClienteManager
from managers.conexionManagerSupabase import getCursor
from models.models import ClienteModel

router = APIRouter(prefix="/clientes", tags=["Clientes routes"])
clientManager = ClienteManager()

@router.get("/obtener_clientes")
def getClientes(cursor: psycopg2.extensions.cursor = Depends(getCursor)):
    res = clientManager.getClientes(cursor)
    return res

@router.get("/obtener_cliente/{id}")
def getClienteForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.getClienteForId(id, cursor)
    return res

@router.post("/crear_cliente")
def postCliente(cliente: ClienteModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.addClient(cliente, cursor)
    return {"msg": res}

@router.put("/modificar_cliente/{id}")
def putCliente(id: int, clienteUpdated: ClienteModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.modifyClient(id, clienteUpdated, cursor)
    return {"msg": res}

@router.delete("/eliminar_cliente/{id}")
def deleteCliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.deleteClient(id, cursor)
    return {"msg": res}