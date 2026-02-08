from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from views.ui.eventos_partido_ui import Ui_EventosPartido
from enum import Enum

class EstadoPartido(Enum):
    SIN_SELECCIONAR = 0
    PENDIENTE = 1
    PRIMER_TIEMPO = 2
    DESCANSO = 3
    SEGUNDO_TIEMPO = 4
    FINALIZADO = 5

class EventosPartidoController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_controller = parent
        self.ui = Ui_EventosPartido()
        self.ui.setupUi(self)
        
        self.partido_actual_id = None
        self.equipo_local_id = None
        self.equipo_visitante_id = None
        self.estado_partido = EstadoPartido.SIN_SELECCIONAR

        self.configurar_estatica()
        self.setup_conexiones()
        self.configurar_reloj()
        self.cargar_partidos()

    def setup_conexiones(self):
        """Conecta los botones y combobox con sus funciones"""
        self.ui.comboBox_seleccion_partido_eventos.currentIndexChanged.connect(self.seleccionar_partido)
        self.ui.pushButton_registrar_evento.clicked.connect(self.registrar_evento)
        self.ui.pushButton_finalizar_partido.clicked.connect(self.manejador_boton_partido)
        
        # Conectar comboBox de equipos para filtrado en cadena
        self.ui.comboBox_intro_equipo_evento.currentIndexChanged.connect(self.filtrar_jugadores_por_equipo)
    
    def configurar_reloj(self):
        """Configura el widget de reloj en modo cronómetro"""
        # Configurar el reloj en modo timer (cronómetro)
        self.ui.widget_reloj.set_mode(1)  # 1 = TIMER mode
        self.ui.widget_reloj.set_timer_duration(30)  # 30 segundos por cada tiempo
        self.ui.widget_reloj.set_is_countdown(False)  # False = Cronómetro (cuenta hacia arriba)
        self.ui.widget_reloj.set_alarm_message("ALERTAS")
        
        # Conectar la señal de fin de temporizador
        self.ui.widget_reloj.timerFinished.connect(self.on_tiempo_finalizado)

    def cargar_partidos(self):
        """Carga todos los partidos no finalizados en el combobox"""
        self.ui.comboBox_seleccion_partido_eventos.clear()
        self.ui.comboBox_seleccion_partido_eventos.addItem("Seleccionar Partido", 0)
        
        partidos = self.db.obtener_partidos_no_finalizados()
        for partido in partidos:
            # partido: (id, equipo_local, equipo_visitante, fecha_hora, fase, goles_local, goles_visitante)
            texto = f"{partido[1]} vs {partido[2]} - {partido[4]}"
            self.ui.comboBox_seleccion_partido_eventos.addItem(texto, partido[0])

    def seleccionar_partido(self):
        """Se ejecuta cuando se selecciona un partido en el combobox"""
        partido_id = self.ui.comboBox_seleccion_partido_eventos.currentData()
        
        if partido_id and partido_id != 0:
            self.partido_actual_id = partido_id
            self.estado_partido = EstadoPartido.PENDIENTE
            
            # Obtener datos del partido
            partido = self.db.obtener_partido_por_id(partido_id)
            if partido:
                # partido: (id, equipo_local_id, equipo_visitante_id, equipo_local, equipo_visitante, arbitro_id, fecha_hora, fase, goles_local, goles_visitante)
                self.equipo_local_id = partido[1]
                self.equipo_visitante_id = partido[2]
                
                # Actualizar labels de nombres de equipos
                self.ui.titulo_equipoA_eventos.setText(partido[3])
                self.ui.titulo_equipoB_eventos.setText(partido[4])
                
                # Cargar comboBox de equipos
                self.cargar_combobox_equipos(partido[3], partido[4])
                
                # Cargar jugadores en los combobox (todos)
                self.cargar_jugadores_equipos()
                
                # Cargar eventos ya registrados
                self.cargar_eventos_partido()
                
                # Actualizar texto del botón y resetear reloj
                self.actualizar_boton_partido()
                self.ui.widget_reloj.reset_timer()
        else:
            self.partido_actual_id = None
            self.equipo_local_id = None
            self.equipo_visitante_id = None
            self.estado_partido = EstadoPartido.SIN_SELECCIONAR
            self.ui.titulo_equipoA_eventos.setText("Equipo A")
            self.ui.titulo_equipoB_eventos.setText("Equipo B")
            self.ui.comboBox_intro_equipo_evento.clear()
            self.ui.comboBox_intro_jugador_evento.clear()
            self.ui.tableWidget_eventos_equipoA.setRowCount(0)
            self.ui.tableWidget_eventos_equipoB.setRowCount(0)
            self.actualizar_boton_partido()
            self.ui.widget_reloj.reset_timer()

    def cargar_combobox_equipos(self, nombre_equipo_local, nombre_equipo_visitante):
        """Carga los dos equipos del partido en el comboBox de equipos"""
        self.ui.comboBox_intro_equipo_evento.clear()
        self.ui.comboBox_intro_equipo_evento.addItem("Todos los equipos", None)
        self.ui.comboBox_intro_equipo_evento.addItem(nombre_equipo_local, self.equipo_local_id)
        self.ui.comboBox_intro_equipo_evento.addItem(nombre_equipo_visitante, self.equipo_visitante_id)
    
    def cargar_jugadores_equipos(self):
        """Carga los jugadores de ambos equipos en el combobox"""
        self.ui.comboBox_intro_jugador_evento.clear()
        self.ui.comboBox_intro_jugador_evento.addItem("Seleccionar Jugador", (0, None))
        
        if self.equipo_local_id:
            jugadores_local = self.db.obtener_jugadores_por_equipo(self.equipo_local_id)
            for jugador_id, nombre, apellido in jugadores_local:
                nombre_completo = f"{nombre} {apellido} (Equipo A)"
                self.ui.comboBox_intro_jugador_evento.addItem(nombre_completo, (jugador_id, self.equipo_local_id))
        
        if self.equipo_visitante_id:
            jugadores_visitante = self.db.obtener_jugadores_por_equipo(self.equipo_visitante_id)
            for jugador_id, nombre, apellido in jugadores_visitante:
                nombre_completo = f"{nombre} {apellido} (Equipo B)"
                self.ui.comboBox_intro_jugador_evento.addItem(nombre_completo, (jugador_id, self.equipo_visitante_id))
    
    def filtrar_jugadores_por_equipo(self):
        """Filtra los jugadores según el equipo seleccionado en el comboBox de equipos"""
        equipo_id = self.ui.comboBox_intro_equipo_evento.currentData()
        
        self.ui.comboBox_intro_jugador_evento.clear()
        self.ui.comboBox_intro_jugador_evento.addItem("Seleccionar Jugador", (0, None))
        
        if equipo_id is None:
            # Mostrar todos los jugadores de ambos equipos
            self.cargar_jugadores_equipos()
        elif equipo_id == self.equipo_local_id:
            # Solo mostrar jugadores del equipo local
            jugadores_local = self.db.obtener_jugadores_por_equipo(self.equipo_local_id)
            for jugador_id, nombre, apellido in jugadores_local:
                nombre_completo = f"{nombre} {apellido}"
                self.ui.comboBox_intro_jugador_evento.addItem(nombre_completo, (jugador_id, self.equipo_local_id))
        elif equipo_id == self.equipo_visitante_id:
            # Solo mostrar jugadores del equipo visitante
            jugadores_visitante = self.db.obtener_jugadores_por_equipo(self.equipo_visitante_id)
            for jugador_id, nombre, apellido in jugadores_visitante:
                nombre_completo = f"{nombre} {apellido}"
                self.ui.comboBox_intro_jugador_evento.addItem(nombre_completo, (jugador_id, self.equipo_visitante_id))

    def cargar_eventos_partido(self):
        """Carga los eventos ya registrados del partido en las tablas"""
        if not self.partido_actual_id:
            return
        
        # Limpiar tablas
        self.ui.tableWidget_eventos_equipoA.setRowCount(0)
        self.ui.tableWidget_eventos_equipoB.setRowCount(0)
        
        # Cargar eventos del equipo A (local)
        if self.equipo_local_id:
            estadisticas_a = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_local_id)
            for est in estadisticas_a:
                # est: (nombre, apellido, goles, asistencias, faltas, amarillas, rojas, paradas)
                # Crear filas para cada tipo de evento
                nombre_completo = f"{est[0]} {est[1]}"
                
                # Goles
                for _ in range(est[2]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoA, nombre_completo, "Gol", "-")
                
                # Asistencias
                for _ in range(est[3]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoA, nombre_completo, "Asistencia", "-")
                
                # Amarillas
                for _ in range(est[5]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoA, nombre_completo, "Amarilla", "-")
                
                # Rojas
                for _ in range(est[6]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoA, nombre_completo, "Roja", "-")
        
        # Cargar eventos del equipo B (visitante)
        if self.equipo_visitante_id:
            estadisticas_b = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_visitante_id)
            for est in estadisticas_b:
                nombre_completo = f"{est[0]} {est[1]}"
                
                # Goles
                for _ in range(est[2]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoB, nombre_completo, "Gol", "-")
                
                # Asistencias
                for _ in range(est[3]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoB, nombre_completo, "Asistencia", "-")
                
                # Amarillas
                for _ in range(est[5]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoB, nombre_completo, "Amarilla", "-")
                
                # Rojas
                for _ in range(est[6]):
                    self.agregar_evento_tabla(self.ui.tableWidget_eventos_equipoB, nombre_completo, "Roja", "-")

    def agregar_evento_tabla(self, tabla, jugador, evento, minuto):
        """Agrega un evento a la tabla especificada"""
        fila = tabla.rowCount()
        tabla.insertRow(fila)
        
        tabla.setItem(fila, 0, QTableWidgetItem(jugador))
        tabla.setItem(fila, 1, QTableWidgetItem(evento))
        tabla.setItem(fila, 2, QTableWidgetItem(str(minuto)))

    def registrar_evento(self):
        """Registra un nuevo evento en el partido"""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Sin partido", "Debe seleccionar un partido primero.")
            return
        
        # Obtener datos del evento
        jugador_data = self.ui.comboBox_intro_jugador_evento.currentData()
        if not jugador_data or jugador_data[0] == 0:
            QMessageBox.warning(self, "Sin jugador", "Debe seleccionar un jugador.")
            return
        
        jugador_id, equipo_id = jugador_data
        
        tipo_evento = self.ui.comboBox_selector_evento.currentText()
        minuto = self.ui.spinBox_min_evento.value()
        
        if tipo_evento == "Seleccionar Evento" or tipo_evento == "Evento":
            QMessageBox.warning(self, "Sin evento", "Debe seleccionar un tipo de evento.")
            return
        
        # Determinar qué estadística incrementar (buscar palabra clave en el texto)
        goles = 1 if "Gol" in tipo_evento else 0
        asistencias = 1 if "Asistencia" in tipo_evento else 0
        faltas = 1 if "Falta" in tipo_evento else 0
        amarillas = 1 if "Amarilla" in tipo_evento else 0
        rojas = 1 if "Roja" in tipo_evento else 0
        paradas = 1 if "Parada" in tipo_evento else 0
        
        # Registrar en la base de datos
        exito = self.db.insertar_estadistica(
            jugador_id, self.partido_actual_id,
            goles, asistencias, faltas, amarillas, rojas, paradas
        )
        
        if exito:
            # Si es un gol, actualizar el contador de goles del partido
            if goles > 0:
                # Obtener goles actuales
                estadisticas_local = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_local_id)
                estadisticas_visitante = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_visitante_id)
                
                goles_local = sum(est[2] for est in estadisticas_local)
                goles_visitante = sum(est[2] for est in estadisticas_visitante)
                
                # Actualizar goles en la tabla partidos
                self.db.actualizar_goles_partido(self.partido_actual_id, goles_local, goles_visitante)
            
            # Agregar a la tabla correspondiente
            jugador_nombre = self.ui.comboBox_intro_jugador_evento.currentText()
            tabla = self.ui.tableWidget_eventos_equipoA if equipo_id == self.equipo_local_id else self.ui.tableWidget_eventos_equipoB
            
            # Determinar el texto del evento (extraer palabra clave)
            if "Gol" in tipo_evento:
                evento_texto = "Gol"
            elif "Asistencia" in tipo_evento:
                evento_texto = "Asistencia"
            elif "Falta" in tipo_evento:
                evento_texto = "Falta"
            elif "Amarilla" in tipo_evento:
                evento_texto = "Amarilla"
            elif "Roja" in tipo_evento:
                evento_texto = "Roja"
            elif "Parada" in tipo_evento:
                evento_texto = "Parada"
            else:
                evento_texto = tipo_evento
            
            self.agregar_evento_tabla(tabla, jugador_nombre, evento_texto, minuto)
            
            QMessageBox.information(self, "Evento registrado", f"El evento ha sido registrado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el evento.")
    
    def actualizar_boton_partido(self):
        """Actualiza el texto del botón según el estado del partido"""
        if self.estado_partido == EstadoPartido.SIN_SELECCIONAR:
            self.ui.pushButton_finalizar_partido.setText("Finalizar Partido")
            self.ui.pushButton_finalizar_partido.setEnabled(False)
        elif self.estado_partido == EstadoPartido.PENDIENTE:
            self.ui.pushButton_finalizar_partido.setText("Iniciar Partido")
            self.ui.pushButton_finalizar_partido.setEnabled(True)
        elif self.estado_partido == EstadoPartido.PRIMER_TIEMPO:
            self.ui.pushButton_finalizar_partido.setText("Primer Tiempo en Juego")
            self.ui.pushButton_finalizar_partido.setEnabled(False)
        elif self.estado_partido == EstadoPartido.DESCANSO:
            self.ui.pushButton_finalizar_partido.setText("Iniciar Segundo Tiempo")
            self.ui.pushButton_finalizar_partido.setEnabled(True)
        elif self.estado_partido == EstadoPartido.SEGUNDO_TIEMPO:
            self.ui.pushButton_finalizar_partido.setText("Segundo Tiempo en Juego")
            self.ui.pushButton_finalizar_partido.setEnabled(False)
        elif self.estado_partido == EstadoPartido.FINALIZADO:
            self.ui.pushButton_finalizar_partido.setText("Finalizar Partido")
            self.ui.pushButton_finalizar_partido.setEnabled(True)
    
    def manejador_boton_partido(self):
        """Maneja el clic del botón según el estado del partido"""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Sin partido", "Debe seleccionar un partido primero.")
            return
        
        if self.estado_partido == EstadoPartido.PENDIENTE:
            # Iniciar primer tiempo
            self.estado_partido = EstadoPartido.PRIMER_TIEMPO
            self.actualizar_boton_partido()
            self.ui.widget_reloj.reset_timer()
            self.ui.widget_reloj.set_alarm_message("Fin Primer Tiempo")
            self.ui.widget_reloj.start_timer()
            
        elif self.estado_partido == EstadoPartido.DESCANSO:
            # Iniciar segundo tiempo
            self.estado_partido = EstadoPartido.SEGUNDO_TIEMPO
            self.actualizar_boton_partido()
            self.ui.widget_reloj.reset_timer()
            self.ui.widget_reloj.set_alarm_message("Final Partido")
            self.ui.widget_reloj.start_timer()
            
        elif self.estado_partido == EstadoPartido.FINALIZADO:
            # Finalizar partido
            self.finalizar_partido()
    
    def on_tiempo_finalizado(self):
        """Se ejecuta cuando el cronómetro llega a 30 segundos"""
        if self.estado_partido == EstadoPartido.PRIMER_TIEMPO:
            # Fin del primer tiempo
            self.estado_partido = EstadoPartido.DESCANSO
            self.actualizar_boton_partido()
            QMessageBox.information(
                self,
                "Fin Primer Tiempo",
                "El primer tiempo ha finalizado. Presione 'Iniciar Segundo Tiempo' para continuar."
            )
            
        elif self.estado_partido == EstadoPartido.SEGUNDO_TIEMPO:
            # Fin del partido
            self.estado_partido = EstadoPartido.FINALIZADO
            self.actualizar_boton_partido()
            QMessageBox.information(
                self,
                "Final del Partido",
                "El partido ha finalizado. Presione 'Finalizar Partido' para guardar los resultados."
            )

    def finalizar_partido(self):
        """Finaliza el partido y determina el ganador"""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Sin partido", "Debe seleccionar un partido primero.")
            return
        
        respuesta = QMessageBox.question(
            self,
            "Finalizar partido",
            "¿Está seguro de que desea finalizar este partido?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            # Calcular goles de cada equipo
            partido = self.db.obtener_partido_por_id(self.partido_actual_id)
            if not partido:
                return
            
            # Obtener estadísticas del partido para contar goles
            estadisticas_local = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_local_id)
            estadisticas_visitante = self.db.obtener_estadisticas_por_partido(self.partido_actual_id, self.equipo_visitante_id)
            
            goles_local = sum(est[2] for est in estadisticas_local)  # est[2] es goles
            goles_visitante = sum(est[2] for est in estadisticas_visitante)
            
            # Actualizar goles en el partido
            self.db.actualizar_goles_partido(self.partido_actual_id, goles_local, goles_visitante)
            
            # Determinar ganador
            if goles_local > goles_visitante:
                ganador_id = self.equipo_local_id
                ganador_nombre = partido[3]
            elif goles_visitante > goles_local:
                ganador_id = self.equipo_visitante_id
                ganador_nombre = partido[4]
            else:
                QMessageBox.information(
                    self,
                    "Partido finalizado",
                    f"El partido ha terminado en empate ({goles_local}-{goles_visitante}).\n\nNota: En un torneo real se necesitaría definir penales o prórroga."
                )
                return
            
            # Avanzar a siguiente fase
            fase_actual = partido[7]
            exito_avance = self.db.avanzar_equipo_siguiente_fase(ganador_id, fase_actual, self.partido_actual_id)
            
            mensaje = f"El partido ha finalizado.\n\nGanador: {ganador_nombre}\nResultado: {goles_local} - {goles_visitante}"
            
            if exito_avance and fase_actual != "Final":
                fases = {
                    "Octavos": "Cuartos de Final",
                    "Cuartos": "Semifinales",
                    "Semifinales": "Final"
                }
                siguiente_fase = fases.get(fase_actual, "siguiente fase")
                mensaje += f"\n\n{ganador_nombre} avanza a {siguiente_fase}!"
            
            # Marcar partido como finalizado en la base de datos
            self.db.marcar_partido_finalizado(self.partido_actual_id)
            
            QMessageBox.information(
                self,
                "Partido finalizado",
                mensaje
            )
            
            # Recargar lista de partidos para que el finalizado no aparezca
            self.cargar_partidos()
            
            # Limpiar selección actual
            self.partido_actual_id = None
            self.equipo_local_id = None
            self.equipo_visitante_id = None
            self.estado_partido = EstadoPartido.SIN_SELECCIONAR
            self.ui.titulo_equipoA_eventos.setText("Equipo A")
            self.ui.titulo_equipoB_eventos.setText("Equipo B")
            self.ui.tableWidget_eventos_equipoA.setRowCount(0)
            self.ui.tableWidget_eventos_equipoB.setRowCount(0)
            self.ui.widget_reloj.reset_timer()
            self.actualizar_boton_partido()
            
            # Actualizar el tablero de inicio si existe el controlador padre
            if self.parent_controller and hasattr(self.parent_controller, 'actualizar_tablero_inicio'):
                self.parent_controller.actualizar_tablero_inicio()
            
            # Limpiar selección
            self.ui.comboBox_seleccion_partido_eventos.setCurrentIndex(0)

        
    def configurar_estatica(self):

                estilo_botones = (
                    "font-size: 11pt; font-weight: bold; color: #267E7E; "
                    "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
                )


                self.ui.pushButton_registrar_evento.setStyleSheet(estilo_botones)
                self.ui.pushButton_registrar_evento.setText("Registrar Evento")

                self.ui.pushButton_finalizar_partido.setStyleSheet(estilo_botones)
                self.actualizar_boton_partido()  # Usar la función para establecer el texto inicial

                self.ui.pushButton_volver_eventos.setStyleSheet(estilo_botones)
                self.ui.pushButton_volver_eventos.setText("Volver")

                self.ui.groupBox_datos_equipo.setTitle("Eventos del Partido")

                # Configurar tabla Equipo A
                self.ui.tableWidget_eventos_equipoA.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.ui.tableWidget_eventos_equipoA.setAlternatingRowColors(False)
                self.ui.tableWidget_eventos_equipoA.verticalHeader().setVisible(False)  # Ocultar números de fila
                
                estilo_tabla = (
                    "QTableWidget { background-color: #1B5A5A; color: white; }"
                    "QTableWidget::item { padding: 5px; background-color: #1B5A5A; color: white; border: 1px solid #267E7E; }"
                    "QTableWidget::item:selected { background-color: #267E7E; }"
                    "QHeaderView::section { background-color: #0D3A3A; color: white; padding: 5px; border: 1px solid #267E7E; }"
                )
                self.ui.tableWidget_eventos_equipoA.setStyleSheet(estilo_tabla)
                
                # Configurar tabla Equipo B
                self.ui.tableWidget_eventos_equipoB.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.ui.tableWidget_eventos_equipoB.setAlternatingRowColors(False)
                self.ui.tableWidget_eventos_equipoB.verticalHeader().setVisible(False)  # Ocultar números de fila
                self.ui.tableWidget_eventos_equipoB.setStyleSheet(estilo_tabla)

                # Cabeceras de las tablas
                headers = [
                    "Jugador", "Evento", "Minuto", 
                ]
                for i, text in enumerate(headers):
                    item = self.ui.tableWidget_eventos_equipoA.horizontalHeaderItem(i)
                    if item:
                        item.setText(text)

                for i, text in enumerate(headers):
                            item = self.ui.tableWidget_eventos_equipoB.horizontalHeaderItem(i)
                            if item:
                                item.setText(text)          