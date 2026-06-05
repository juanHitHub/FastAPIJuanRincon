from fastapi import FastAPI
from api.v1.api import api_router 



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




app.include_router(api_router, prefix="/api/v1")
















