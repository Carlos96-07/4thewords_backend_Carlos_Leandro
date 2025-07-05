from fastapi import FastAPI # Importa FastAPI para crear la aplicación web.
from sqlmodel import SQLModel # Importa SQLModel para interactuar con la base de datos de forma tipada.
from app.database import engine
from app.routers import auth, legend, location  
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.staticfiles import StaticFiles


app = FastAPI() # Instancia principal de tu aplicación FastAPI.


origins = [
    "http://localhost",
    "http://localhost:8080", 
    "http://localhost:5173", 
 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],   
    allow_headers=["*"],    
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.on_event("startup") # Función que se ejecuta al iniciar la aplicación.
def startup():
    SQLModel.metadata.create_all(engine) # Genera las tablas en la base de datos.

app.include_router(auth.router,  tags=["Auth"])
app.include_router(legend.router,  tags=["Legends"])
app.include_router(location.router)  

# ARCHIVO PRINCIPAL CON LAS CONFIGURACIONES DEL SISTEMA COMO CORS E INSTANCIA DEL FASTAPI