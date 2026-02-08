from PySide6.QtWidgets import QWidget, QHeaderView, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from views.ui.registro_equipos_ui import Ui_Registro_Equipos

class EquipoController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.ui = Ui_Registro_Equipos()
        self.ui.setupUi(self)
        
        self.ruta_escudo = "" 
        self.ruta_equipacion = ""
        self.equipo_actual_id = None  # Para saber si estamos editando
        self.modo_edicion = False  # Para controlar el modo de edición
        self.parent_controller = parent  # Referencia al MainController

        self.configurar_estetica()
        self.setup_conexiones()
        self.configurar_modo_registro()  # Configurar vista inicial

# CONEXIONES DE BOTONES --------------------------------------

    def setup_conexiones(self):
        self.ui.pushButton_cargar_escudo.clicked.connect(self.seleccionar_escudo)
        self.ui.pushButton_registrar_equipo.clicked.connect(self.registrar_equipo)
        self.ui.pushButton_cargar_equipacion.clicked.connect(self.seleccionar_equipacion)
        self.ui.pushButton_limpiar_equipo.clicked.connect(self.limpiar_formulario)
        self.ui.pushButton_crear_jugador_equipo.clicked.connect(self.crear_jugador)
        self.ui.pushButton_eliminar_equipo.clicked.connect(self.eliminar_equipo)

# CONFIGURAR MODO REGISTRO (desde menú) ----------------------

    def configurar_modo_registro(self):
        """Configura la vista cuando se entra desde el menú de registro"""
        self.modo_edicion = False
        self.equipo_actual_id = None
        self.ui.pushButton_eliminar_equipo.setVisible(False)
        self.ui.pushButton_registrar_equipo.setText("💾 Registrar")
        self.ui.tableWidget_jugadores_equipo.setRowCount(0)
        self.limpiar_formulario()

