import psycopg
from models.models import ProductoModel, ProductoUpdateModel

class ProductosManager:
    def addProducto(self, producto: ProductoModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO producto (nombre, precio) VALUES (%s,%s)",
            (producto.nombre, producto.precio),
        )
        return "Producto agregado"

    def getProductos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT * FROM producto").fetchall()
        return [
            {"id_producto": row[0], "nombre": row[1], "precio": row[2]} for row in res
        ]

    def modificarProducto(self, id: int, producto: ProductoUpdateModel, cursor: psycopg.Cursor) -> str:
        if producto.nombre and producto.precio:
            cursor.execute(
                "UPDATE producto SET nombre = %s, precio = %s WHERE id_producto = %s",
                (producto.nombre, producto.precio, id)
            )
        elif producto.nombre:
            cursor.execute(
                "UPDATE producto SET nombre = %s WHERE id_producto = %s",
                (producto.nombre, id)
            )
        elif producto.precio:
            cursor.execute(
                "UPDATE producto SET precio = %s WHERE id_producto = %s",
                (producto.precio, id)
            )
        return "Producto modificado"

    def eliminarProducto(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id,))
        return "Producto eliminado"