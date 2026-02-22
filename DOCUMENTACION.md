# 📘 Documentación Técnica - Sistema de Gestión de Torneos de Fútbol

## Índice

1. [Visión General](#visión-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Modelos de Datos](#modelos-de-datos)
4. [Controladores](#controladores)
5. [Vistas e Interfaces](#vistas-e-interfaces)
6. [Flujo de Trabajo](#flujo-de-trabajo)
7. [API de Base de Datos](#api-de-base-de-datos)
8. [Guía de Desarrollo](#guía-de-desarrollo)
9. [Patrones de Diseño](#patrones-de-diseño)
10. [Convenciones de Código](#convenciones-de-código)

---

## Visión General

### Objetivo del Proyecto

Sistema integral para la gestión de torneos de fútbol con sistema de eliminatoria directa, que permite:
- Registro y gestión de equipos y participantes
- Creación y seguimiento de partidos
- Registro de eventos en tiempo real
- Generación automática de estadísticas
- Gestión de calendario y avance de fases

### Tecnologías Base

| Componente | Tecnología | Versión | Propósito |
|------------|-----------|---------|-----------|
| Lenguaje | Python | 3.8+ | Lógica de negocio |
| Framework GUI | PySide6 | 6.x | Interfaz gráfica |
| Base de Datos | SQLite | 3 | Persistencia de datos (archivo local) |
| Conector DB | sqlite3 | Built-in | Comunicación con BD (stdlib Python) |
| Diseño UI | Qt Designer | 6.x | Diseño visual |
| Informes PDF | JasperReports | 6.20.6 | Motor de generación de informes |
| Wrapper Jasper | PyReportJasper | 2.x | Ejecución de reportes desde Python |

---

## Arquitectura del Sistema

### Patrón MVC (Modelo-Vista-Controlador)

El proyecto implementa una arquitectura MVC estricta:

```
┌─────────────────────────────────────────────┐
│                  USUARIO                     │
└─────────────────┬───────────────────────────┘
                  │
          ┌───────▼────────┐
          │     VISTAS     │ ◄─── Qt Designer (.ui)
          │  (views/ui/)   │
          └───────┬────────┘
                  │ Eventos/Señales
          ┌───────▼────────┐
          │ CONTROLADORES  │ ◄─── Lógica de negocio
          │ (controllers/) │
          └───────┬────────┘
                  │ Consultas
          ┌───────▼────────┐
          │    MODELOS     │ ◄─── Acceso a datos
          │   (models/)    │
          └───────┬────────┘
                  │
          ┌───────▼────────┐
          │   BASE DATOS   │
          │     SQLite     │
          └────────────────┘
```

### Componentes Principales

#### 1. Main Controller (`main_controller.py`)
- Gestiona la ventana principal
- Coordina navegación entre vistas
- Mantiene referencias a todos los controladores
- Actualiza el tablero del torneo

#### 2. Controladores Específicos
Cada módulo tiene su controlador dedicado:

| Controlador | Responsabilidad |
|-------------|----------------|
| `equipo_controller.py` | CRUD de equipos, asignación de jugadores |
| `participante_controller.py` | CRUD de participantes, estadísticas |
| `calendario_controller.py` | Visualización y asignación de fechas |
| `enfrentamiento_controller.py` | Creación de partidos, sorteos |
| `eventos_partido_controller.py` | Registro de eventos en tiempo real |
| `listado_equipos_controller.py` | Listados, búsquedas, edición |
| `listado_participantes_controller.py` | Listados, filtros, edición |
| `informes_controller.py` | Generación de informes PDF con JasperReports |
| `creditos_controller.py` | Vista "Acerca de" |
| `guia_controller.py` | Visualizador de manual HTML/PDF |

#### 3. Modelo de Datos (`db_manager.py`)
- Clase `DatabaseManager`: Singleton para conexión DB
- Métodos CRUD para todas las entidades
- Lógica de avance automático de fases
- Cálculo de estadísticas

---

## Modelos de Datos

### Esquema de Base de Datos

```sql
-- Tabla de equipos
CREATE TABLE equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    curso TEXT,
    color TEXT,
    escudo TEXT,
    equipacion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de participantes
CREATE TABLE participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    curso TEXT,
    fecha_nacimiento TEXT,
    posicion TEXT,
    es_jugador INTEGER DEFAULT 1,
    es_arbitro INTEGER DEFAULT 0,
    foto TEXT,
    equipo_id INTEGER,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
);

-- Tabla de partidos
CREATE TABLE partidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_local_id INTEGER NOT NULL,
    equipo_visitante_id INTEGER NOT NULL,
    fase TEXT NOT NULL,
    fecha_hora TEXT,
    arbitro_id INTEGER,
    ganador_id INTEGER,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    finalizado INTEGER DEFAULT 0,
    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id),
    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id),
    FOREIGN KEY (arbitro_id) REFERENCES participantes(id),
    FOREIGN KEY (ganador_id) REFERENCES equipos(id)
);

-- Tabla de estadísticas
CREATE TABLE estadisticas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participante_id INTEGER NOT NULL,
    partido_id INTEGER NOT NULL,
    goles INTEGER DEFAULT 0,
    asistencias INTEGER DEFAULT 0,
    faltas INTEGER DEFAULT 0,
    amarillas INTEGER DEFAULT 0,
    rojas INTEGER DEFAULT 0,
    paradas INTEGER DEFAULT 0,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
);
```

### Relaciones

```
equipos (1) ──────< (N) participantes
             ╲
              ╲
               ╲< partidos (equipo1_id, equipo2_id, ganador_id)
                  │
                  │ (1)
                  │
                  ▼
                  (N) estadisticas ──> (N) participantes
```

---

## Controladores

### Ciclo de Vida de un Controlador

```python
class EjemploController:
    def __init__(self, db_manager, parent_controller=None):
        # 1. Inicialización
        self.db = db_manager
        self.parent_controller = parent_controller
        
        # 2. Cargar UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # 3. Configurar estética
        self.configurar_estetica()
        
        # 4. Conectar señales
        self.setup_connections()
        
        # 5. Cargar datos iniciales
        self.cargar_datos()
    
    def setup_connections(self):
        """Conecta señales de UI con métodos"""
        self.ui.pushButton.clicked.connect(self.on_button_click)
    
    def configurar_estetica(self):
        """Aplica estilos y configura apariencia"""
        self.ui.tableWidget.setAlternatingRowColors(False)
    
    def cargar_datos(self):
        """Carga datos desde la base de datos"""
        datos = self.db.obtener_datos()
        self.mostrar_datos(datos)
```

### Comunicación entre Controladores

```python
# Desde listado_participantes_controller
def editar_participante(self):
    participante_id = self.obtener_id_seleccionado()
    
    # Llamar al controlador de edición a través del parent
    self.parent_controller.vista_participantes.configurar_modo_edicion(
        participante_id
    )
    self.parent_controller.mostrar_registro_participantes()
```

---

## Vistas e Interfaces

### Generación de Interfaces

Las interfaces se diseñan en **Qt Designer** y se convierten a Python:

```bash
# Conversión de .ui a .py
pyside6-uic views/ui/MainWindow.ui -o views/ui/MainWindow_ui.py
```

### Uso de Interfaces en Controladores

```python
from views.ui.MainWindow_ui import Ui_MainWindow

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Aplicar diseño
```

### Componentes UI Principales

| Widget | Uso | Ejemplo |
|--------|-----|---------|
| QLineEdit | Campos de texto | Nombre, apellido |
| QComboBox | Selección de opciones | Curso, posición |
| QDateEdit | Selección de fechas | Fecha nacimiento, fecha partido |
| QRadioButton | Opciones excluyentes | Jugador/Árbitro |
| QTableWidget | Tablas de datos | Listados, estadísticas |
| QLabel | Mostrar imágenes/texto | Escudo, foto |
| QPushButton | Acciones | Guardar, eliminar, volver |
| QStackedWidget | Navegación | Cambio entre vistas |

---

## Flujo de Trabajo

### Flujo de Registro de Equipo

```
Usuario → Completa Formulario
    ↓
Clic en "Registrar"
    ↓
Validación de Datos (controller)
    ↓
¿Válido? → NO → Mostrar Error → Volver a Formulario
    ↓ SÍ
Llamada a db.insertar_equipo()
    ↓
¿Éxito? → NO → Mostrar Error
    ↓ SÍ
Mostrar Confirmación
    ↓
Limpiar Formulario
```

### Flujo de Partido

```
Crear Partido (enfrentamiento_controller)
    ↓
Asignar Fecha (calendario_controller)
    ↓
Iniciar Partido (eventos_partido_controller)
    ↓
Registrar Eventos (goles, tarjetas, etc.)
    ↓
Finalizar Partido
    ↓
Validación (no empate)
    ↓
Determinar Ganador
    ↓
Avanzar Automáticamente a Siguiente Fase
    ↓
Actualizar Tablero Principal
```

---

## API de Base de Datos

### Métodos Principales de DatabaseManager

#### Equipos
```python
def insertar_equipo(nombre, curso, color, escudo, equipacion):
    """Registra un nuevo equipo"""

def obtener_equipos():
    """Obtiene todos los equipos"""

def actualizar_equipo(id, nombre, curso, color, escudo, equipacion):
    """Actualiza datos de un equipo"""

def eliminar_equipo(id):
    """Elimina un equipo y sus relaciones"""
```

#### Participantes
```python
def insertar_participante(nombre, apellido, curso, fecha_nacimiento, 
                         posicion, es_jugador, es_arbitro, foto, equipo_id):
    """Registra un nuevo participante"""

def obtener_participantes():
    """Obtiene todos los participantes"""

def obtener_estadisticas_participante(participante_id):
    """Obtiene estadísticas detalladas por partido"""

def obtener_resumen_estadisticas_participante(participante_id):
    """Obtiene totales de estadísticas"""
```

#### Partidos
```python
def insertar_partido(equipo1_id, equipo2_id, fase, fecha_hora, arbitro_id):
    """Crea un nuevo partido"""

def obtener_partidos_por_fase(fase):
    """Obtiene partidos de una fase específica"""

def finalizar_partido(partido_id, ganador_id):
    """Marca partido como finalizado y avanza ganador"""

def avanzar_equipo_siguiente_fase(ganador_id, fase_actual):
    """Lógica de avance automático entre fases"""
```

#### Estadísticas
```python
def insertar_estadistica(participante_id, partido_id, goles, asistencias,
                        faltas, amarillas, rojas, paradas):
    """Registra un evento en un partido"""

def obtener_estadisticas_por_partido(partido_id):
    """Obtiene todos los eventos de un partido"""
```

---

## Guía de Desarrollo

### Añadir una Nueva Vista

1. **Diseñar en Qt Designer**
   - Crear archivo `.ui` en `views/ui/`
   - Diseñar interfaz visualmente
   
2. **Convertir a Python**
   ```bash
   pyside6-uic views/ui/nueva_vista.ui -o views/ui/nueva_vista_ui.py
   ```

3. **Crear Controlador**
   ```python
   # controllers/nueva_vista_controller.py
   from views.ui.nueva_vista_ui import Ui_Form
   
   class NuevaVistaController(QWidget):
       def __init__(self, db, parent_controller=None):
           super().__init__()
           self.db = db
           self.parent_controller = parent_controller
           self.ui = Ui_Form()
           self.ui.setupUi(self)
           self.setup_connections()
   ```

4. **Registrar en MainController**
   ```python
   # En __init__ de MainController
   self.vista_nueva = NuevaVistaController(self.db, self)
   self.ui.stackedWidget.addWidget(self.vista_nueva)
   
   # En setup_connections()
   self.ui.actionNuevaVista.triggered.connect(self.mostrar_nueva_vista)
   
   # Método para mostrar
   def mostrar_nueva_vista(self):
       self.ui.stackedWidget.setCurrentWidget(self.vista_nueva)
       self.ui.titulo.setText("📋 Nueva Vista 📋")
   ```

### Añadir un Nuevo Método a la Base de Datos

```python
# En models/db_manager.py
def nuevo_metodo(self, parametro):
    """Descripción del método"""
    try:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM tabla WHERE campo = ?
        """, (parametro,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        return None
```

---

## Patrones de Diseño

### Singleton (DatabaseManager)
```python
class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Observer (Signals y Slots)
```python
# Signal: botón emite señal al ser clickeado
self.ui.pushButton.clicked.connect(self.metodo_receptor)

# Slot: método que recibe la señal
def metodo_receptor(self):
    print("Botón clickeado")
```

### Strategy (Validaciones)
```python
def validar_formulario(self):
    if not self.ui.lineEdit.text():
        return False, "Campo requerido"
    return True, ""
```

---

## Convenciones de Código

### Nomenclatura

- **Clases**: PascalCase → `MainController`, `DatabaseManager`
- **Métodos**: snake_case → `cargar_datos()`, `insertar_equipo()`
- **Variables**: snake_case → `equipo_id`, `nombre_equipo`
- **Constantes**: UPPER_SNAKE_CASE → `DB_HOST`, `MAX_EQUIPOS`

### Estructura de Métodos

```python
def nombre_metodo(self, parametro):
    """
    Descripción breve del método.
    
    Args:
        parametro (tipo): Descripción del parámetro
    
    Returns:
        tipo: Descripción del retorno
    """
    # Implementación
    pass
```

### Manejo de Errores

```python
try:
    # Operación que puede fallar
    resultado = self.db.operacion()
except Exception as e:
    # Manejo específico
    QMessageBox.critical(self, "Error", f"Error: {str(e)}")
    return None
finally:
    # Limpieza si es necesaria
    pass
```

---

## Referencias

- [Documentación oficial PySide6](https://doc.qt.io/qtforpython/)
- [Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [Guía Qt/PySide - Héctor Costa](https://hektorprofe.github.io/qt-pyside/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 — DB-API 2.0](https://docs.python.org/3/library/sqlite3.html)
- [PyReportJasper](https://github.com/jadsonbr/pyreportjasper)
- [JasperReports 6.20.6](https://community.jaspersoft.com/)

---

**Última actualización**: Febrero 2026  
**Versión**: 1.0  
**Mantenedor**: Boris Baldominos González
