from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/4thewords_prueba_carlos_leandro"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# CONFIGURACION PARA LA CONEXION DE LA BASE DE DATOS