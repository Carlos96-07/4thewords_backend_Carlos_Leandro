from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(plain_password, hashed_password):
    """Verifica si una contraseña plana coincide con una contraseña hasheada."""
    return pwd_context.verify(plain_password, hashed_password)

def hashear_password(password: str) -> str:
    """Hashea una contraseña plana."""
    return pwd_context.hash(password)