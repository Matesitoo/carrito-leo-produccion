import psycopg2
from models.models import PedidoModel

class PedidosManager:
    def getPedidos(self, cursor: psycopg2.extensions.cursor) -> list:
        cursor.execute(
            "SELECT pedido.id_pedido, producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto"
        )
        res = cursor.fetchall()
        return [
            {"id_pedido": row[0], "producto": row[1], "precio": row[2], "cliente": row[3]} for row in res
        ]

    def getPedidoForId(self, id: int, cursor: psycopg2.extensions.cursor) -> list:
        cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto=producto.id_producto WHERE pedido.id_pedido = %s",
            (id,),
        )
        res = cursor.fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def getPedidoForCliente(self, nombre: str, cursor: psycopg2.extensions.cursor) -> list | str:
        cursor.execute(
            "SELECT id_cliente FROM cliente WHERE nombre = %s", (nombre,)
        )
        idCliente = cursor.fetchone()
        if idCliente:
            cursor.execute(
                "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto WHERE pedido.id_cliente = %s",
                (idCliente[0],),
            )
            res = cursor.fetchall()
            return [
                {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
            ]
        else:
            return "Error, usuario no encontrado"

    def addPedido(self, pedido: PedidoModel, cursor: psycopg2.extensions.cursor) -> str:
        cursor.execute(
            "INSERT INTO pedido (id_producto, id_cliente) VALUES (%s,%s)",
            (pedido.id_producto, pedido.id_cliente),
        )
        return "pedido agregado"

    def getTotalPedido(self, id_pedido: int, cursor: psycopg2.extensions.cursor) -> dict:
        cursor.execute(
            "SELECT SUM(producto.precio) FROM pedido INNER JOIN producto ON pedido.id_producto = producto.id_producto WHERE pedido.id_pedido = %s",
            (id_pedido,)
        )
        res = cursor.fetchone()
        return {"total": res[0] if res[0] else 0}

    def getPedidosPorFecha(self, fecha: str, cursor: psycopg2.extensions.cursor) -> list:
        cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre, pedido.fecha_pedido FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto WHERE DATE(pedido.fecha_pedido) = %s",
            (fecha,)
        )
        res = cursor.fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2], "fecha": row[3]} for row in res
        ]