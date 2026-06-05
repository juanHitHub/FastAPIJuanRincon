
from sqlalchemy.orm import Session 
from app.models.categoria import  Categoria
from app.schemas.categoria import  CategoriaCreate




def crear_categorias(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def obtener_categorias(db:Session):
    return db.query(Categoria).all()


