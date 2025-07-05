from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import Province, Canton, District, Category
from app.database import get_session
from typing import List

router = APIRouter(prefix="/location", tags=["Location"])

@router.get("/provinces", response_model=List[Province])
def get_provinces(session: Session = Depends(get_session)):
    return session.exec(select(Province)).all()

@router.get("/cantons", response_model=List[Canton])
def get_cantons(province_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Canton).where(Canton.province_id == province_id)).all()

@router.get("/districts", response_model=List[District])
def get_districts(canton_id: int, session: Session = Depends(get_session)):
    print(f"canton_id recibido: {canton_id}")
    distritos = session.exec(select(District).where(District.canton_id == canton_id)).all()
    print(f"Distritos encontrados: {distritos}")
    return distritos

@router.get("/categories", response_model=List[Category])
def get_categories(session: Session = Depends(get_session)):
    return session.exec(select(Category)).all()


# ENDPOINTS PARA PROVINCIAS, CANTON, DISTRITO Y CATEGORIAS PARA CARGAR LOS DATOS DESDE LA BASE DE DATOS