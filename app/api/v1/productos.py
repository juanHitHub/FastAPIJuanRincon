from fastapi import APIRouter
from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.producto import *
from app.deps.deps import get_db
from app.deps.deps import  require_admin
from app.crud.producto import *

api_router = APIRouter()



@api_router.get("/", response_model=list[ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
    return obtener_productos(db)

  


@api_router.post("/productos", response_model=ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)




@api_router.put("/productos/{id}", response_model=ProductoCreate)
def actualizar_producto(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    producto = update_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@api_router.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db:Session = Depends(get_db)):
    producto = delete_producto(db, producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado"}