from doctest import ELLIPSIS_MARKER
from PySide6.QtWidgets import QWidget, QHeaderView, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QDate
from views.ui.registro_participantes_ui import Ui_Registro_Participante
from models.db_manager import DatabaseManager

class ParticipanteController(QWidget):
    def __init__(self, db: DatabaseManager, parent=None):
        super().__init__(parent)
        self.db = db    
        self.ui = Ui_Registro_Participante()
        self.ui.setupUi(self)
        
        self.ruta_foto_participante = ""
        self.participante_actual_id = None
        self.modo_edicion = False
        self.equipo_preseleccionado_id = None  # Para cuando venimos desde crear jugador en equipo
        self.parent_controller = parent
        
        self.conexiones()
        self.configurar_estetica()
        self.cargar_equipos_combobox()
        self.configurar_modo_registro()

# CONEXIONES DE BOTONES -----------------------------------------------------------------------------

    def conexiones(self):
        self.ui.pushButton_cargar_participante.clicked.connect(self.seleccionar_foto)
        self.ui.pushButton_guardar_participante.clicked.connect(self.registrar_participante)
        self.ui.pushButton_limpiar_participante.clicked.connect(self.limpiar_formulario)
        self.ui.pushButton_asignar_participante.clicked.connect(self.asignar_equipo_partido)
        self.ui.pushButton_eliminar_participante.clicked.connect(self.eliminar_participante)

# CARGAR EQUIPOS EN COMBOBOX ------------------------------------------------------------------

    def cargar_equipos_combobox(self):
        """Carga los equipos disponibles en el combobox"""
        if not hasattr(self.ui, 'comboBox_equipo_participante'):
            return
        
        self.ui.comboBox_equipo_participante.clear()
        self.ui.comboBox_equipo_participante.addItem("Sin equipo", 0)
        
        equipos = self.db.obtener_equipos()
        for equipo_id, nombre in equipos:
            self.ui.comboBox_equipo_participante.addItem(nombre, equipo_id)

# CONFIGURAR MODO REGISTRO --------------------------------------------------------------------

    def configurar_modo_registro(self):
        """Configura la vista cuando se entra desde el menú de registro"""
        self.modo_edicion = False
        self.participante_actual_id = None
        self.equipo_preseleccionado_id = None
        self.ui.pushButton_eliminar_participante.setVisible(False)
        self.ui.pushButton_guardar_participante.setText("💾 Guardar Cambios")
        self.ui.tableWidget_participante.setRowCount(0)
        if hasattr(self.ui, 'textEdit_resumen_participante'):
            self.ui.textEdit_resumen_participante.setPlainText("Historial")
        self.limpiar_formulario()

# CONFIGURAR PARA EQUIPO (desde crear jugador) ----------------------------------------------

    def configurar_para_equipo(self, equipo_id):
        """Configura la vista cuando se crea un jugador desde un equipo"""
        self.configurar_modo_registro()
        self.equipo_preseleccionado_id = equipo_id
        # Pre-seleccionar el equipo en el combobox
        if hasattr(self.ui, 'comboBox_equipo_participante'):
            index = self.ui.comboBox_equipo_participante.findData(equipo_id)
            if index >= 0:
                self.ui.comboBox_equipo_participante.setCurrentIndex(index)

