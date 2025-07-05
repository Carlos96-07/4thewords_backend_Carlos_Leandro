from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from app.models import Legend
from app.database import get_session
from app.auth.deps import get_current_user
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CREAR leyenda
@router.post("/", response_model=Legend)
def create_legend(
    name: str = Form(...),
    description: str = Form(...),
    date: datetime = Form(...),
    category_id: int = Form(...),
    province_id: int = Form(...),
    canton_id: int = Form(...),
    district_id: int = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user)
):
    # Guardar imagen
    image_filename = image.filename 
    image_path = f"{UPLOAD_DIR}/{image_filename}" 

    try:
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar la imagen: {e}")

    new_legend = Legend(
        name=name,
        description=description,
        date=date,
        category_id=category_id,
        province_id=province_id,
        canton_id=canton_id,
        district_id=district_id,
        image_url=image_filename # <-- CORRECCIÓN: Guardar solo el nombre del archivo en la DB
    )
    session.add(new_legend)
    session.commit()
    session.refresh(new_legend)
    return new_legend

# LISTAR todas las leyendas con filtros opcionales
@router.get("/", response_model=List[Legend])
def get_legends(
    name: Optional[str] = None,
    category_id: Optional[int] = None,
    province_id: Optional[int] = None,
    canton_id: Optional[int] = None,
    district_id: Optional[int] = None,
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user)
):
    query = select(Legend)

    if name:
        query = query.where(Legend.name.contains(name))
    if category_id:
        query = query.where(Legend.category_id == category_id)
    if province_id:
        query = query.where(Legend.province_id == province_id)
    if canton_id:
        query = query.where(Legend.canton_id == canton_id)
    if district_id:
        query = query.where(Legend.district_id == district_id)

    legends = session.exec(query).all()
    return legends

# OBTENER una leyenda por ID
@router.get("/{legend_id}", response_model=Legend)
def get_legend(legend_id: int, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return legend

# EDITAR leyenda
@router.put("/{legend_id}", response_model=Legend)
def update_legend(
    legend_id: int,
    name: str = Form(...),
    description: str = Form(...),
    date: datetime = Form(...),
    category_id: int = Form(...),
    province_id: int = Form(...),
    canton_id: int = Form(...),
    district_id: int = Form(...),
    image: Optional[UploadFile] = File(None),
    session: Session = Depends(get_session),
    user: str = Depends(get_current_user)
):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")

    # Si se sube imagen nueva
    if image:
        # Opcional: Eliminar la imagen antigua si existe y es diferente
        if legend.image_url and legend.image_url != image.filename:
             old_image_path = os.path.join(UPLOAD_DIR, legend.image_url)
             if os.path.exists(old_image_path):
                 os.remove(old_image_path)

        image_filename = image.filename # <-- OBTENEMOS SOLO EL NOMBRE DEL ARCHIVO
        image_path = f"{UPLOAD_DIR}/{image_filename}" # Construimos la ruta completa para guardar el archivo físicamente
        try:
            with open(image_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            legend.image_url = image_filename # <-- CORRECCIÓN: Guardar solo el nombre del archivo en la DB
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar la imagen: {e}")

    legend.name = name
    legend.description = description
    legend.date = date
    legend.category_id = category_id
    legend.province_id = province_id
    legend.canton_id = canton_id
    legend.district_id = district_id

    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend

# ELIMINAR leyenda
@router.delete("/{legend_id}")
def delete_legend(legend_id: int, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    session.delete(legend)
    session.commit()
    return {"ok": True, "message": "Leyenda eliminada correctamente"}

# ENDPOINTS PARA LA CONFIGURACION DEL CRUD PARA LEYENDAS