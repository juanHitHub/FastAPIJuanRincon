
from fastapi import APIRouter
from fastapi import  Depends
from sqlalchemy.orm import Session
from app.schemas.categoria import CategoriaResponse, CategoriaCreate
from app.deps.deps import get_db
from app.crud.categoria import *




api_router = APIRouter()



@api_router.post("/categorias", response_model=CategoriaResponse)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crear_categorias(db, categoria)

@api_router.get("/categorias", response_model=list[CategoriaResponse])
def listar_categoria(db: Session = Depends(get_db)):
    return obtener_categorias(db)
