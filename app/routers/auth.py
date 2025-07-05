from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.database import get_session
from app.models import User
from app.auth.jwt_handler import create_token
from app.auth.utils import verificar_password

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    # Buscar usuario por email
    user = session.exec(select(User).where(User.email == form_data.username)).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    try:
        if not verificar_password(form_data.password, user.hashed_password.strip()):
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    except ValueError:
        raise HTTPException(status_code=500, detail="Hash bcrypt inválido")

    # Crear y devolver token
    token = create_token(user.email)
    return {"access_token": token, "token_type": "bearer"}

# ARCHIVO QUE FUNCIONA PARA EL HASH Y VERIFICACIÓN DE CONTRASEÑA
