from app.schemas.usuario import UsuarioResponse, UsuarioCreate
from app.schemas.token import Token
from app.crud.usuario import *
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from app.deps.deps import get_db, require_admin, get_current_user
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, crear_token





api_router = APIRouter()



@api_router.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db:Session = Depends(get_db)):
    try:
        return crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@api_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = obtener_usuario_por_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token = crear_token(sub=user.email, es_admin=user.es_admin)
    return {"access_token": token, "token_type": "bearer"}


@api_router.get("/usuarios/me", response_model=UsuarioResponse)
def leer_perfil(current_user = Depends(get_current_user)):
    return current_user


@api_router.get("/admin/ping")
def admin_ping(_admin = Depends(require_admin)):
    return {"ok": True, "role": "admin"}