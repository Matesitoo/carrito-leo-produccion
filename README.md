# API carrito - FastAPI + Supabase + Vercel

API para gestion de clientes, productos y pedidos agregada en Vercel con base de datos Supabase.

## Endpoints Disponibles

### Clientes
- `GET /clientes/obtener_clientes` - Lista todos los clientes
- `GET /clientes/obtener_cliente/{id}` - Obtener cliente por ID
- `POST /clientes/crear_cliente` - Crear nuevo cliente
- `PUT /clientes/modificar_cliente/{id}` - Actualizar cliente
- `DELETE /clientes/eliminar_cliente/{id}` - Eliminar cliente

### Productos
- `GET /productos/obtener_productos` - Lista todos los productos
- `POST /productos/crear_productos` - Crear nuevo producto
- `PUT /productos/modificar_producto/{id}` - Actualizar producto
- `DELETE /productos/eliminar_producto/{id}` - Eliminar producto

### Pedidos
- `POST /pedidos/crear_pedido` - Crear nuevo pedido
- `GET /pedidos/obtener_pedidos` - Lista todos los pedidos
- `GET /pedidos/obtener_pedido/{id}` - Obtener pedido por ID
- `GET /pedidos/obtener_pedido_por_cliente/{nombre}` - Filtrar pedidos por cliente
- `GET /pedidos/total_pedido/{id_pedido}` - Calcular total de pedido
- `GET /pedidos/pedidos_por_fecha/{fecha}` - Filtrar pedidos por fecha

## Estructura de Base de Datos

### Tablas en Supabase:
```sql
- cliente (id_cliente, nombre)
- producto (id_producto, nombre, precio)  
- pedido (id_pedido, id_producto, id_cliente, fecha_pedido)