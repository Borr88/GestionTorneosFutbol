"""
Módulo de gestión de base de datos para el sistema de torneos (Versión SQLite).
Autor: Boris Baldominos González
Fecha: 2025-2026
"""

import sqlite3
import os
import sys
from pathlib import Path

# Determinar la ruta base (funciona tanto en desarrollo como en ejecutable)
if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).resolve().parent.parent

class DatabaseManager:
    def __init__(self):
        # La base de datos será un archivo local en la raíz del proyecto
        self.db_path = base_path / 'torneo_futbol.db'
        print(f"Base de datos SQLite en: {self.db_path}")
        
        try:
            self.init_db()
            print("Base de datos inicializada correctamente")
        except Exception as e:
            print(f"ERROR al inicializar la base de datos: {e}")

    def get_connection(self):
        """Crea y retorna una conexión a la base de datos SQLite."""
        try:
            conn = sqlite3.connect(self.db_path)
            # Habilitar el soporte para Foreign Keys en SQLite
            conn.execute("PRAGMA foreign_keys = ON")
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar a SQLite: {e}")
            return None

    def init_db(self):
        """Crea las tablas del sistema si no existen."""
        conn = self.get_connection()
        if not conn: return
        
        try:
            cursor = conn.cursor()
            
            # Tabla Equipos 
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS equipos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    curso TEXT NOT NULL,
                    color TEXT NOT NULL,
                    escudo_path TEXT,
                    equipacion_path TEXT
                )
            ''')

            # Tabla Participantes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS participantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    fecha_nacimiento DATE,
                    curso TEXT,
                    posicion TEXT,
                    es_jugador INTEGER DEFAULT 1,
                    es_arbitro INTEGER DEFAULT 0,
                    foto_path TEXT,
                    equipo_id INTEGER,
                    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
                )
            ''')

            # Tabla Partidos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS partidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    equipo_local_id INTEGER,
                    equipo_visitante_id INTEGER,
                    arbitro_id INTEGER,
                    fecha_hora DATETIME,
                    fase TEXT,
                    goles_local INTEGER DEFAULT 0,
                    goles_visitante INTEGER DEFAULT 0,
                    finalizado INTEGER DEFAULT 0,
                    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id) ON DELETE CASCADE,
                    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id) ON DELETE CASCADE,
                    FOREIGN KEY (arbitro_id) REFERENCES participantes(id) ON DELETE SET NULL
                )
            ''')
            
            # Agregar columna 'finalizado' si no existe (migración para SQLite)
            cursor.execute("PRAGMA table_info(partidos)")
            columnas = [col[1] for col in cursor.fetchall()]
            if 'finalizado' not in columnas:
                cursor.execute('ALTER TABLE partidos ADD COLUMN finalizado INTEGER DEFAULT 0')
                print("Columna 'finalizado' agregada a la tabla partidos")

            # Tabla Estadísticas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estadisticas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    participante_id INTEGER,
                    partido_id INTEGER,
                    goles INTEGER DEFAULT 0,
                    asistencias INTEGER DEFAULT 0,
                    faltas INTEGER DEFAULT 0,
                    amarillas INTEGER DEFAULT 0,
                    rojas INTEGER DEFAULT 0,
                    paradas INTEGER DEFAULT 0,
                    FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
                    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
                )
            ''')
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            conn.close()