# CONFIGURAR MODO EDICIÓN (desde listado equipos) ------------

    def configurar_modo_edicion(self, equipo_id):
        """Configura la vista cuando se entra desde listado de equipos para editar"""
        self.modo_edicion = True
        self.equipo_actual_id = equipo_id
        self.ui.pushButton_eliminar_equipo.setVisible(True)
        self.ui.pushButton_registrar_equipo.setText("💾 Guardar Cambios")
        
        # Cargar datos del equipo
        equipo = self.db.obtener_equipo_por_id(equipo_id)
        if equipo:
            self.ui.lineEdit_nombre_equipo.setText(equipo[1])  # nombre
            # Buscar el índice del curso en el combobox
            index = self.ui.comboBox_curso_equipo.findText(equipo[2])
            if index >= 0:
                self.ui.comboBox_curso_equipo.setCurrentIndex(index)
            self.ui.lineEdit_color_equipo.setText(equipo[3])  # color
            
            # Cargar imágenes
            if equipo[4]:  # escudo_path
                self.ruta_escudo = equipo[4]
                pixmap = QPixmap(equipo[4])
                self.ui.label_imagen_escudo.setPixmap(pixmap.scaled(
                    self.ui.label_imagen_escudo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            if equipo[5]:  # equipacion_path
                self.ruta_equipacion = equipo[5]
                pixmap = QPixmap(equipo[5])
                self.ui.label_imagen_equipacion.setPixmap(pixmap.scaled(
                    self.ui.label_imagen_equipacion.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        # Cargar jugadores del equipo en la tabla
        self.cargar_jugadores_equipo()
        
# REGISTRO DE EQUIPO -----------------------------------------

    def registrar_equipo(self):
        
        # DATOS GROUP BOX

        nombre = self.ui.lineEdit_nombre_equipo.text().strip()
        
        curso = self.ui.comboBox_curso_equipo.currentText()
        if self.ui.comboBox_curso_equipo.currentIndex() == 0:
            curso = ""

        color = self.ui.lineEdit_color_equipo.text().strip()

        # VALIDACIÓN DE REQUISITOS MÍNIMOS
        errores = []
        if not nombre: errores.append("- Nombre del equipo")
        if not curso: errores.append("- Curso")
        if not color: errores.append("- Color de la equipación")
        if not self.ruta_escudo: errores.append("- Imagen del escudo")

        if errores:
            mensaje = "Por favor, rellene los siguientes campos obligatorios:\n" + "\n".join(errores)
            QMessageBox.warning(self, "Campos incompletos", mensaje)
            return 

        # REGISTRA O ACTUALIZA EN DB SI ALL OK
        if self.modo_edicion and self.equipo_actual_id:
            # Modo edición: actualizar equipo existente
            exito = self.db.actualizar_equipo(self.equipo_actual_id, nombre, curso, color, self.ruta_escudo, self.ruta_equipacion)
            if exito:
                QMessageBox.information(self, "Éxito", f"El equipo '{nombre}' ha sido actualizado correctamente.")
                self.cargar_jugadores_equipo()  # Recargar la tabla de jugadores
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el equipo en la base de datos.")
        else:
            # Modo registro: insertar nuevo equipo
            exito = self.db.insertar_equipo(nombre, curso, color, self.ruta_escudo, self.ruta_equipacion)        
            if exito:
                QMessageBox.information(self, "Éxito", f"El equipo '{nombre}' ha sido registrado correctamente.")
                # Obtener el ID del equipo recién creado
                self.equipo_actual_id = self.db.obtener_ultimo_equipo_id()
                # Habilitar botón crear jugador
                self.ui.pushButton_crear_jugador_equipo.setEnabled(True)
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el equipo en la base de datos.")

# CREAR JUGADOR -----------------------------------------------

    def crear_jugador(self):
        """Abre la vista de crear participante con el equipo pre-seleccionado"""
        if self.equipo_actual_id:
            # Cambiar a la vista de registro de participante
            if self.parent_controller:
                self.parent_controller.vista_participantes.configurar_para_equipo(self.equipo_actual_id)
                self.parent_controller.mostrar_registro_participantes()
        else:
            QMessageBox.warning(self, "Equipo no guardado", "Debe registrar el equipo primero antes de añadir jugadores.")

# ELIMINAR EQUIPO ---------------------------------------------

    def eliminar_equipo(self):
        """Elimina el equipo actual después de confirmación"""
        if not self.equipo_actual_id:
            return
        
        nombre_equipo = self.ui.lineEdit_nombre_equipo.text()
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar el equipo '{nombre_equipo}'?\n\nEsto quitará la asignación de equipo a todos sus jugadores.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            exito = self.db.eliminar_equipo(self.equipo_actual_id)
            if exito:
                QMessageBox.information(self, "Éxito", f"El equipo '{nombre_equipo}' ha sido eliminado.")
                # Volver a la vista anterior
                if self.parent_controller:
                    self.parent_controller.mostrar_inicio()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el equipo.")

# CARGAR JUGADORES DEL EQUIPO ---------------------------------

    def cargar_jugadores_equipo(self):
        """Carga los jugadores del equipo en la tabla"""
        if not self.equipo_actual_id:
            return
        
        jugadores = self.db.obtener_participantes_por_equipo(self.equipo_actual_id)
        self.ui.tableWidget_jugadores_equipo.setRowCount(0)
        
        for jugador in jugadores:
            fila = self.ui.tableWidget_jugadores_equipo.rowCount()
            self.ui.tableWidget_jugadores_equipo.insertRow(fila)
            
            # jugador: (id, nombre, apellido, curso, posicion, es_jugador, es_arbitro)
            self.ui.tableWidget_jugadores_equipo.setItem(fila, 0, QTableWidgetItem(jugador[1]))  # nombre
            self.ui.tableWidget_jugadores_equipo.setItem(fila, 1, QTableWidgetItem(jugador[2]))  # apellido
            self.ui.tableWidget_jugadores_equipo.setItem(fila, 2, QTableWidgetItem(jugador[3]))  # curso
            self.ui.tableWidget_jugadores_equipo.setItem(fila, 3, QTableWidgetItem(jugador[4] if jugador[4] else ""))  # posicion


# LIMPIAR FORMULARIO -----------------------------------------

    def limpiar_formulario(self):
        self.ui.lineEdit_nombre_equipo.clear()
        self.ui.lineEdit_color_equipo.clear()
        self.ui.comboBox_curso_equipo.setCurrentIndex(0)
        self.ui.label_imagen_escudo.clear()
        self.ui.label_imagen_escudo.setText("Sin imagen")
        self.ruta_escudo = ""
        self.ui.label_imagen_equipacion.clear()
        self.ui.label_imagen_equipacion.setText("Sin imagen")
        self.ruta_equipacion = ""
        self.ui.tableWidget_jugadores_equipo.setRowCount(0)
        
        if not self.modo_edicion:
            self.equipo_actual_id = None
            self.ui.pushButton_crear_jugador_equipo.setEnabled(False)

# SELECCION ESCUDO --------------------------------------------

    def seleccionar_escudo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Escudo", "", "Imágenes (*.png *.jpg *.jpeg)")
        if archivo:
            self.ruta_escudo = archivo
            pixmap = QPixmap(archivo)
            self.ui.label_imagen_escudo.setPixmap(pixmap.scaled(
                self.ui.label_imagen_escudo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))    

# SELECCION EQUIPACION ----------------------------------------

    def seleccionar_equipacion(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Equipacion", "", "Imágenes (*.png *.jpg *.jpeg)")
        if archivo:
            self.ruta_equipacion = archivo
            pixmap = QPixmap(archivo)
            self.ui.label_imagen_equipacion.setPixmap(pixmap.scaled(
                self.ui.label_imagen_equipacion.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

# ESTETICA VISUAL ---------------------------------------------

    def configurar_estetica(self):
        # --- BOTONES GRANDES (Recuadro Verde) ---
        # Reducimos a 12pt o 14pt para que quepa el texto + emoji
        estilo_botones = ("font-size: 11pt; font-weight: bold; color: #267E7E; "
                         "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;")
        
        self.ui.pushButton_registrar_equipo.setStyleSheet(estilo_botones)
        self.ui.pushButton_registrar_equipo.setText("💾 Registrar")
        
        self.ui.pushButton_limpiar_equipo.setStyleSheet(estilo_botones)
        self.ui.pushButton_limpiar_equipo.setText("🗑️ Limpiar")
        
        self.ui.pushButton_crear_jugador_equipo.setStyleSheet(estilo_botones)
        self.ui.pushButton_crear_jugador_equipo.setText("➕ Crear Jugador")
        
        self.ui.pushButton_eliminar_equipo.setStyleSheet(estilo_botones)
        self.ui.pushButton_eliminar_equipo.setText("❌ Eliminar Equipo")
        
        self.ui.pushButton_volver_equipos.setStyleSheet(estilo_botones)
        self.ui.pushButton_volver_equipos.setText("↩️ Volver")

        
        self.ui.groupBox_datos_equipo.setTitle("📋 Datos del Equipo")
        self.ui.groupBox_escudo.setTitle("🛡️ Escudo del Equipo")
        self.ui.groupBox_equipacion.setTitle("👕 Equipación")

        self.ui.lineEdit_nombre_equipo.setPlaceholderText("⚽ Nombre del Equipo *")
        self.ui.lineEdit_color_equipo.setPlaceholderText("👕 Color (ej: Rojo)")
        
        self.ui.pushButton_cargar_escudo.setText("📤 Cargar Escudo")
        self.ui.pushButton_cargar_equipacion.setText("📤 Cargar Equipación")

        self.ui.tableWidget_jugadores_equipo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_jugadores_equipo.setAlternatingRowColors(False)

        header = self.ui.tableWidget_jugadores_equipo.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        

        # Headers de tabla (Blanco y azul intermedio vía QSS)
        headers = ["👤 Nombre", "👤 Apellido", "📚 Curso", "⚡ Posición"]
        for i, text in enumerate(headers):
            item = self.ui.tableWidget_jugadores_equipo.horizontalHeaderItem(i)
            if item: item.setText(text)


        