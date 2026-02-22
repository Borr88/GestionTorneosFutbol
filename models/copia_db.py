"""
Módulo de gestión de base de datos para el sistema de torneos.

Este módulo proporciona la clase DatabaseManager que maneja todas las 
operaciones con la base de datos MySQL, incluyendo:
- Gestión de equipos
- Gestión de participantes
- Gestión de partidos y calendarios
- Cálculo de estadísticas
- Avance de equipos en el torneo

Tablas de la base de datos:
- equipos: Información de los equipos participantes
- participantes: Jugadores asociados a equipos
- partidos: Enfrentamientos entre equipos
- estadisticas: Registro de eventos en cada partido

Autor: Boris Baldominos González
Fecha: 2025-2026
"""

import mysql.connector
from mysql.connector import Error
import os
import sys
from pathlib import Path

# Determinar la ruta base (funciona tanto en desarrollo como en ejecutable)
if getattr(sys, 'frozen', False):
    # Si está ejecutándose como ejecutable de PyInstaller
    base_path = Path(sys._MEIPASS)
    print(f"Ejecutando desde ejecutable. Base path: {base_path}")
else:
    # Si está ejecutándose como script normal
    base_path = Path(__file__).resolve().parent.parent
    print(f"Ejecutando desde script. Base path: {base_path}")

# Intentar cargar python-dotenv si está disponible
try:
    from dotenv import load_dotenv
    # Cargar variables del archivo .env desde la ubicación correcta
    env_path = base_path / '.env'
    print(f"Buscando archivo .env en: {env_path}")
    if env_path.exists():
        load_dotenv(env_path)
        print("Archivo .env cargado correctamente")
    else:
        print(f"Archivo .env no encontrado en {env_path}")
        # Intentar cargar desde el directorio actual
        load_dotenv()
except ImportError:
    print("python-dotenv no disponible, usando variables de entorno del sistema")