# --- MÉTODOS CRUD (Con ? en lugar de %s) ---

    def insertar_equipo(self, nombre, curso, color, escudo_path, equipacion_path):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO equipos (nombre, curso, color, escudo_path, equipacion_path)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, curso, color, escudo_path, equipacion_path))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def insertar_participante(self, nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO participantes (
                    nombre, apellido, curso, fecha_nacimiento, 
                    posicion, es_jugador, es_arbitro, foto_path, equipo_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def obtener_equipos(self):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre FROM equipos ORDER BY nombre ASC")
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_participantes_por_equipo(self, equipo_id):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido, curso, posicion, es_jugador, es_arbitro 
                FROM participantes WHERE equipo_id = ?
            """, (equipo_id,))
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_ultimo_equipo_id(self):
        conn = self.get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM equipos")
            result = cursor.fetchone()
            return result[0] if result[0] else None
        finally:
            conn.close()

    def eliminar_equipo(self, equipo_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE participantes SET equipo_id = NULL WHERE equipo_id = ?", (equipo_id,))
            cursor.execute("DELETE FROM equipos WHERE id = ?", (equipo_id,))
            conn.commit()
            return True
        finally:
            conn.close()

    def actualizar_equipo(self, equipo_id, nombre, curso, color, escudo_path, equipacion_path):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE equipos SET nombre = ?, curso = ?, color = ?, escudo_path = ?, equipacion_path = ?
                WHERE id = ?
            ''', (nombre, curso, color, escudo_path, equipacion_path, equipo_id))
            conn.commit()
            return True
        finally:
            conn.close()

    def obtener_equipo_por_id(self, equipo_id):
        conn = self.get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, curso, color, escudo_path, equipacion_path FROM equipos WHERE id = ?", (equipo_id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def obtener_equipos_con_estadisticas(self, filtro_curso=None, filtro_nombre=None):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    e.id, e.nombre, e.curso,
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
                query += " AND e.curso = ?"
                params.append(filtro_curso)
            if filtro_nombre:
                query += " AND e.nombre LIKE ?"
                params.append(f"%{filtro_nombre}%")
                
            query += " GROUP BY e.id ORDER BY e.nombre"
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            conn.close()

    def eliminar_participante(self, participante_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estadisticas WHERE participante_id = ?", (participante_id,))
            cursor.execute("DELETE FROM participantes WHERE id = ?", (participante_id,))
            conn.commit()
            return True
        finally:
            conn.close()

    def actualizar_participante(self, participante_id, nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE participantes 
                SET nombre = ?, apellido = ?, curso = ?, fecha_nacimiento = ?,
                    posicion = ?, es_jugador = ?, es_arbitro = ?, foto_path = ?, equipo_id = ?
                WHERE id = ?
            ''', (nombre, apellido, curso, fecha_nacimiento, posicion, es_jugador, es_arbitro, foto_path, equipo_id, participante_id))
            conn.commit()
            return True
        finally:
            conn.close()

    def obtener_participante_por_id(self, participante_id):
        conn = self.get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, apellido, fecha_nacimiento, curso, posicion, es_jugador, es_arbitro, foto_path, equipo_id FROM participantes WHERE id = ?", (participante_id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def obtener_participantes_con_estadisticas(self, filtro_curso=None, filtro_nombre=None, filtro_equipo=None, filtro_tipo=None):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    p.id, p.nombre, p.apellido,
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
                query += " AND p.curso = ?"
                params.append(filtro_curso)
            if filtro_nombre:
                query += " AND (p.nombre LIKE ? OR p.apellido LIKE ?)"
                params.append(f"%{filtro_nombre}%")
                params.append(f"%{filtro_nombre}%")
            if filtro_equipo and filtro_equipo != "Seleccionar Equipo":
                query += " AND e.nombre = ?"
                params.append(filtro_equipo)
            if filtro_tipo:
                if filtro_tipo == "Jugador":
                    query += " AND p.es_jugador = 1"
                elif filtro_tipo == "Árbitro":
                    query += " AND p.es_arbitro = 1"
                    
            query += " GROUP BY p.id ORDER BY p.apellido, p.nombre"
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_estadisticas_participante(self, participante_id):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT est.goles, est.asistencias, est.faltas, est.amarillas, est.rojas, est.paradas, part.fecha_hora
                FROM estadisticas est
                INNER JOIN partidos part ON est.partido_id = part.id
                WHERE est.participante_id = ? ORDER BY part.fecha_hora DESC
            """, (participante_id,))
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_resumen_estadisticas_participante(self, participante_id):
        conn = self.get_connection()
        if not conn: return None
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
                FROM estadisticas WHERE participante_id = ?
            """, (participante_id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def insertar_partido(self, equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase="Octavos"):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante)
                VALUES (?, ?, ?, ?, ?, 0, 0)
            ''', (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase))
            conn.commit()
            return True
        finally:
            conn.close()

    def obtener_arbitros_disponibles(self, fecha):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre, apellido FROM participantes
                WHERE es_arbitro = 1 AND id NOT IN (
                    SELECT arbitro_id FROM partidos 
                    WHERE DATE(fecha_hora) = DATE(?) AND arbitro_id IS NOT NULL
                ) ORDER BY apellido, nombre
            """, (fecha,))
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_todos_los_arbitros(self):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, apellido FROM participantes WHERE es_arbitro = 1 ORDER BY apellido, nombre")
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_partidos_por_fase(self, fase=None):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            query = """
                SELECT p.id, el.nombre as equipo_local, ev.nombre as equipo_visitante, 
                       p.fecha_hora, p.fase, p.goles_local, p.goles_visitante
                FROM partidos p
                LEFT JOIN equipos el ON p.equipo_local_id = el.id
                LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
            """
            if fase and fase != "Selección Fase":
                query += " WHERE p.fase = ? ORDER BY p.id"
                cursor.execute(query, (fase,))
            else:
                query += " ORDER BY p.id"
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_partidos_no_finalizados(self):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, el.nombre as equipo_local, ev.nombre as equipo_visitante, 
                       p.fecha_hora, p.fase, p.goles_local, p.goles_visitante
                FROM partidos p
                LEFT JOIN equipos el ON p.equipo_local_id = el.id
                LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                WHERE p.finalizado = 0 AND p.fecha_hora IS NOT NULL
                ORDER BY p.fecha_hora, p.id
            """)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def marcar_partido_finalizado(self, partido_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE partidos SET finalizado = 1 WHERE id = ?", (partido_id,))
            conn.commit()
            return True
        finally:
            conn.close()

    def actualizar_fecha_partido(self, partido_id, fecha_hora):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE partidos SET fecha_hora = ? WHERE id = ?", (fecha_hora, partido_id))
            conn.commit()
            return True
        finally:
            conn.close()

    def obtener_partido_por_id(self, partido_id):
        conn = self.get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, p.equipo_local_id, p.equipo_visitante_id, el.nombre as equipo_local, 
                       ev.nombre as equipo_visitante, p.arbitro_id, p.fecha_hora, p.fase, p.goles_local, p.goles_visitante
                FROM partidos p
                LEFT JOIN equipos el ON p.equipo_local_id = el.id
                LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
                WHERE p.id = ?
            """, (partido_id,))
            return cursor.fetchone()
        finally:
            conn.close()

    def obtener_jugadores_por_equipo(self, equipo_id):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, apellido FROM participantes WHERE equipo_id = ? AND es_jugador = 1 ORDER BY apellido, nombre", (equipo_id,))
            return cursor.fetchall()
        finally:
            conn.close()

    def insertar_estadistica(self, participante_id, partido_id, goles=0, asistencias=0, faltas=0, amarillas=0, rojas=0, paradas=0):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM estadisticas WHERE participante_id = ? AND partido_id = ?", (participante_id, partido_id))
            existente = cursor.fetchone()
            
            if existente:
                cursor.execute("""
                    UPDATE estadisticas
                    SET goles = goles + ?, asistencias = asistencias + ?, faltas = faltas + ?,
                        amarillas = amarillas + ?, rojas = rojas + ?, paradas = paradas + ?
                    WHERE id = ?
                """, (goles, asistencias, faltas, amarillas, rojas, paradas, existente[0]))
            else:
                cursor.execute("""
                    INSERT INTO estadisticas (participante_id, partido_id, goles, asistencias, faltas, amarillas, rojas, paradas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (participante_id, partido_id, goles, asistencias, faltas, amarillas, rojas, paradas))
            conn.commit()
            return True
        finally:
            conn.close()

    def obtener_estadisticas_por_partido(self, partido_id, equipo_id):
        conn = self.get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.nombre, p.apellido, est.goles, est.asistencias, est.faltas, est.amarillas, est.rojas, est.paradas
                FROM estadisticas est
                INNER JOIN participantes p ON est.participante_id = p.id
                WHERE est.partido_id = ? AND p.equipo_id = ?
            """, (partido_id, equipo_id))
            return cursor.fetchall()
        finally:
            conn.close()

    def actualizar_goles_partido(self, partido_id, goles_local, goles_visitante):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE partidos SET goles_local = ?, goles_visitante = ? WHERE id = ?", (goles_local, goles_visitante, partido_id))
            conn.commit()
            return True
        finally:
            conn.close()

    def avanzar_equipo_siguiente_fase(self, equipo_ganador_id, fase_actual, partido_id):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            fases = {"Octavos": "Cuartos", "Cuartos": "Semifinales", "Semifinales": "Final"}
            siguiente_fase = fases.get(fase_actual)
            if not siguiente_fase: return True
            
            cursor.execute("SELECT id FROM partidos WHERE fase = ? ORDER BY id", (fase_actual,))
            ids_fase = [row[0] for row in cursor.fetchall()]
            
            try:
                posicion_partido = ids_fase.index(partido_id)
            except ValueError:
                return False
                
            partido_destino = posicion_partido // 2
            es_local = (posicion_partido % 2 == 0)
            
            cursor.execute("SELECT id, equipo_local_id, equipo_visitante_id FROM partidos WHERE fase = ? ORDER BY id", (siguiente_fase,))
            partidos_siguiente = cursor.fetchall()
            
            if partido_destino < len(partidos_siguiente):
                partido_siguiente = partidos_siguiente[partido_destino]
                if es_local:
                    cursor.execute("UPDATE partidos SET equipo_local_id = ? WHERE id = ?", (equipo_ganador_id, partido_siguiente[0]))
                else:
                    cursor.execute("UPDATE partidos SET equipo_visitante_id = ? WHERE id = ?", (equipo_ganador_id, partido_siguiente[0]))
            else:
                while len(partidos_siguiente) <= partido_destino:
                    if len(partidos_siguiente) == partido_destino and es_local:
                        cursor.execute("INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado) VALUES (?, NULL, NULL, NULL, ?, 0, 0, 0)", (equipo_ganador_id, siguiente_fase))
                    elif len(partidos_siguiente) == partido_destino and not es_local:
                        cursor.execute("INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado) VALUES (NULL, ?, NULL, NULL, ?, 0, 0, 0)", (equipo_ganador_id, siguiente_fase))
                    else:
                        cursor.execute("INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha_hora, fase, goles_local, goles_visitante, finalizado) VALUES (NULL, NULL, NULL, NULL, ?, 0, 0, 0)", (siguiente_fase,))
                    partidos_siguiente.append((cursor.lastrowid, None, None))
            
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al avanzar equipo: {e}")
            return False
        finally:
            conn.close()