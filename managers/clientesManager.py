import psycopg2
from models.models import ClienteModel

class ClienteManager:
    def addClient(self, cliente: ClienteModel, cursor: psycopg2.extensions.cursor) -> str:
        cursor.execute(
            "INSERT INTO cliente (nombre) VALUES (%s)",
            (cliente.nombre,),
        )
        return "cliente creado"

    def getClientes(self, cursor: psycopg2.extensions.cursor) -> list:
        cursor.execute("SELECT id_cliente,nombre FROM cliente")
        res = cursor.fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]

    def getClienteForId(self, id: int, cursor: psycopg2.extensions.cursor) -> list:
        cursor.execute(
            "SELECT id_cliente,nombre FROM cliente WHERE id_cliente = %s", (id,)
        )
        res = cursor.fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]

    def modifyClient(self, id: int, updatedClient: ClienteModel, cursor: psycopg2.extensions.cursor) -> str:
        cursor.execute(
            "UPDATE cliente SET nombre = %s WHERE id_cliente = %s",
            (updatedClient.nombre, id),
        )
        return "Cliente modificado!"

    def deleteClient(self, id: int, cursor: psycopg2.extensions.cursor) -> str:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id,))
        return "Cliente eliminado"