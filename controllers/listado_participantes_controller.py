from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from views.ui.listado_participantes_ui import Ui_Listado_Participantes

class ListadoParticipantesController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_controller = parent
        self.ui = Ui_Listado_Participantes()
        self.ui.setupUi(self)

        self.configurar_estatica()
        self.setup_conexiones()
        self.cargar_equipos_combobox()
        self.cargar_participantes()

    def setup_conexiones(self):
        """Conecta los botones con sus funciones"""
        self.ui.pushButton_buscar_participante.clicked.connect(self.buscar_participantes)
        self.ui.pushButton_editar_participante.clicked.connect(self.editar_participante)

    def cargar_equipos_combobox(self):
        """Carga los equipos en el combobox de filtros"""
        self.ui.comboBox_equipo_participante_filtro.clear()
        self.ui.comboBox_equipo_participante_filtro.addItem("Seleccionar Equipo")
        
        equipos = self.db.obtener_equipos()
        for equipo_id, nombre in equipos:
            self.ui.comboBox_equipo_participante_filtro.addItem(nombre)

    def cargar_participantes(self):
        """Carga todos los participantes con sus estadísticas en la tabla"""
        participantes = self.db.obtener_participantes_con_estadisticas()
        self.actualizar_tabla(participantes)

    def buscar_participantes(self):
        """Aplica los filtros y busca participantes"""
        filtro_curso = self.ui.comboBox_curso_participante_filtro.currentText()
        filtro_nombre = self.ui.lineEdit_nombre_participante_filtro.text().strip()
        filtro_equipo = self.ui.comboBox_equipo_participante_filtro.currentText()
        filtro_tipo = None
        
        if hasattr(self.ui, 'comboBox_tipo_participante_filtro'):
            filtro_tipo = self.ui.comboBox_tipo_participante_filtro.currentText()
            if filtro_tipo == "Seleccionar Tipo":
                filtro_tipo = None
        
        if filtro_curso == "Seleccionar Curso":
            filtro_curso = None
        
        if filtro_equipo == "Seleccionar Equipo":
            filtro_equipo = None
        
        participantes = self.db.obtener_participantes_con_estadisticas(
            filtro_curso, filtro_nombre, filtro_equipo, filtro_tipo
        )
        self.actualizar_tabla(participantes)

    def actualizar_tabla(self, participantes):
        """Actualiza la tabla con los datos de participantes"""
        self.ui.tableWidget_lista_participantes.setRowCount(0)
        
        for participante in participantes:
            # participante: (id, nombre, apellido, equipo, posicion, total_goles, total_asistencias, 
            #                total_faltas, total_amarillas, total_rojas, total_paradas)
            fila = self.ui.tableWidget_lista_participantes.rowCount()
            self.ui.tableWidget_lista_participantes.insertRow(fila)
            
            # Guardar el ID en la primera columna
            item_nombre = QTableWidgetItem(participante[1])
            item_nombre.setData(Qt.UserRole, participante[0])  # Guardar ID
            self.ui.tableWidget_lista_participantes.setItem(fila, 0, item_nombre)
            
            self.ui.tableWidget_lista_participantes.setItem(fila, 1, QTableWidgetItem(participante[2]))  # apellido
            self.ui.tableWidget_lista_participantes.setItem(fila, 2, QTableWidgetItem(participante[3]))  # equipo
            self.ui.tableWidget_lista_participantes.setItem(fila, 3, QTableWidgetItem(participante[4] if participante[4] else ""))  # posicion
            self.ui.tableWidget_lista_participantes.setItem(fila, 4, QTableWidgetItem(str(participante[5])))  # goles
            self.ui.tableWidget_lista_participantes.setItem(fila, 5, QTableWidgetItem(str(participante[6])))  # asistencias
            self.ui.tableWidget_lista_participantes.setItem(fila, 6, QTableWidgetItem(str(participante[7])))  # faltas
            self.ui.tableWidget_lista_participantes.setItem(fila, 7, QTableWidgetItem(str(participante[8])))  # amarillas
            self.ui.tableWidget_lista_participantes.setItem(fila, 8, QTableWidgetItem(str(participante[9])))  # rojas
            self.ui.tableWidget_lista_participantes.setItem(fila, 9, QTableWidgetItem(str(participante[10])))  # paradas

    def editar_participante(self):
        """Abre la vista de edición del participante seleccionado"""
        fila_seleccionada = self.ui.tableWidget_lista_participantes.currentRow()
        
        if fila_seleccionada < 0:
            QMessageBox.warning(self, "Sin selección", "Debe seleccionar un participante para editar.")
            return
        
        # Obtener el ID del participante
        item = self.ui.tableWidget_lista_participantes.item(fila_seleccionada, 0)
        participante_id = item.data(Qt.UserRole)
        
        # Cambiar a la vista de registro de participantes en modo edición
        if self.parent_controller:
            self.parent_controller.vista_participantes.configurar_modo_edicion(participante_id)
            self.parent_controller.ui.stackedWidget.setCurrentWidget(self.parent_controller.vista_participantes)
            self.parent_controller.ui.titulo.setText("📝 Editar Participante 📝")

    def configurar_estatica(self):

        estilo_botones = (
            "font-size: 11pt; font-weight: bold; color: #267E7E; "
            "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
        )

        self.ui.pushButton_buscar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_buscar_participante.setText("🔎 Buscar")
        
        self.ui.pushButton_editar_participante.setStyleSheet(estilo_botones)
        self.ui.pushButton_editar_participante.setText("📝 Editar")
        
        self.ui.pushButton_volver_lista_participantes.setStyleSheet(estilo_botones)
        self.ui.pushButton_volver_lista_participantes.setText("↩️ Volver")


        self.ui.groupBox_filtro_participante.setTitle("Filtros de Busqueda 📋")

        self.ui.lineEdit_nombre_participante_filtro.setPlaceholderText("👤 Nombre del Participante")

        # Desactivar colores alternados
        self.ui.tableWidget_lista_participantes.setAlternatingRowColors(False)

        header = self.ui.tableWidget_lista_participantes.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        # --- CABECERAS DE LA TABLA ---
        headers = [
            "👤 Nombre", "👤 Apellido", "👕 Equipo", 
            "⚡ Posición", "⚽ Goles", "👟 Asistencias", "🗣️❌ Faltas",
            "🟨 Amarillas", "🟥 Rojas", "🧤Paradas"
        ]
        for i, text in enumerate(headers):
            item = self.ui.tableWidget_lista_participantes.horizontalHeaderItem(i)
            if item:
                item.setText(text)