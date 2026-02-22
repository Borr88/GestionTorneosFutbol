# ⚽ Sistema de Gestión de Torneos de Fútbol

Sistema de gestión completo para torneos de fútbol con clasificación por eliminatoria, desarrollado con **PySide6** (Qt for Python) y **SQLite**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.x-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)
![JasperReports](https://img.shields.io/badge/JasperReports-6.20.6-orange.svg)
![License](https://img.shields.io/badge/License-Educational-purple.svg)

## 📋 Descripción

Aplicación de escritorio para la gestión integral de torneos de fútbol con sistema de eliminatoria directa. Permite registrar equipos, participantes (jugadores y árbitros), crear enfrentamientos, gestionar eventos de partido en tiempo real y generar estadísticas automáticas.

### ✨ Características Principales

- 🏆 **Gestión de Torneos**: Sistema de eliminatoria directa (Octavos → Cuartos → Semifinales → Final)
- 👥 **Registro de Participantes**: Jugadores y árbitros con fotos y datos completos
- ⚽ **Gestión de Equipos**: Registro con escudo, equipación y jugadores asignados
- 📅 **Calendario Automático**: Asignación de fechas para partidos
- 🎮 **Eventos en Tiempo Real**: Registro de goles, asistencias, tarjetas, faltas y paradas
- 📊 **Estadísticas Automáticas**: Seguimiento individual y por equipo
- � **Generación de Informes PDF**: Tres tipos de informe (Equipos y Jugadores, Partidos y Resultados, Clasificación y Eliminatorias) generados con JasperReports vía PyReportJasper
- �📖 **Manual Integrado**: Guía de usuario en HTML/PDF
- 🎨 **Interfaz Moderna**: Diseño personalizado con Qt Designer

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+**: Lenguaje principal
- **SQLite 3**: Base de datos relacional embebida
- **PyReportJasper**: Generación de informes PDF con JasperReports 6.20.6
- **sqlite-jdbc**: Driver JDBC para conectar JasperReports con SQLite

### Frontend
- **PySide6 (Qt 6.x)**: Framework de interfaz gráfica
- **Qt Designer**: Diseño visual de interfaces (.ui → .py)
- **QSS (Qt Style Sheets)**: Estilos personalizados

### Informes
- **JasperReports 6.20.6**: Motor de generación de informes
- **Jaspersoft Studio 7.x**: Diseño visual de plantillas `.jrxml`
- **PyReportJasper**: Wrapper Python para ejecutar reportes Jasper

### Arquitectura
- **Patrón MVC**: Separación Modelo-Vista-Controlador
- **Programación Orientada a Objetos**: Código modular y mantenible

## 📁 Estructura del Proyecto

```
torneo_futbol/
├── main.py                         # Punto de entrada de la aplicación
├── .env                            # Variables de entorno (DB)
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── DOCUMENTACION.md                # Documentación técnica detallada
│
├── controllers/                    # Controladores (Lógica de negocio)
│   ├── __init__.py
│   ├── main_controller.py         # Controlador principal
│   ├── equipo_controller.py       # Gestión de equipos
│   ├── participante_controller.py # Gestión de participantes
│   ├── calendario_controller.py   # Gestión de calendario
│   ├── enfrentamiento_controller.py # Creación de partidos
│   ├── eventos_partido_controller.py # Eventos en tiempo real
│   ├── listado_equipos_controller.py # Listados y estadísticas
│   ├── listado_participantes_controller.py # Edición de participantes
│   ├── informes_controller.py     # Generación de informes PDF
│   ├── creditos_controller.py     # Ventana "Acerca de"
│   └── guia_controller.py         # Visualizador de manual
│
├── models/                         # Modelos (Acceso a datos)
│   ├── __init__.py
│   └── db_manager.py              # Gestor de base de datos SQLite
│
├── views/                          # Vistas
│   ├── __init__.py
│   ├── registro_equipos_view.py   # Vista personalizada equipos
│   └── ui/                        # Interfaces Qt Designer
│       ├── __init__.py
│       ├── MainWindow.ui          # Ventana principal (diseño)
│       ├── MainWindow_ui.py       # Ventana principal (código)
│       ├── registro_equipos.ui
│       ├── registro_equipos_ui.py
│       ├── registro_participantes.ui
│       ├── registro_participantes_ui.py
│       ├── calendario.ui
│       ├── calendario_ui.py
│       ├── enfrentamiento.ui
│       ├── enfrentamiento_ui.py
│       ├── eventos_partido.ui
│       ├── eventos_partido_ui.py
│       ├── listado_equipos.ui
│       ├── listado_equipos_ui.py
│       ├── listado_participantes.ui
│       ├── listado_participantes_ui.py
│       ├── creditos.ui
│       └── creditos_ui.py
│
├── resources/                      # Recursos del proyecto
│   ├── documentacion/             # Documentación
│   │   ├── manual.html           # Manual en HTML
│   │   └── Manual de uso de aplicación.pdf # Manual PDF
│   ├── iconos/                    # Iconos de la aplicación
│   │   └── __init__.py
│   ├── img/                       # Imágenes y recursos gráficos
│   │   └── __init__.py
│   └── qss/                       # Hojas de estilo Qt
│       ├── __init__.py
│       └── style.qss             # Hoja de estilos principal
│
├── reports/                        # Plantillas y recursos de informes
│   ├── equipos_jugadores.jrxml    # Informe de equipos y jugadores
│   ├── partidos.jrxml             # Informe de partidos y resultados
│   ├── clasificacion.jrxml        # Informe de clasificación y eliminatorias
│   └── sqlite-jdbc.jar            # Driver JDBC para conexión SQLite→Jasper
│
└── imagenes/                       # Recursos Qt compilados
    ├── __init__.py
    ├── recursos.qrc               # Archivo de recursos Qt
    └── recursos_rc.py             # Recursos compilados
```

## 🎨 Iconos Recomendados

Puedes descargar iconos gratuitos de:
- **Lucide Icons**: https://lucide.dev/ (recomendado)
- **Heroicons**: https://heroicons.com/
- **Font Awesome**: https://fontawesome.com/

### Iconos necesarios para el proyecto:

| Función | Nombre archivo | Descripción |
|---------|---------------|-------------|
| Guardar | `save.png` | Icono de diskette/guardar |
| Limpiar | `clean.png` | Icono de escoba/limpiar |
| Agregar jugador | `add-user.png` | Icono de usuario con + |
| Eliminar jugador | `remove-user.png` | Icono de usuario con X |
| Subir imagen | `upload.png` | Icono de flecha hacia arriba |
| Fútbol | `football.png` | Icono de balón de fútbol |
| Editar | `edit.png` | Icono de lápiz |
| Eliminar | `delete.png` | Icono de papelera |
| Calendario | `calendar.png` | Icono de calendario |
| Trofeo | `trophy.png` | Icono de trofeo |

## 🚀 Instalación

### Prerrequisitos

1. **Python 3.8 o superior**
   ```bash
   python --version
   ```

2. **MySQL 8.0 o superior**
   - Descargar desde: https://dev.mysql.com/downloads/

3. **Git** (opcional)
   ```bash
   git --version
   ```

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <url-repositorio>
   cd torneo_futbol
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

   Contenido de `requirements.txt`:
   ```
   PySide6>=6.10.0
   pyreportjasper>=2.2.0
   ```

   > **Requisito adicional**: Java 8 o superior debe estar instalado y accesible en el PATH para que JasperReports funcione.

5. **Verificar base de datos**
   - El archivo `torneo_futbol.db` (SQLite) se crea automáticamente en la raíz del proyecto al iniciar la aplicación.
   - El driver JDBC `sqlite-jdbc.jar` debe estar en la carpeta `reports/` para la generación de informes.

6. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

## 📖 Uso Básico

### Primer Uso

1. **Registrar Equipos**: Menú `Nuevo → Registrar Equipo`
   - Completar nombre, curso, color
   - Cargar escudo y equipación
   
2. **Registrar Participantes**: Menú `Nuevo → Registrar Participante`
   - Ingresar datos personales
   - Seleccionar tipo (Jugador/Árbitro)
   - Asignar a equipo (si es jugador)

3. **Crear Enfrentamientos**: Menú `Gestión de torneo → Crear Partido`
   - Seleccionar fase (Octavos, Cuartos, etc.)
   - Asignar equipos y árbitro
   - Establecer fecha

4. **Iniciar Partido**: Menú `Gestión de torneo → Iniciar Partido`
   - Seleccionar partido
   - Registrar eventos (goles, tarjetas, etc.)
   - Finalizar partido (el ganador avanza automáticamente)

### Funcionalidades Avanzadas

- **Editar Participantes**: `Listados → Participantes` → Doble clic en registro
- **Ver Estadísticas**: Visualización automática en listados
- **Consultar Calendario**: `Listados → Calendario`
- **Exportar Manual**: `Ayuda → Guía` → Botón "Abrir Manual en PDF"

### Generación de Informes PDF

1. Acceder a `Informes → Generar Informe`
2. Seleccionar el tipo de informe en el desplegable:
   - **Equipos y Jugadores**: Lista de equipos con sus jugadores. Permite filtrar por equipo.
   - **Partidos y resultados**: Resultados y datos de cada partido. Permite filtrar por fase.
   - **Clasificación y Eliminatorias**: Estadísticas globales del torneo y cuadro de honor. Permite filtrar por fase.
3. Aplicar filtros opcionales (equipo o fase según el informe)
4. Seleccionar la carpeta de destino
5. Pulsar **Generar Informe PDF**

## 📦 Distribución (Crear .exe)

### Para Windows

```bash
pyinstaller --name="TorneoFutbol" ^
    --windowed ^
    --onefile ^
    --icon="resources/iconos/football.ico" ^
    --add-data "resources;resources" ^
    --add-data "reports;reports" ^
    main.py
```

> Los archivos `.jrxml` y `sqlite-jdbc.jar` deben incluirse en la carpeta `reports/` junto al ejecutable para que la generación de informes funcione correctamente.

### Para Linux

```bash
pyinstaller --name="torneoFutbol" \
    --windowed \
    --onefile \
    --icon="resources/iconos/football.png" \
    --add-data "resources:resources" \
    --add-data "reports:reports" \
    main.py
```

## 🎨 Personalización

### Modificar Estilos

Los estilos se encuentran en `resources/qss/style.qss`:

```css
/* Ejemplo: Cambiar color de botones */
QPushButton {
    background-color: #FF9501;
    color: #267E7E;
    border-radius: 10px;
}
```

### Colores del Tema Actual

- **Fondo principal**: rgb(94, 207, 207) `#5ECFCF`
- **Fondo secundario**: rgb(27, 90, 90) `#1B5A5A`
- **Acento naranja**: rgb(255, 149, 1) `#FF9501`
- **Texto principal**: rgb(38, 126, 126) `#267E7E`
- **Blanco**: rgb(255, 255, 255) `#FFFFFF`

### Regenerar Interfaces desde Qt Designer

```bash
# Convertir .ui a .py
pyside6-uic views/ui/MainWindow.ui -o views/ui/MainWindow_ui.py

# Compilar recursos
pyside6-rcc imagenes/recursos.qrc -o imagenes/recursos_rc.py
```

## �️ Base de Datos

### Estructura Principal

- **equipos**: Información de equipos (nombre, color, escudo, equipación)
- **participantes**: Jugadores y árbitros (datos personales, foto, tipo)
- **partidos**: Enfrentamientos (equipos, fase, fecha, árbitro, resultado, ganador)
- **estadisticas**: Eventos por participante y partido (goles, asistencias, tarjetas, etc.)

### Diagrama de Relaciones

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

### Script SQL Completo

```sql
-- Tabla de equipos
CREATE TABLE equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    curso VARCHAR(50),
    color VARCHAR(50),
    escudo VARCHAR(255),
    equipacion VARCHAR(255),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de participantes
CREATE TABLE participantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    curso VARCHAR(50),
    fecha_nacimiento DATE,
    posicion VARCHAR(50),
    es_jugador BOOLEAN DEFAULT TRUE,
    es_arbitro BOOLEAN DEFAULT FALSE,
    foto VARCHAR(255),
    equipo_id INT,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
);

-- Tabla de partidos
CREATE TABLE partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo1_id INT NOT NULL,
    equipo2_id INT NOT NULL,
    fase VARCHAR(50) NOT NULL,
    fecha_hora DATETIME,
    arbitro_id INT,
    ganador_id INT,
    finalizado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (equipo1_id) REFERENCES equipos(id),
    FOREIGN KEY (equipo2_id) REFERENCES equipos(id),
    FOREIGN KEY (arbitro_id) REFERENCES participantes(id),
    FOREIGN KEY (ganador_id) REFERENCES equipos(id)
);

-- Tabla de estadísticas
CREATE TABLE estadisticas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    participante_id INT NOT NULL,
    partido_id INT NOT NULL,
    goles INT DEFAULT 0,
    asistencias INT DEFAULT 0,
    faltas INT DEFAULT 0,
    amarillas INT DEFAULT 0,
    rojas INT DEFAULT 0,
    paradas INT DEFAULT 0,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
);
```

## 🐛 Solución de Problemas

### Error: "No module named 'PySide6'"
```bash
pip install PySide6
```

### Error: "No se puede abrir la base de datos"
Verifica que el archivo `torneo_futbol.db` existe en la raíz del proyecto

### Error al generar informe PDF: "input file ... is not a valid jrxml file"
- Asegúrate de que los archivos `.jrxml` en `reports/` son compatibles con JasperReports 6.x
- Verifica que `sqlite-jdbc.jar` está en la carpeta `reports/`

### Error al generar informe PDF: "java not found" / proceso no inicia
- Instala Java 8 o superior y añádelo al PATH del sistema

### Los iconos no se muestran
- Verifica que las rutas a los iconos sean correctas
- Asegúrate de que los archivos `.png` existen en `resources/iconos/`

### Los estilos QSS no se aplican
- Verifica que el archivo `style.qss` existe en `resources/qss/`
- Comprueba que no hay errores de sintaxis en el archivo QSS

## 🧪 Desarrollo

### Ejecutar en Modo Desarrollo

```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows

# Ejecutar aplicación
python main.py
```

### Buenas Prácticas Implementadas

- ✅ Arquitectura MVC separada
- ✅ Clases con responsabilidad única
- ✅ Gestión centralizada de base de datos
- ✅ Manejo de errores con try-except
- ✅ Validación de datos de entrada
- ✅ Confirmaciones para acciones destructivas
- ✅ Retroalimentación visual al usuario
- ✅ Código documentado con docstrings
- ✅ Generación de informes PDF con JasperReports

### Características Técnicas

- 🎨 Tema visual con colores corporativos
- 📱 Interfaz responsive y moderna
- 🖼️ Soporte para carga de imágenes (escudos, fotos, equipaciones)
- ⚡ Feedback visual en todas las acciones
- 🔔 Notificaciones al usuario (QMessageBox)
- 📊 Generación automática de estadísticas
- 🔄 Avance automático entre fases
- � Informes PDF con filtrado por equipo/fase via JasperReports
- �📖 Manual de usuario integrado

## 👨‍💻 Autor

**Boris Baldominos González**
- Curso: DAM 2 - 2º 25-26
- Módulo: Desarrollo de Interfaces (DI)
- Año: 2026

## 📄 Licencia

Este proyecto es de uso educativo. Desarrollado como parte del módulo de Desarrollo de Interfaces del ciclo de Desarrollo de Aplicaciones Multiplataforma.

## 🙏 Agradecimientos

- Documentación basada en las guías de [Héctor Costa (Hektor Profe)](https://hektorprofe.github.io/qt-pyside/)
- Framework [Qt/PySide](https://www.qt.io/qt-for-python)
- Comunidad de desarrolladores Qt

## 📚 Documentación Adicional

Para más información técnica, consultar:
- [DOCUMENTACION.md](DOCUMENTACION.md) - Documentación técnica completa
- [Manual de Usuario](resources/documentacion/Manual%20de%20uso%20de%20aplicación.pdf) - Manual en PDF

---

**¡Disfruta gestionando tu torneo de fútbol! ⚽🏆**