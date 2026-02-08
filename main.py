"""
Módulo principal de la aplicación Torneo de Fútbol.

Este módulo es el punto de entrada de la aplicación. Se encarga de:
- Inicializar la aplicación Qt
- Cargar los estilos CSS/QSS
- Instanciar y mostrar la ventana principal

Autor: Boris Baldominos González
Fecha: 2025-2026
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController


def load_stylesheet(app, path):
    """
    Carga y aplica una hoja de estilos QSS a la aplicación.
    
    Args:
        app (QApplication): Instancia de la aplicación Qt
        path (str): Ruta al archivo QSS con los estilos
    """
    qss_path = Path(path)
    if qss_path.exists():
        try:
            with open(qss_path, "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
            print("Estilos cargados correctamente")
        except Exception as e:
            print(f"Error al leer estilos: {e}")

def main():
    """
    Función principal que inicializa y ejecuta la aplicación.
    
    Crea la aplicación Qt, carga los estilos, instancia el controlador
    principal y ejecuta el bucle de eventos de la aplicación.
    """
    print("=" * 80)
    print("INICIANDO APLICACIÓN TORNEO DE FÚTBOL")
    print("=" * 80)
    
    app = QApplication(sys.argv)
    
    # Usar rutas absolutas relativas al archivo main.py
    base_dir = Path(__file__).resolve().parent
    print(f"Directorio base: {base_dir}")
    
    # Aplicar estilos
    load_stylesheet(app, base_dir / "resources" / "qss" / "style.qss")
    
    # Iniciar el controlador principal
    try:
        print("Creando ventana principal...")
        ventana = MainController()
        print("Mostrando ventana...")
        ventana.show()
        print("Iniciando bucle de eventos...")
        sys.exit(app.exec())
    except Exception as e:
        print(f"ERROR al iniciar la ventana: {e}")
        import traceback
        traceback.print_exc()
        input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    main()