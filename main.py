from fastapi import FastAPI
from routes.clientRouter import router as routerClient
from routes.pedidoRouter import router as routerPedidos
from routes.productoRouter import router as routerProducts

app = FastAPI()

app.include_router(routerClient)
app.include_router(routerProducts)
app.include_router(routerPedidos)

@app.get("/")
def root():
    return {"message": "API carrito funcionando con Supabase"}