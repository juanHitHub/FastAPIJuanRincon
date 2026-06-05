from sqlalchemy.orm import Session 
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate







def crear_producto(db: Session, producto:ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto





def obtener_productos(db:Session):
    return db.query(Producto).all()


def obtener_producto(db:Session, producto_id: int ):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def update_producto(db:Session, producto_id: int, datos:ProductoCreate):
    producto = obtener_producto(db, producto_id)

    if producto:
        for key, value in datos.dict().items():
            setattr(producto, key, value)
        db.commit()
        db.refresh(producto)
    return producto

def delete_producto(db:Session, producto_id: int):
    producto = obtener_producto(db, producto_id)

    if producto:
        db.delete(producto)
        db.commit()
    return producto