class DatabaseManager:
    """
    Gestor centralizado de base de datos MySQL para el torneo.
    
    Esta clase implementa el patrón Singleton para gestionar la conexión
    con MySQL y proporciona métodos para todas las operaciones CRUD sobre
    equipos, participantes, partidos y estadísticas.
    
    Attributes:
        host (str): Host del servidor MySQL
        port (str): Puerto de conexión
        user (str): Usuario de la base de datos
        password (str): Contraseña del usuario
        database (str): Nombre de la base de datos
    """
    def __init__(self):
        """
        Inicializa el gestor de base de datos.
        
        Carga las credenciales desde el archivo .env, crea la base de datos
        si no existe y inicializa las tablas necesarias.
        """
        # Cargar credenciales desde variables de entorno
        self.host = os.getenv('DB_HOST', '127.0.0.1')
        self.port = os.getenv('DB_PORT', '3306')
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_NAME', 'torneo_futbol')
        
        # Mostrar configuración para debug
        print(f"Configuración de BD:")
        print(f"  Host: {self.host}")
        print(f"  Puerto: {self.port}")
        print(f"  Usuario: {self.user}")
        print(f"  Base de datos: {self.database}")
        
        # Intentar crear la base de datos y las tablas
        try:
            self._crear_base_datos()
            self.init_db()
            print("Base de datos inicializada correctamente")
        except Exception as e:
            print(f"ERROR al inicializar la base de datos: {e}")
            print("Verifica que MySQL esté ejecutándose en XAMPP")

    def _crear_base_datos(self):
        """
        Crea la base de datos si no existe.
        
        Conecta al servidor MySQL y ejecuta CREATE DATABASE IF NOT EXISTS
        para garantizar que la base de datos esté disponible.
        """
        try:
            print("Intentando conectar al servidor MySQL...")
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                use_pure=True  # Usar conector Python puro para evitar problemas con PyInstaller
            )
            print("Conexión a MySQL establecida")
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Base de datos '{self.database}' verificada/creada correctamente")
            cursor.close()
            connection.close()
        except Error as e:
            print(f"Error al crear base de datos: {e}")
            raise

    def get_connection(self):
        """
        Crea y retorna una conexión a la base de datos MySQL.
        
        Returns:
            mysql.connector.connection.MySQLConnection: Objeto de conexión activa
            None: Si ocurre un error de conexión
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                use_pure=True  # Usar conector Python puro para evitar problemas con PyInstaller
            )
            return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    def init_db(self):
        """
        Crea las tablas del sistema si no existen.
        
        Crea las siguientes tablas:
        - equipos: id, nombre_equipo, tutor
        - participantes: id, nombre, apellido, edad, id_equipo
        - partidos: id, id_equipo1, id_equipo2, fecha, ganador, fase
        - estadisticas: id_participante, id_partido, goles, asistencias, etc.
        """
        conn = self.get_connection()
        if not conn:
            print("No se pudo conectar a la base de datos para crear las tablas")
            return
        
        try:
            cursor = conn.cursor()
            
            # Tabla Equipos 
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS equipos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    curso VARCHAR(100) NOT NULL,
                    color VARCHAR(100) NOT NULL,
                    escudo_path VARCHAR(500),
                    equipacion_path VARCHAR(500)
                )
            ''')

            # Tabla Participantes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS participantes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    apellido VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE,
                    curso VARCHAR(100),
                    posicion VARCHAR(100),
                    es_jugador TINYINT(1) DEFAULT 1,
                    es_arbitro TINYINT(1) DEFAULT 0,
                    foto_path VARCHAR(500),
                    equipo_id INT,
                    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
                )
            ''')

            # Tabla Partidos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS partidos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    equipo_local_id INT,
                    equipo_visitante_id INT,
                    arbitro_id INT,
                    fecha_hora DATETIME,
                    fase VARCHAR(50),
                    goles_local INT DEFAULT 0,
                    goles_visitante INT DEFAULT 0,
                    finalizado TINYINT(1) DEFAULT 0,
                    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id) ON DELETE CASCADE,
                    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id) ON DELETE CASCADE,
                    FOREIGN KEY (arbitro_id) REFERENCES participantes(id) ON DELETE SET NULL
                )
            ''')
            
            # Agregar columna 'finalizado' si no existe (migración)
            cursor.execute('''
                SELECT COUNT(*) 
                FROM information_schema.COLUMNS 
                WHERE TABLE_SCHEMA = %s 
                AND TABLE_NAME = 'partidos' 
                AND COLUMN_NAME = 'finalizado'
            ''', (self.database,))
            
            if cursor.fetchone()[0] == 0:
                cursor.execute('ALTER TABLE partidos ADD COLUMN finalizado TINYINT(1) DEFAULT 0')
                print("Columna 'finalizado' agregada a la tabla partidos")

            # Tabla Estadísticas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estadisticas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    participante_id INT,
                    partido_id INT,
                    goles INT DEFAULT 0,
                    asistencias INT DEFAULT 0,
                    faltas INT DEFAULT 0,
                    amarillas INT DEFAULT 0,
                    rojas INT DEFAULT 0,
                    paradas INT DEFAULT 0,
                    FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
                    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
                )
            ''')
            
            conn.commit()
            print("Base de datos inicializada correctamente")
        except Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    

# REGISTRAR EQUIPO --------------------------------------------

    def insertar_equipo(self, nombre, curso, color, escudo_path, equipacion_path):
        """Inserta un nuevo equipo y devuelve True si tuvo éxito"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO equipos (nombre, curso, color, escudo_path, equipacion_path)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nombre, curso, color, escudo_path, equipacion_path))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al insertar equipo: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        

 # REGISTRAR PARTICIPANTE --------------------------------------

    def insertar_participante(self, nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id):
        """Inserta un nuevo participante respetando la dualidad de roles"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO participantes (
                    nombre, apellido, curso, fecha_nacimiento, 
                    posicion, es_jugador, es_arbitro, foto_path, equipo_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al insertar participante: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        

# OBTENER EQUIPO ----------------------------------------------

    def obtener_equipos(self):
        """Devuelve una lista de tuplas (id, nombre) de todos los equipos """
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre FROM equipos ORDER BY nombre ASC")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener equipos: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        
# OBTENER PARTICIPANTES POR EQUIPO ----------------------------

    def obtener_participantes_por_equipo(self, equipo_id):
        """Consulta los jugadores que pertenecen a un equipo específico"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido, curso, posicion, es_jugador, es_arbitro 
                FROM participantes 
                WHERE equipo_id = %s
            """, (equipo_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener participantes del equipo: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER ÚLTIMO EQUIPO INSERTADO ----------------------------
    
    def obtener_ultimo_equipo_id(self):
        """Devuelve el ID del último equipo insertado"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM equipos")
            result = cursor.fetchone()
            return result[0] if result[0] else None
        except Error as e:
            print(f"Error al obtener último equipo: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ELIMINAR EQUIPO ---------------------------------------------

    def eliminar_equipo(self, equipo_id):
        """Elimina un equipo y sus participantes asociados"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            # Primero actualizar los participantes para quitar la referencia
            cursor.execute("UPDATE participantes SET equipo_id = NULL WHERE equipo_id = %s", (equipo_id,))
            # Luego eliminar el equipo
            cursor.execute("DELETE FROM equipos WHERE id = %s", (equipo_id,))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al eliminar equipo: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ACTUALIZAR EQUIPO -------------------------------------------

    def actualizar_equipo(self, equipo_id, nombre, curso, color, escudo_path, equipacion_path):
        """Actualiza los datos de un equipo existente"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE equipos 
                SET nombre = %s, curso = %s, color = %s, escudo_path = %s, equipacion_path = %s
                WHERE id = %s
            ''', (nombre, curso, color, escudo_path, equipacion_path, equipo_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar equipo: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER EQUIPO POR ID ---------------------------------------

    def obtener_equipo_por_id(self, equipo_id):
        """Obtiene los datos de un equipo específico"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, curso, color, escudo_path, equipacion_path 
                FROM equipos 
                WHERE id = %s
            """, (equipo_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener equipo: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER TODOS LOS EQUIPOS CON ESTADÍSTICAS -----------------

    def obtener_equipos_con_estadisticas(self, filtro_curso=None, filtro_nombre=None):
        """Obtiene todos los equipos con sus estadísticas agregadas"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    e.id,
                    e.nombre,
                    e.curso,
                    COUNT(DISTINCT CASE 
                        WHEN (p.equipo_local_id = e.id AND p.goles_local > p.goles_visitante) OR
                             (p.equipo_visitante_id = e.id AND p.goles_visitante > p.goles_local)
                        THEN p.id 
                    END) as victorias,
                    COALESCE(SUM(est.goles), 0) as total_goles,
                    COALESCE(SUM(est.faltas), 0) as total_faltas,
                    COALESCE(SUM(est.amarillas), 0) as total_amarillas,
                    COALESCE(SUM(est.rojas), 0) as total_rojas,
                    COALESCE(SUM(est.paradas), 0) as total_paradas
                FROM equipos e
                LEFT JOIN participantes part ON part.equipo_id = e.id
                LEFT JOIN estadisticas est ON est.participante_id = part.id
                LEFT JOIN partidos p ON (p.equipo_local_id = e.id OR p.equipo_visitante_id = e.id)
                WHERE 1=1
            """
            params = []
            
            if filtro_curso and filtro_curso != "Seleccionar Curso":
                query += " AND e.curso = %s"
                params.append(filtro_curso)
                
            if filtro_nombre:
                query += " AND e.nombre LIKE %s"
                params.append(f"%{filtro_nombre}%")
                
            query += " GROUP BY e.id ORDER BY e.nombre"
            
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener equipos con estadísticas: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ELIMINAR PARTICIPANTE ---------------------------------------

    def eliminar_participante(self, participante_id):
        """Elimina un participante y sus estadísticas asociadas"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            # Primero eliminar estadísticas
            cursor.execute("DELETE FROM estadisticas WHERE participante_id = %s", (participante_id,))
            # Luego eliminar participante
            cursor.execute("DELETE FROM participantes WHERE id = %s", (participante_id,))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al eliminar participante: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ACTUALIZAR PARTICIPANTE -------------------------------------

    def actualizar_participante(self, participante_id, nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id):
        """Actualiza los datos de un participante existente"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE participantes 
                SET nombre = %s, apellido = %s, curso = %s, fecha_nacimiento = %s,
                    posicion = %s, es_jugador = %s, es_arbitro = %s, foto_path = %s, equipo_id = %s
                WHERE id = %s
            ''', (nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id, participante_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar participante: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER PARTICIPANTE POR ID ---------------------------------

    def obtener_participante_por_id(self, participante_id):
        """Obtiene los datos de un participante específico"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido, fecha_nacimiento, curso, posicion, 
                       es_jugador, es_arbitro, foto_path, equipo_id
                FROM participantes 
                WHERE id = %s
            """, (participante_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener participante: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER PARTICIPANTES CON ESTADÍSTICAS ---------------------

    def obtener_participantes_con_estadisticas(self, filtro_curso=None, filtro_nombre=None, filtro_equipo=None, filtro_tipo=None):
        """Obtiene todos los participantes con sus estadísticas agregadas"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    p.id,
                    p.nombre,
                    p.apellido,
                    COALESCE(e.nombre, 'Sin equipo') as equipo,
                    p.posicion,
                    COALESCE(SUM(est.goles), 0) as total_goles,
                    COALESCE(SUM(est.asistencias), 0) as total_asistencias,
                    COALESCE(SUM(est.faltas), 0) as total_faltas,
                    COALESCE(SUM(est.amarillas), 0) as total_amarillas,
                    COALESCE(SUM(est.rojas), 0) as total_rojas,
                    COALESCE(SUM(est.paradas), 0) as total_paradas
                FROM participantes p
                LEFT JOIN equipos e ON p.equipo_id = e.id
                LEFT JOIN estadisticas est ON est.participante_id = p.id
                WHERE 1=1
            """
            params = []
            
            if filtro_curso and filtro_curso != "Seleccionar Curso":
                query += " AND p.curso = %s"
                params.append(filtro_curso)
                
            if filtro_nombre:
                query += " AND (p.nombre LIKE %s OR p.apellido LIKE %s)"
                params.append(f"%{filtro_nombre}%")
                params.append(f"%{filtro_nombre}%")
            
            if filtro_equipo and filtro_equipo != "Seleccionar Equipo":
                query += " AND e.nombre = %s"
                params.append(filtro_equipo)
            
            if filtro_tipo:
                if filtro_tipo == "Jugador":
                    query += " AND p.es_jugador = 1"
                elif filtro_tipo == "Árbitro":
                    query += " AND p.es_arbitro = 1"
                
            query += " GROUP BY p.id ORDER BY p.apellido, p.nombre"
            
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener participantes con estadísticas: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER ESTADÍSTICAS POR PARTICIPANTE -----------------------

    def obtener_estadisticas_participante(self, participante_id):
        """Obtiene el historial de estadísticas de un participante con fechas de partidos"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    est.goles,
                    est.asistencias,
                    est.faltas,
                    est.amarillas,
                    est.rojas,
                    est.paradas,
                    part.fecha_hora
                FROM estadisticas est
                INNER JOIN partidos part ON est.partido_id = part.id
                WHERE est.participante_id = %s
                ORDER BY part.fecha_hora DESC
            """, (participante_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener estadísticas del participante: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER RESUMEN ESTADÍSTICAS PARTICIPANTE -------------------

    def obtener_resumen_estadisticas_participante(self, participante_id):
        """Obtiene el resumen total de estadísticas de un participante"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    COALESCE(SUM(goles), 0) as total_goles,
                    COALESCE(SUM(asistencias), 0) as total_asistencias,
                    COALESCE(SUM(faltas), 0) as total_faltas,
                    COALESCE(SUM(amarillas), 0) as total_amarillas,
                    COALESCE(SUM(rojas), 0) as total_rojas,
                    COALESCE(SUM(paradas), 0) as total_paradas
                FROM estadisticas
                WHERE participante_id = %s
            """, (participante_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener resumen de estadísticas: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# INSERTAR PARTIDO --------------------------------------------

    def insertar_partido(self, equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase="Octavos"):
        """Inserta un nuevo partido"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante)
                VALUES (%s, %s, %s, %s, %s, 0, 0)
            ''', (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al insertar partido: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER ÁRBITROS DISPONIBLES --------------------------------

    def obtener_arbitros_disponibles(self, fecha):
        """Obtiene árbitros que no tienen partido asignado en la fecha indicada"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido
                FROM participantes
                WHERE es_arbitro = 1
                AND id NOT IN (
                    SELECT arbitro_id 
                    FROM partidos 
                    WHERE DATE(fecha_hora) = DATE(%s)
                    AND arbitro_id IS NOT NULL
                )
                ORDER BY apellido, nombre
            """, (fecha,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener árbitros disponibles: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER TODOS LOS ÁRBITROS ----------------------------------

    def obtener_todos_los_arbitros(self):
        """Obtiene todos los árbitros registrados"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido
                FROM participantes
                WHERE es_arbitro = 1
                ORDER BY apellido, nombre
            """)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener árbitros: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER PARTIDOS POR FASE -----------------------------------

    def obtener_partidos_por_fase(self, fase=None):
        """Obtiene los partidos filtrados por fase"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            if fase and fase != "Selección Fase":
                cursor.execute("""
                    SELECT 
                        p.id,
                        el.nombre as equipo_local,
                        ev.nombre as equipo_visitante,
                        p.fecha_hora,
                        p.fase,
                        p.goles_local,
                        p.goles_visitante
                    FROM partidos p
                    LEFT JOIN equipos el ON p.equipo_local_id = el.id
                    LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                    WHERE p.fase = %s
                    ORDER BY p.id
                """, (fase,))
            else:
                cursor.execute("""
                    SELECT 
                        p.id,
                        el.nombre as equipo_local,
                        ev.nombre as equipo_visitante,
                        p.fecha_hora,
                        p.fase,
                        p.goles_local,
                        p.goles_visitante
                    FROM partidos p
                    LEFT JOIN equipos el ON p.equipo_local_id = el.id
                    LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                    ORDER BY p.id
                """)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener partidos: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ACTUALIZAR FECHA PARTIDO ------------------------------------

    def obtener_partidos_no_finalizados(self):
        """Obtiene todos los partidos que no han sido finalizados y tienen fecha asignada"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    p.id,
                    el.nombre as equipo_local,
                    ev.nombre as equipo_visitante,
                    p.fecha_hora,
                    p.fase,
                    p.goles_local,
                    p.goles_visitante
                FROM partidos p
                LEFT JOIN equipos el ON p.equipo_local_id = el.id
                LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                WHERE p.finalizado = 0 
                AND p.fecha_hora IS NOT NULL
                ORDER BY p.fecha_hora, p.id
            """)
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener partidos no finalizados: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def marcar_partido_finalizado(self, partido_id):
        """Marca un partido como finalizado"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE partidos 
                SET finalizado = 1 
                WHERE id = %s
            """, (partido_id,))
            conn.commit()
            print(f"Partido {partido_id} marcado como finalizado")
            return True
        except Error as e:
            print(f"Error al marcar partido como finalizado: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ACTUALIZAR FECHA PARTIDO ------------------------------------

    def actualizar_fecha_partido(self, partido_id, fecha_hora):
        """Actualiza la fecha de un partido"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE partidos 
                SET fecha_hora = %s
                WHERE id = %s
            """, (fecha_hora, partido_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar fecha del partido: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER PARTIDO POR ID --------------------------------------

    def obtener_partido_por_id(self, partido_id):
        """Obtiene los datos completos de un partido"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    p.id,
                    p.equipo_local_id,
                    p.equipo_visitante_id,
                    el.nombre as equipo_local,
                    ev.nombre as equipo_visitante,
                    p.arbitro_id,
                    p.fecha_hora,
                    p.fase,
                    p.goles_local,
                    p.goles_visitante
                FROM partidos p
                LEFT JOIN equipos el ON p.equipo_local_id = el.id
                LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                WHERE p.id = %s
            """, (partido_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error al obtener partido: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER JUGADORES POR EQUIPO --------------------------------

    def obtener_jugadores_por_equipo(self, equipo_id):
        """Obtiene todos los jugadores de un equipo"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido
                FROM participantes
                WHERE equipo_id = %s AND es_jugador = 1
                ORDER BY apellido, nombre
            """, (equipo_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener jugadores: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# INSERTAR ESTADÍSTICA ----------------------------------------

    def insertar_estadistica(self, participante_id, partido_id, goles=0, asistencias=0, faltas=0, amarillas=0, rojas=0, paradas=0):
        """Inserta o actualiza una estadística en un partido"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            # Verificar si ya existe
            cursor.execute("""
                SELECT id FROM estadisticas 
                WHERE participante_id = %s AND partido_id = %s
            """, (participante_id, partido_id))
            
            existente = cursor.fetchone()
            
            if existente:
                # Actualizar sumando los nuevos valores
                cursor.execute("""
                    UPDATE estadisticas
                    SET goles = goles + %s,
                        asistencias = asistencias + %s,
                        faltas = faltas + %s,
                        amarillas = amarillas + %s,
                        rojas = rojas + %s,
                        paradas = paradas + %s
                    WHERE id = %s
                """, (goles, asistencias, faltas, amarillas, rojas, paradas, existente[0]))
            else:
                # Insertar nuevo
                cursor.execute("""
                    INSERT INTO estadisticas 
                    (participante_id, partido_id, goles, asistencias, faltas, amarillas, rojas, paradas)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (participante_id, partido_id, goles, asistencias, faltas, amarillas, rojas, paradas))
            
            conn.commit()
            return True
        except Error as e:
            print(f"Error al insertar estadística: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# OBTENER ESTADÍSTICAS POR PARTIDO ----------------------------

    def obtener_estadisticas_por_partido(self, partido_id, equipo_id):
        """Obtiene las estadísticas de un equipo en un partido específico"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    p.nombre,
                    p.apellido,
                    est.goles,
                    est.asistencias,
                    est.faltas,
                    est.amarillas,
                    est.rojas,
                    est.paradas
                FROM estadisticas est
                INNER JOIN participantes p ON est.participante_id = p.id
                WHERE est.partido_id = %s AND p.equipo_id = %s
            """, (partido_id, equipo_id))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener estadísticas del partido: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# ACTUALIZAR GOLES PARTIDO ------------------------------------

    def actualizar_goles_partido(self, partido_id, goles_local, goles_visitante):
        """Actualiza los goles de un partido"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE partidos
                SET goles_local = %s, goles_visitante = %s
                WHERE id = %s
            """, (goles_local, goles_visitante, partido_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar goles: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# AVANZAR EQUIPO A SIGUIENTE FASE -----------------------------

    def avanzar_equipo_siguiente_fase(self, equipo_ganador_id, fase_actual, partido_id):
        """Crea o actualiza el partido de la siguiente fase con el equipo ganador
        
        Respeta la estructura del bracket visual donde:
        - Partidos consecutivos se emparejan en la siguiente fase
        - Octavos pos 0,1 → Cuartos partido 0 | pos 2,3 → Cuartos partido 1 | etc.
        - Cuartos pos 0,1 → Semi partido 0 | pos 2,3 → Semi partido 1
        - Semi pos 0,1 → Final
        """
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            
            # Determinar la siguiente fase
            fases = {
                "Octavos": "Cuartos",
                "Cuartos": "Semifinales",
                "Semifinales": "Final"
            }
            
            siguiente_fase = fases.get(fase_actual)
            if not siguiente_fase:
                return True  # Ya está en la final
            
            # Obtener todos los partidos de la fase actual ordenados por ID
            cursor.execute("""
                SELECT id FROM partidos 
                WHERE fase = %s
                ORDER BY id
            """, (fase_actual,))
            
            ids_fase = [row[0] for row in cursor.fetchall()]
            total_partidos_fase = len(ids_fase)
            
            # Encontrar la posición del partido actual (0-based)
            try:
                posicion_partido = ids_fase.index(partido_id)
            except ValueError:
                print(f"Partido {partido_id} no encontrado en fase {fase_actual}")
                return False
            
            # Calcular el partido de destino y posición según el bracket visual
            # Los partidos consecutivos se emparejan:
            # - Octavos: pos 0,1 -> Cuartos partido 0 | pos 2,3 -> Cuartos partido 1 | etc.
            # - Cuartos: pos 0,1 -> Semi partido 0 | pos 2,3 -> Semi partido 1 | etc.
            # - Semi: pos 0,1 -> Final partido 0
            
            # Lógica estándar: partidos consecutivos se emparejan
            partido_destino = posicion_partido // 2
            es_local = (posicion_partido % 2 == 0)
            
            print(f"DEBUG: Partido ID {partido_id} en posición {posicion_partido} de {fase_actual} ({total_partidos_fase} partidos)")
            print(f"DEBUG: Avanza a partido {partido_destino} de {siguiente_fase} como {'local' if es_local else 'visitante'}")
            
            # Buscar si ya existe el partido de la siguiente fase en la posición calculada
            cursor.execute("""
                SELECT id, equipo_local_id, equipo_visitante_id 
                FROM partidos 
                WHERE fase = %s
                ORDER BY id
            """, (siguiente_fase,))
            
            partidos_siguiente = cursor.fetchall()
            print(f"DEBUG: Partidos existentes en {siguiente_fase}: {len(partidos_siguiente)}")
            
            # Verificar si ya existe el partido en la posición destino
            if partido_destino < len(partidos_siguiente):
                # Actualizar el partido existente
                partido_siguiente = partidos_siguiente[partido_destino]
                if es_local:
                    cursor.execute("""
                        UPDATE partidos 
                        SET equipo_local_id = %s
                        WHERE id = %s
                    """, (equipo_ganador_id, partido_siguiente[0]))
                else:
                    cursor.execute("""
                        UPDATE partidos 
                        SET equipo_visitante_id = %s
                        WHERE id = %s
                    """, (equipo_ganador_id, partido_siguiente[0]))
                print(f"DEBUG: Actualizado partido existente {partido_siguiente[0]}")
            else:
                # Crear nuevos partidos hasta llegar a la posición destino
                while len(partidos_siguiente) <= partido_destino:
                    if len(partidos_siguiente) == partido_destino and es_local:
                        # Este es el partido que necesitamos crear con el ganador como local
                        cursor.execute("""
                            INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado)
                            VALUES (%s, NULL, NULL, NULL, %s, 0, 0, 0)
                        """, (equipo_ganador_id, siguiente_fase))
                    elif len(partidos_siguiente) == partido_destino and not es_local:
                        # Este es el partido que necesitamos crear con el ganador como visitante
                        cursor.execute("""
                            INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado)
                            VALUES (NULL, %s, NULL, NULL, %s, 0, 0, 0)
                        """, (equipo_ganador_id, siguiente_fase))
                    else:
                        # Crear partido vacío intermedio
                        cursor.execute("""
                            INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado)
                            VALUES (NULL, NULL, NULL, NULL, %s, 0, 0, 0)
                        """, (siguiente_fase,))
                    partidos_siguiente.append((cursor.lastrowid, None, None))
                    print(f"DEBUG: Creado nuevo partido {cursor.lastrowid} en {siguiente_fase}")
            
            conn.commit()
            return True
        except Error as e:
            print(f"Error al avanzar equipo: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
