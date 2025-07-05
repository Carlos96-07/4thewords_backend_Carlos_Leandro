# hash_test.py
from app.auth.utils import hashear_password # Asegúrate de que hashear_password exista en utils.py
from app.auth.utils import verificar_password

# Prueba
clave = "admin123"
hash_generado = hashear_password(clave)
print(f"Hash generado: {hash_generado}")

# Verificación
print("¿Es válida?", verificar_password("admin123", hash_generado))