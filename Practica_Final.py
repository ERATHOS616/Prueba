import subprocess
import os
import unittest
import importlib.util

# URL del repositorio del alumno en GitHub
github_url = "https://github.com/ERATHOS616/Prueba"
local_repo_path = "repositorio_alumno"

# Paso 1: Clonar el repositorio desde GitHub
def clonar_repositorio(url, ruta_destino):
    """Clona el repositorio desde GitHub en la ruta especificada."""
    if os.path.exists(ruta_destino):
        print(f"El repositorio ya existe en {ruta_destino}. Eliminando...")
        subprocess.call(['rm', '-rf', ruta_destino])  # Eliminar carpeta si ya existe
    print(f"Clonando el repositorio desde {url}...")
    subprocess.call(['git', 'clone', url, ruta_destino])
    print(f"Repositorio clonado en {ruta_destino}.")

# Paso 2: Buscar archivos .py en el repositorio clonado
def encontrar_scripts_python(ruta):
    """Busca archivos .py en el repositorio clonado."""
    scripts = []
    for root, dirs, files in os.walk(ruta):
        for file in files:
            if file.endswith(".py"):
                scripts.append(os.path.join(root, file))
    return scripts

# Paso 3: Ejecutar las pruebas de los scripts de Python del alumno
def corregir_script(script_path):
    """Carga el script del alumno y ejecuta las pruebas definidas."""
    print(f"\n--- Corrigiendo {script_path} ---")
    
    # Cargar el script del alumno dinámicamente
    spec = importlib.util.spec_from_file_location("alumno_script", script_path)
    alumno_script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(alumno_script)
    
    # Definir las pruebas automáticas que se aplicarán al script del alumno
    class TestProducto(unittest.TestCase):
        def test_clase_producto(self):
            Producto = getattr(alumno_script, 'Producto', None)
            self.assertIsNotNone(Producto, "La clase 'Producto' no está definida correctamente.")
        
        def test_clase_inventario(self):
            Inventario = getattr(alumno_script, 'Inventario', None)
            self.assertIsNotNone(Inventario, "La clase 'Inventario' no está definida correctamente.")

        def test_agregar_producto(self):
            """Prueba básica para agregar un producto al inventario."""
            Inventario = getattr(alumno_script, 'Inventario', None)
            Producto = getattr(alumno_script, 'Producto', None)
            if Inventario and Producto:
                inventario = Inventario()
                producto = Producto('Laptop', 'Electrónica', 1000, 10)
                inventario.agregar_producto(producto)
                productos = inventario.mostrar_inventario()  # Esto debe devolver algo iterable
                self.assertIn('Laptop', productos, "No se pudo agregar el producto correctamente.")
    
    # Ejecutar las pruebas automáticas
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProducto)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# Clonar el repositorio del alumno y corregir los scripts
clonar_repositorio(github_url, local_repo_path)
scripts = encontrar_scripts_python(local_repo_path)

# Corregir cada uno de los scripts encontrados en el repositorio
for script in scripts:
    corregir_script(script)