# CONFIGURAR MODO EDICIÓN (desde listado participantes) -------------------------------------

    def configurar_modo_edicion(self, participante_id):
        """Configura la vista cuando se entra desde listado de participantes para editar"""
        self.modo_edicion = True
        self.participante_actual_id = participante_id
        self.equipo_preseleccionado_id = None
        self.ui.pushButton_eliminar_participante.setVisible(True)
        self.ui.pushButton_guardar_participante.setText("💾 Guardar Cambios")
        
        # Cargar datos del participante
        participante = self.db.obtener_participante_por_id(participante_id)
        if participante:
            # participante: (id, nombre, apellido, fecha_nacimiento, curso, posicion, es_jugador, es_arbitro, foto_path, equipo_id)
            self.ui.lineEdit_nombre_participante.setText(participante[1])
            self.ui.lineEdit_apellido_participante.setText(participante[2])
            
            # Fecha de nacimiento
            if participante[3]:
                fecha = QDate.fromString(participante[3], "yyyy/MM/dd")
                self.ui.dateEdit_fecha_nacimiento.setDate(fecha)
            
            # Curso
            index = self.ui.comboBox_curso_participante.findText(participante[4])
            if index >= 0:
                self.ui.comboBox_curso_participante.setCurrentIndex(index)
            
            # Posición
            if hasattr(self.ui, 'comboBox_posicion_participante') and participante[5]:
                index = self.ui.comboBox_posicion_participante.findText(participante[5])
                if index >= 0:
                    self.ui.comboBox_posicion_participante.setCurrentIndex(index)
            
            # Tipo (jugador/árbitro)
            self.ui.radioButton_jugador.setAutoExclusive(False)
            self.ui.radioButton_arbitro.setAutoExclusive(False)
            self.ui.radioButton_jugador.setChecked(participante[6] == 1)
            self.ui.radioButton_arbitro.setChecked(participante[7] == 1)
            self.ui.radioButton_jugador.setAutoExclusive(True)
            self.ui.radioButton_arbitro.setAutoExclusive(True)
            
            # Foto
            if participante[8]:
                self.ruta_foto_participante = participante[8]
                pixmap = QPixmap(participante[8])
                self.ui.label_imagen_participante.setPixmap(pixmap.scaled(
                    self.ui.label_imagen_participante.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            # Equipo
            if participante[9] and hasattr(self.ui, 'comboBox_equipo_participante'):
                index = self.ui.comboBox_equipo_participante.findData(participante[9])
                if index >= 0:
                    self.ui.comboBox_equipo_participante.setCurrentIndex(index)
        
        # Cargar estadísticas en la tabla
        self.cargar_estadisticas_participante()
        # Cargar resumen en el label
        self.cargar_resumen_estadisticas()

# REGISTRO DE PARTICIPANTE -------------------------------------------------------------------------

    def registrar_participante(self):

        # DATOS DEL GROUP BOX
        nombre = self.ui.lineEdit_nombre_participante.text().strip()
        apellido = self.ui.lineEdit_apellido_participante.text().strip()

        fecha_nacimiento = self.ui.dateEdit_fecha_nacimiento.date().toString("yyyy/MM/dd")

        curso = self.ui.comboBox_curso_participante.currentText()
        if self.ui.comboBox_curso_participante.currentIndex() == 0:
            curso = ""

        es_jugador = 1 if self.ui.radioButton_jugador.isChecked() else 0
        es_arbitro = 1 if self.ui.radioButton_arbitro.isChecked() else 0
        
        equipo_id = None
        if hasattr(self.ui, 'comboBox_equipo_participante'):
            equipo_id = self.ui.comboBox_equipo_participante.currentData()
            if equipo_id == 0:
                equipo_id = None
        elif self.equipo_preseleccionado_id:
            equipo_id = self.equipo_preseleccionado_id
        
        posicion = ""
        if hasattr(self.ui, 'comboBox_posicion_participante'):
            posicion = self.ui.comboBox_posicion_participante.currentText()
            if self.ui.comboBox_posicion_participante.currentIndex() == 0:
                posicion = ""

        errores = []
        if not nombre: errores.append("- Nombre del Participante")
        if not apellido: errores.append("- Apellido del Participante")
        if not fecha_nacimiento: errores.append("- Fecha de Nacimiento")
        if es_jugador == 0 and es_arbitro == 0:
            errores.append("- Indica tipo jugador o arbitro")
        

        if errores:
            mensaje = "Por favor, rellene los siguientes campos obligatorios:\n" + "\n".join(errores)
            QMessageBox.warning(self, "Campos incompletos", mensaje)
            return
        
        # REGISTRA O ACTUALIZA EN DB SI ALL OK
        if self.modo_edicion and self.participante_actual_id:
            # Modo edición: actualizar participante existente
            exito = self.db.actualizar_participante(
                self.participante_actual_id, nombre, apellido, curso, fecha_nacimiento, 
                posicion, es_jugador, es_arbitro, 
                self.ruta_foto_participante, equipo_id
            )
            if exito:
                QMessageBox.information(self, "Éxito", f"El participante '{nombre} {apellido}' ha sido actualizado correctamente.")
                self.cargar_estadisticas_participante()
                self.cargar_resumen_estadisticas()
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el participante en la base de datos.")
        else:
            # Modo registro: insertar nuevo participante
            exito = self.db.insertar_participante(
                nombre, apellido, curso, fecha_nacimiento, 
                posicion, es_jugador, es_arbitro, 
                self.ruta_foto_participante, equipo_id
            )
            if exito:
                QMessageBox.information(self, "Éxito", f"El participante '{nombre} {apellido}' ha sido registrado correctamente.")
                # Si venimos desde crear jugador en equipo, volver a la vista de equipo
                if self.equipo_preseleccionado_id and self.parent_controller:
                    self.parent_controller.vista_equipos.cargar_jugadores_equipo()
                    self.parent_controller.ui.stackedWidget.setCurrentWidget(self.parent_controller.vista_equipos)
                else:
                    self.limpiar_formulario()
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el participante en la base de datos.")

# ASIGNAR EQUIPO/PARTIDO ----------------------------------------------------------------------

    def asignar_equipo_partido(self):
        """Guarda el participante y lo asigna a equipo (si es jugador) o partido (si es árbitro)"""
        # Primero guardar el participante
        self.registrar_participante()
        
        # Determinar si es jugador o árbitro
        es_jugador = self.ui.radioButton_jugador.isChecked()
        es_arbitro = self.ui.radioButton_arbitro.isChecked()
        
        if es_jugador and self.parent_controller:
            # Ir a vista de listado de equipos
            self.parent_controller.mostrar_listado_equipos()
        elif es_arbitro and self.parent_controller:
            # Ir a vista de crear partido (enfrentamientos)
            self.parent_controller.mostrar_enfrentamientos()

# ELIMINAR PARTICIPANTE -----------------------------------------------------------------------

    def eliminar_participante(self):
        """Elimina el participante actual después de confirmación"""
        if not self.participante_actual_id:
            return
        
        nombre = self.ui.lineEdit_nombre_participante.text()
        apellido = self.ui.lineEdit_apellido_participante.text()
        
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar a {nombre} {apellido}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            exito = self.db.eliminar_participante(self.participante_actual_id)
            if exito:
                QMessageBox.information(self, "Éxito", f"{nombre} {apellido} ha sido eliminado.")
                if self.parent_controller:
                    self.parent_controller.mostrar_inicio()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el participante.")

# CARGAR ESTADÍSTICAS ---------  --------------------------------------------------------------

    def cargar_estadisticas_participante(self):
        """Carga las estadísticas del participante en la tabla"""
        if not self.participante_actual_id:
            return
        
        estadisticas = self.db.obtener_estadisticas_participante(self.participante_actual_id)
        self.ui.tableWidget_participante.setRowCount(0)
        
        for est in estadisticas:
            # est: (goles, asistencias, faltas, amarillas, rojas, paradas, fecha_hora)
            fila = self.ui.tableWidget_participante.rowCount()
            self.ui.tableWidget_participante.insertRow(fila)
            
            self.ui.tableWidget_participante.setItem(fila, 0, QTableWidgetItem(str(est[0])))  # goles
            self.ui.tableWidget_participante.setItem(fila, 1, QTableWidgetItem(str(est[5])))  # paradas
            self.ui.tableWidget_participante.setItem(fila, 2, QTableWidgetItem(str(est[1])))  # asistencias
            self.ui.tableWidget_participante.setItem(fila, 3, QTableWidgetItem(str(est[2])))  # faltas
            self.ui.tableWidget_participante.setItem(fila, 4, QTableWidgetItem(str(est[3])))  # amarillas
            self.ui.tableWidget_participante.setItem(fila, 5, QTableWidgetItem(str(est[4])))  # rojas
            fecha_str = str(est[6]) if est[6] else "Sin fecha"
            self.ui.tableWidget_participante.setItem(fila, 6, QTableWidgetItem(fecha_str))  # fecha
        
        # Actualizar el resumen después de cargar la tabla
        self.cargar_resumen_estadisticas()

# CARGAR RESUMEN ESTADÍSTICAS -----------------------------------------------------------------

    def cargar_resumen_estadisticas(self):
        """Carga el resumen de estadísticas en el textEdit"""
        if not self.participante_actual_id or not hasattr(self.ui, 'textEdit_resumen_participante'):
            return
        
        resumen = self.db.obtener_resumen_estadisticas_participante(self.participante_actual_id)
        if resumen:
            texto = (f"Historial:\n"
                    f"- Goles: {resumen[0]}\n"
                    f"- Asistencias: {resumen[1]}\n"
                    f"- Faltas: {resumen[2]}\n"
                    f"- Amarillas: {resumen[3]}\n"
                    f"- Rojas: {resumen[4]}\n"
                    f"- Paradas: {resumen[5]}")
            self.ui.textEdit_resumen_participante.setPlainText(texto)


# LIMPIAR FORMULARIO -------------------------------------------------------------------------------

    def limpiar_formulario(self):
        self.ui.lineEdit_nombre_participante.clear()
        self.ui.lineEdit_apellido_participante.clear()
        self.ui.dateEdit_fecha_nacimiento.setDate(QDate.currentDate())
        self.ui.comboBox_curso_participante.setCurrentIndex(0)
        self.ui.radioButton_jugador.setAutoExclusive(False)
        self.ui.radioButton_jugador.setChecked(False)
        self.ui.radioButton_arbitro.setChecked(False)
        self.ui.radioButton_jugador.setAutoExclusive(True)
        if hasattr(self.ui, 'comboBox_equipo_participante'):
            self.ui.comboBox_equipo_participante.setCurrentIndex(0)
        if hasattr(self.ui, 'comboBox_posicion_participante'):
            self.ui.comboBox_posicion_participante.setCurrentIndex(0)
        self.ui.label_imagen_participante.clear()
        self.ui.label_imagen_participante.setText("Sin imagen")
        self.ruta_foto_participante = ""
        self.ui.tableWidget_participante.setRowCount(0)
        if hasattr(self.ui, 'textEdit_resumen_participante'):
            self.ui.textEdit_resumen_participante.setPlainText("Historial")
        
        if not self.modo_edicion:
            self.participante_actual_id = None

# SELECCION FOTO -----------------------------------------------------------------------------------

    def seleccionar_foto(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar foto", "", "Imágenes (*.png *.jpg *.jpeg)")
        if archivo:
            self.ruta_foto_participante = archivo
            pixmap = QPixmap(archivo)
            self.ui.label_imagen_participante.setPixmap(pixmap.scaled(
                self.ui.label_imagen_participante.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))  


# ESTETICA VISUAL ----------------------------------------------------------------------------------

    def configurar_estetica(self):
        # --- BOTONES INFERIORES (Estilo Naranja - Tamaño 11pt) ---
        estilo_botones = (
            "font-size: 11pt; font-weight: bold; color: #267E7E; "
            "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
        )
        
        self.ui.pushButton_asignar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_asignar_participante.setText("📥 Asignar Equipo/Partido")
        
        self.ui.pushButton_eliminar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_eliminar_participante.setText("❌ Eliminar Jugador")
        
        self.ui.pushButton_guardar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_guardar_participante.setText("💾 Guardar Cambios")
        
        self.ui.pushButton_limpiar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_limpiar_participante.setText("🗑️ Limpiar")
        
        self.ui.pushButton_volver_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_volver_participante.setText("↩️ Volver")

        # --- SECCIONES Y CAMPOS (Emojis tamaño 20) ---
        self.ui.groupBox_datos_participante.setTitle("📋 Datos Participante")
        self.ui.groupBox_tipo_participante.setTitle("🏃 Tipo Participante")
        self.ui.groupBox_escudo.setTitle("👤 Foto Jugador") # Nombre de objeto del .ui
        
        self.ui.lineEdit_nombre_participante.setPlaceholderText("👤 Nombre del Participante *")
        self.ui.radioButton_jugador.setText("⚽ Jugador")
        self.ui.radioButton_arbitro.setText("🏁 Árbitro")
        
        self.ui.pushButton_cargar_participante.setText("📤 Cargar Foto")

        self.ui.tableWidget_participante.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_participante.setAlternatingRowColors(False)

        # --- CABECERAS DE LA TABLA ---
        headers = [
            "⚽ Goles", "🧤 Paradas", "👟 Asistencias", 
            "🗣️❌ Faltas", "🟨 Amarillas", "🟥 Rojas", "🗓️ Fecha"
        ]
        for i, text in enumerate(headers):
            item = self.ui.tableWidget_participante.horizontalHeaderItem(i)
            if item:
                item.setText(text)

