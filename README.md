# 4thewords_backend_Carlos_Leandro

Tecnologías Utilizadas
Python 3.x

FastAPI: Framework web de alto rendimiento.

SQLModel: ORM basado en Pydantic y SQLAlchemy para interactuar con la base de datos.

MySQL: Base de datos relacional para el almacenamiento de datos.

Uvicorn: Servidor ASGI para ejecutar la aplicación FastAPI.

Credenciales de Acceso (por defecto)
Para probar la autenticación y las rutas protegidas:

Email: admin@admin.com

Contraseña: admin123

Levantar el Servidor Backend:
Desde la raíz de Proyecto_Back_End:


uvicorn app.main:app --reload --host 127.0.0.1 --port 8080

La API estará accesible en http://localhost:8080.

La documentación interactiva (Swagger UI) estará disponible en http://localhost:8080/docs.
