from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    hashed_password: str


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class Province(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Canton(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    province_id: int = Field(foreign_key="province.id")

class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    canton_id: int = Field(foreign_key="canton.id")

class Legend(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    image_url: str
    date: datetime
    category_id: int = Field(foreign_key="category.id")
    province_id: int = Field(foreign_key="province.id")
    canton_id: int = Field(foreign_key="canton.id")
    district_id: int = Field(foreign_key="district.id")

# CLASES PARA LAS TABLAS DE LA BASE DE DATOS CON SUS RESPECTIVOS CAMPOS