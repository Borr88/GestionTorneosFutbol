"""
Controlador principal de la aplicación Torneo de Fútbol.

Este módulo contiene el controlador MainController que gestiona:
- La ventana principal de la aplicación
- La navegación entre diferentes vistas mediante QStackedWidget
- El tablero de torneo con los emparejamientos
- La integración con todos los sub-controladores

Autor: Boris Baldominos González
Fecha: 2025-2026
"""

from PySide6.QtWidgets import QMainWindow
from models.db_manager import DatabaseManager
from views.ui.MainWindow_ui import Ui_MainWindow
from controllers.equipo_controller import EquipoController
from controllers.participante_controller import ParticipanteController
from controllers.listado_participantes_controller import ListadoParticipantesController
from controllers.listado_equipos_controller import ListadoEquiposController
from controllers.eventos_partido_controller import EventosPartidoController
from controllers.enfrentamiento_controller import EnfrentamientoController
from controllers.calendario_controller import CalendarioController
from controllers.creditos_controller import CreditosController
from controllers.guia_controller import GuiaController
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainController(QMainWindow):
    """
    Controlador principal de la aplicación de gestión de torneos.
    
    Gestiona la ventana principal, la navegación entre vistas y la 
    visualización del tablero del torneo. Coordina todos los sub-controladores
    para las diferentes funcionalidades del sistema.
    
    Attributes:
        db (DatabaseManager): Gestor de base de datos compartido
        ui (Ui_MainWindow): Interface de usuario generada desde Qt Designer
        vista_equipos (EquipoController): Controlador de registro de equipos
        vista_participantes (ParticipanteController): Controlador de participantes
        vista_listado_participantes (ListadoParticipantesController): Listado completo
        vista_listado_equipos (ListadoEquiposController): Listado de equipos
        vista_enfrentamientos (EnfrentamientoController): Gestión de partidos
        vista_calendario (CalendarioController): Calendario de eventos
        vista_eventos (EventosPartidoController): Registro de eventos en partidos
        creditos_controller (CreditosController): Vista de créditos
        guia_controller (GuiaController): Manual de usuario
    """
    def __init__(self):
        """
        Inicializa el controlador principal.
        
        Crea la interfaz, inicializa la base de datos, configura todos los
        sub-controladores y conecta las señales de los botones del menú.
        """
        super().__init__()
        self.db = DatabaseManager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # --- MANTENEMOS TU CONFIGURACIÓN DE EMOJI ---
        self.ui.label_45.setStyleSheet("font-size: 80px; background: transparent; border: none;")
        self.ui.label_45.setText("🏆")
        self.ui.label_45.setAlignment(Qt.AlignCenter)
        
        self.setWindowTitle("Torneo de Fútbol - Instituto")
        self.ui.titulo.setText("⚽ Torneo 2025-2026 ⚽")

      
        self.vista_equipos = EquipoController(self.db, self)
        self.ui.stackedWidget.addWidget(self.vista_equipos)

        self.vista_participantes = ParticipanteController(self.db, self)
        self.ui.stackedWidget.addWidget(self.vista_participantes)

        self.vista_listado_participantes = ListadoParticipantesController(self.db,self)
        self.ui.stackedWidget.addWidget(self.vista_listado_participantes)

        self.vista_listado_equipos = ListadoEquiposController(self.db,self)
        self.ui.stackedWidget.addWidget(self.vista_listado_equipos)

        self.vista_eventos_partido = EventosPartidoController(self.db,self)
        self.ui.stackedWidget.addWidget(self.vista_eventos_partido)
        
        self.vista_enfrentamientos = EnfrentamientoController(self.db,self)
        self.ui.stackedWidget.addWidget(self.vista_enfrentamientos)

        self.vista_calendario = CalendarioController(self.db,self)
        self.ui.stackedWidget.addWidget(self.vista_calendario)

        self.vista_creditos = CreditosController(self)
        self.ui.stackedWidget.addWidget(self.vista_creditos.widget)

        self.vista_guia = GuiaController(self)
        self.ui.stackedWidget.addWidget(self.vista_guia.widget)

        self.setup_connections()
        self.actualizar_tablero_inicio()



    def setup_connections(self):
        # Menú superior
        self.ui.actionRegistrar_Equipo.triggered.connect(self.mostrar_registro_equipos)
        self.ui.actionRegistrar_participante.triggered.connect(self.mostrar_registro_participantes)
        self.ui.actionParticipantes.triggered.connect(self.mostrar_listado_participantes)
        self.ui.actionEquipos.triggered.connect(self.mostrar_listado_equipos)
        self.ui.actionInicio_Partido.triggered.connect(self.mostrar_eventos_partido)
        self.ui.actionCrear_partido.triggered.connect(self.mostrar_enfrentamientos)
        self.ui.actionCalendario.triggered.connect(self.mostrar_calendario)
        self.ui.actionInicio.triggered.connect(self.mostrar_inicio)
        self.ui.actionGuia.triggered.connect(self.mostrar_guia)
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_creditos)
        
        # BOTÓN VOLVER: 
        self.vista_equipos.ui.pushButton_volver_equipos.clicked.connect(self.mostrar_inicio)
        self.vista_participantes.ui.pushButton_volver_participante.clicked.connect(self.mostrar_inicio)
        self.vista_listado_participantes.ui.pushButton_volver_lista_participantes.clicked.connect(self.mostrar_inicio)
        self.vista_listado_equipos.ui.pushButton_lista_equipos_volver.clicked.connect(self.mostrar_inicio)
        self.vista_enfrentamientos.ui.pushButton_volver_enfrentamientos.clicked.connect(self.mostrar_inicio)
        self.vista_eventos_partido.ui.pushButton_volver_eventos.clicked.connect(self.mostrar_inicio)
        self.vista_calendario.ui.pushButton_volver_calendario.clicked.connect(self.mostrar_inicio)

    def mostrar_inicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.titulo.setText("⚽ Torneo 2025-2026 ⚽")
        self.actualizar_tablero_inicio()

    def mostrar_registro_equipos(self):
        self.vista_equipos.configurar_modo_registro()
        self.ui.stackedWidget.setCurrentWidget(self.vista_equipos)
        self.ui.titulo.setText("👕 Registro de Equipos 👕")

    def mostrar_registro_participantes(self):
        self.vista_participantes.configurar_modo_registro()
        self.ui.stackedWidget.setCurrentWidget(self.vista_participantes)
        self.ui.titulo.setText("🏃 Registro de Participantes 🏃")

    def mostrar_listado_participantes(self):
        self.vista_listado_participantes.cargar_participantes()
        self.ui.stackedWidget.setCurrentWidget(self.vista_listado_participantes)
        self.ui.titulo.setText("👤 Listado/Estadisticas Participantes 👤")

    def mostrar_listado_equipos(self):
        self.vista_listado_equipos.cargar_equipos()
        self.ui.stackedWidget.setCurrentWidget(self.vista_listado_equipos)
        self.ui.titulo.setText("👕 Listado/Estadisticas Equipos 👕")

    def mostrar_eventos_partido(self):
        self.vista_eventos_partido.cargar_partidos()
        self.ui.stackedWidget.setCurrentWidget(self.vista_eventos_partido)
        self.ui.titulo.setText("⚽ Gestor Eventos de Partidos ⚽")

    def mostrar_enfrentamientos(self):
        self.vista_enfrentamientos.cargar_datos_iniciales()
        self.vista_enfrentamientos.cargar_partidos_existentes()
        self.ui.stackedWidget.setCurrentWidget(self.vista_enfrentamientos)
        self.ui.titulo.setText("⚔️ Enfrentamientos ⚔️")

    def mostrar_calendario(self):
        self.vista_calendario.cargar_partidos()
        self.ui.stackedWidget.setCurrentWidget(self.vista_calendario)
        self.ui.titulo.setText("📅 Calendario 📅")

    def mostrar_creditos(self):
        self.ui.stackedWidget.setCurrentWidget(self.vista_creditos.widget)
        self.ui.titulo.setText("ℹ️ Acerca de... ℹ️")

    def mostrar_guia(self):
        self.ui.stackedWidget.setCurrentWidget(self.vista_guia.widget)
        self.ui.titulo.setText("📖 Guía de Usuario 📖")

    def actualizar_tablero_inicio(self):
        """Consulta la DB y actualiza los labels de la pantalla principal con los partidos"""
        # Limpiar todos los labels primero
        for i in range(1, 31):
            nombre_label = f"label_equipo{i}"
            if hasattr(self.ui, nombre_label):
                getattr(self.ui, nombre_label).setText("")
        
        # Limpiar labels de cuartos, semi y final
        for i in range(1, 9):
            if hasattr(self.ui, f"label_cuartos{i}"):
                getattr(self.ui, f"label_cuartos{i}").setText("")
        for i in range(1, 5):
            if hasattr(self.ui, f"label_semi{i}"):
                getattr(self.ui, f"label_semi{i}").setText("")
        for i in range(1, 3):
            if hasattr(self.ui, f"label_final{i}"):
                getattr(self.ui, f"label_final{i}").setText("")
        
        # OCTAVOS DE FINAL - Mostrar equipos participantes
        partidos_octavos = self.db.obtener_partidos_por_fase("Octavos")
        num_equipos = len(partidos_octavos) * 2  # Cada partido tiene 2 equipos
        es_torneo_8_equipos = (num_equipos == 8)  # 4 partidos de octavos = 8 equipos
        # Mapeo: label_equipo1-2, 3-4, 5-6, 7-8 (lado izq) y 9-10, 11-12, 13-14, 15-16 (lado der)
        label_indices_octavos = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)]
        
        ganadores_octavos = {}  # Diccionario para guardar ganadores por índice
        
        for idx, partido in enumerate(partidos_octavos[:8]):
            if idx < len(label_indices_octavos):
                label_local_idx, label_visitante_idx = label_indices_octavos[idx]
                
                # Mostrar equipos en label_equipo
                if hasattr(self.ui, f"label_equipo{label_local_idx}"):
                    getattr(self.ui, f"label_equipo{label_local_idx}").setText(f" {partido[1]}")
                if hasattr(self.ui, f"label_equipo{label_visitante_idx}"):
                    getattr(self.ui, f"label_equipo{label_visitante_idx}").setText(f" {partido[2]}")
                
                # Determinar ganador si el partido está finalizado
                partido_completo = self.db.obtener_partido_por_id(partido[0])
                if partido_completo:
                    goles_local = partido_completo[8] if len(partido_completo) > 8 else 0
                    goles_visitante = partido_completo[9] if len(partido_completo) > 9 else 0
                    
                    # Verificar si está finalizado
                    conn = self.db.get_connection()
                    if conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT finalizado FROM partidos WHERE id = %s", (partido[0],))
                        resultado = cursor.fetchone()
                        cursor.close()
                        conn.close()
                        
                        if resultado and resultado[0] == 1:  # Partido finalizado
                            if goles_local > goles_visitante:
                                ganadores_octavos[idx] = partido[1]
                            elif goles_visitante > goles_local:
                                ganadores_octavos[idx] = partido[2]
        
        # CUARTOS - Mostrar ganadores de Octavos en label_cuartos
        # label_cuartos1 = ganador partido 0 (equipo1 vs equipo2)
        # label_cuartos2 = ganador partido 1 (equipo3 vs equipo4)
        # label_cuartos3 = ganador partido 2 (equipo5 vs equipo6)
        # label_cuartos4 = ganador partido 3 (equipo7 vs equipo8)
        # label_cuartos5 = ganador partido 4 (equipo9 vs equipo10)
        # label_cuartos6 = ganador partido 5 (equipo11 vs equipo12)
        # label_cuartos7 = ganador partido 6 (equipo13 vs equipo14)
        # label_cuartos8 = ganador partido 7 (equipo15 vs equipo16)
        for i in range(8):
            if i in ganadores_octavos:
                label_cuartos = f"label_cuartos{i + 1}"
                if hasattr(self.ui, label_cuartos):
                    getattr(self.ui, label_cuartos).setText(ganadores_octavos[i])
        
        # CUARTOS - También mostrar en label_equipo17-24
        partidos_cuartos = self.db.obtener_partidos_por_fase("Cuartos")
        label_indices_cuartos = [(17, 18), (23, 24), (19, 20), (21, 22)]
        
        ganadores_cuartos = {}
        
        for idx, partido in enumerate(partidos_cuartos[:4]):
            if idx < len(label_indices_cuartos):
                label_local_idx, label_visitante_idx = label_indices_cuartos[idx]
                
                if partido[1] and hasattr(self.ui, f"label_equipo{label_local_idx}"):
                    getattr(self.ui, f"label_equipo{label_local_idx}").setText(f" {partido[1]}")
                if partido[2] and hasattr(self.ui, f"label_equipo{label_visitante_idx}"):
                    getattr(self.ui, f"label_equipo{label_visitante_idx}").setText(f" {partido[2]}")
                
                # Determinar ganador si finalizado
                partido_completo = self.db.obtener_partido_por_id(partido[0])
                if partido_completo:
                    goles_local = partido_completo[8] if len(partido_completo) > 8 else 0
                    goles_visitante = partido_completo[9] if len(partido_completo) > 9 else 0
                    
                    conn = self.db.get_connection()
                    if conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT finalizado FROM partidos WHERE id = %s", (partido[0],))
                        resultado = cursor.fetchone()
                        cursor.close()
                        conn.close()
                        
                        if resultado and resultado[0] == 1:
                            if goles_local > goles_visitante:
                                ganadores_cuartos[idx] = partido[1]
                            elif goles_visitante > goles_local:
                                ganadores_cuartos[idx] = partido[2]
        
        # SEMIFINALES - Mostrar ganadores de Cuartos en label_semi
        # label_semi1 = ganador entre label_cuartos1 y label_cuartos2 (partido cuartos 0)
        # label_semi2 = ganador entre label_cuartos3 y label_cuartos4 (partido cuartos 1)
        # label_semi3 = ganador entre label_cuartos5 y label_cuartos6 (partido cuartos 2)
        # label_semi4 = ganador entre label_cuartos7 y label_cuartos8 (partido cuartos 3)
        mapeo_semi = {0: "label_semi1", 1: "label_semi2", 2: "label_semi3", 3: "label_semi4"}
        for idx_cuartos, ganador in ganadores_cuartos.items():
            if idx_cuartos in mapeo_semi and hasattr(self.ui, mapeo_semi[idx_cuartos]):
                getattr(self.ui, mapeo_semi[idx_cuartos]).setText(ganador)
        
        # SEMIFINALES - También mostrar en label_equipo25-28
        partidos_semi = self.db.obtener_partidos_por_fase("Semifinales")
        label_indices_semi = [(25, 26), (27, 28)]
        
        ganadores_semi = {}
        
        for idx, partido in enumerate(partidos_semi[:2]):
            if idx < len(label_indices_semi):
                label_local_idx, label_visitante_idx = label_indices_semi[idx]
                
                if partido[1] and hasattr(self.ui, f"label_equipo{label_local_idx}"):
                    getattr(self.ui, f"label_equipo{label_local_idx}").setText(f" {partido[1]}")
                if partido[2] and hasattr(self.ui, f"label_equipo{label_visitante_idx}"):
                    getattr(self.ui, f"label_equipo{label_visitante_idx}").setText(f" {partido[2]}")
                
                # Determinar ganador si finalizado
                partido_completo = self.db.obtener_partido_por_id(partido[0])
                if partido_completo:
                    goles_local = partido_completo[8] if len(partido_completo) > 8 else 0
                    goles_visitante = partido_completo[9] if len(partido_completo) > 9 else 0
                    
                    conn = self.db.get_connection()
                    if conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT finalizado FROM partidos WHERE id = %s", (partido[0],))
                        resultado = cursor.fetchone()
                        cursor.close()
                        conn.close()
                        
                        if resultado and resultado[0] == 1:
                            if goles_local > goles_visitante:
                                ganadores_semi[idx] = partido[1]
                            elif goles_visitante > goles_local:
                                ganadores_semi[idx] = partido[2]
        
        # Si es torneo de 8 equipos y hay ganador de semifinales, marcar como campeón
        if es_torneo_8_equipos and len(partidos_semi) > 0:
            # En torneo de 8 equipos, Semifinales es la final
            partido_final_8 = partidos_semi[0]
            partido_completo = self.db.obtener_partido_por_id(partido_final_8[0])
            if partido_completo:
                conn = self.db.get_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT finalizado FROM partidos WHERE id = %s", (partido_final_8[0],))
                    resultado = cursor.fetchone()
                    cursor.close()
                    conn.close()
                    
                    if resultado and resultado[0] == 1 and 0 in ganadores_semi:
                        # Hay un campeón en torneo de 8 equipos
                        campeon = ganadores_semi[0]
                        if hasattr(self.ui, "label_final1"):
                            self.ui.label_final1.setText(f"🏆 {campeon} 🏆")
                        return  # No procesar más fases
        
        # FINAL - Mostrar ganadores de Semifinales en label_final (solo en torneo de 16 equipos)
        # label_final1 = ganador entre label_semi1 y label_semi2 (partido semi 0)
        # label_final2 = ganador entre label_semi3 y label_semi4 (partido semi 1)
        if not es_torneo_8_equipos:
            if 0 in ganadores_semi and hasattr(self.ui, "label_final1"):
                self.ui.label_final1.setText(ganadores_semi[0])
            if 1 in ganadores_semi and hasattr(self.ui, "label_final2"):
                self.ui.label_final2.setText(ganadores_semi[1])
        
        # FINAL - Mostrar en label_equipo29-30
        partidos_final = self.db.obtener_partidos_por_fase("Final")
        if partidos_final and len(partidos_final) > 0:
            partido_final = partidos_final[0]
            
            if partido_final[1] and hasattr(self.ui, "label_equipo29"):
                self.ui.label_equipo29.setText(f" {partido_final[1]}")
            if partido_final[2] and hasattr(self.ui, "label_equipo30"):
                self.ui.label_equipo30.setText(f" {partido_final[2]}")
            
            # Determinar CAMPEÓN si la final está finalizada
            partido_completo = self.db.obtener_partido_por_id(partido_final[0])
            if partido_completo:
                goles_local = partido_completo[8] if len(partido_completo) > 8 else 0
                goles_visitante = partido_completo[9] if len(partido_completo) > 9 else 0
                
                conn = self.db.get_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT finalizado FROM partidos WHERE id = %s", (partido_final[0],))
                    resultado = cursor.fetchone()
                    cursor.close()
                    conn.close()
                    
                    if resultado and resultado[0] == 1:
                        campeon = None
                        if goles_local > goles_visitante:
                            campeon = partido_final[1]
                            # Reemplazar label_final1 con el campeón con trofeos
                            if hasattr(self.ui, "label_final1"):
                                self.ui.label_final1.setText(f"🏆 {campeon} 🏆")
                        elif goles_visitante > goles_local:
                            campeon = partido_final[2]
                            # Reemplazar label_final2 con el campeón con trofeos
                            if hasattr(self.ui, "label_final2"):
                                self.ui.label_final2.setText(f"🏆 {campeon} 🏆")