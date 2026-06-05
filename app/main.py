from fastapi import FastAPI
import uvicorn
from app.api.v1.api import api_router 
import os


app = FastAPI(
    title="E-commerce API",
    description="""
        Api RESTful completa para la gestion de un E-commerce.

        Incluye:
        - Autenticacion con Jwt
        - Administracion de productos y categorias
        - Carrito de compras
        - Gestion de pedidos
""",
version="1.0.0",

contact={
      "name": "Juan Manuel Rincón Barrón",
    "url": "https://github.com/juanHitHub/FastAPIJuanRincon.git",
    "email": "juanm.rincon.ext@grupocox.com"
},

license_info= {
    "name": "MIT Lincense",
    "url": "https://opensource.org/licences/MIT",
}

)


if __name__== '__main__':
    port = int(os.environ.get("PORT",8000))
    uvicorn.run("main:app",host="0.0.0.0",port=port)
    
DATABASE_URL = os.getenv("DATABASE_URL")

app.include_router(api_router, prefix="/api/v1")
















