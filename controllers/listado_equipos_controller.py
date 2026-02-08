from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from views.ui.listado_equipos_ui import Ui_ListadoEquipos

class ListadoEquiposController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_controller = parent
        self.ui = Ui_ListadoEquipos()
        self.ui.setupUi(self)

        self.configurar_estatica()
        self.setup_conexiones()
        self.cargar_equipos()

    def setup_conexiones(self):
        """Conecta los botones con sus funciones"""
        self.ui.pushButton_buscar_equipos.clicked.connect(self.buscar_equipos)
        self.ui.pushButton_editar_equipos.clicked.connect(self.editar_equipo)

    def cargar_equipos(self):
        """Carga todos los equipos con sus estadísticas en la tabla"""
        equipos = self.db.obtener_equipos_con_estadisticas()
        self.actualizar_tabla(equipos)

    def buscar_equipos(self):
        """Aplica los filtros y busca equipos"""
        filtro_curso = self.ui.comboBox_curso_equipo_filtro.currentText()
        filtro_nombre = self.ui.lineEdit_nombre_equipo_filtro.text().strip()
        
        if filtro_curso == "Seleccionar Curso":
            filtro_curso = None
        
        equipos = self.db.obtener_equipos_con_estadisticas(filtro_curso, filtro_nombre)
        self.actualizar_tabla(equipos)

    def actualizar_tabla(self, equipos):
        """Actualiza la tabla con los datos de equipos"""
        self.ui.tableWidget_lista_equipos.setRowCount(0)
        
        for equipo in equipos:
            # equipo: (id, nombre, curso, victorias, total_goles, total_faltas, total_amarillas, total_rojas, total_paradas)
            fila = self.ui.tableWidget_lista_equipos.rowCount()
            self.ui.tableWidget_lista_equipos.insertRow(fila)
            
            # Guardar el ID en la primera columna (oculta o como dato)
            item_id = QTableWidgetItem()
            item_id.setData(Qt.UserRole, equipo[0])  # Guardar ID
            item_id.setText(equipo[1])  # Mostrar nombre
            self.ui.tableWidget_lista_equipos.setItem(fila, 0, item_id)
            
            self.ui.tableWidget_lista_equipos.setItem(fila, 1, QTableWidgetItem(str(equipo[3])))  # victorias
            self.ui.tableWidget_lista_equipos.setItem(fila, 2, QTableWidgetItem(str(equipo[4])))  # goles
            self.ui.tableWidget_lista_equipos.setItem(fila, 3, QTableWidgetItem(str(equipo[5])))  # faltas
            self.ui.tableWidget_lista_equipos.setItem(fila, 4, QTableWidgetItem(str(equipo[6])))  # amarillas
            self.ui.tableWidget_lista_equipos.setItem(fila, 5, QTableWidgetItem(str(equipo[7])))  # rojas
            self.ui.tableWidget_lista_equipos.setItem(fila, 6, QTableWidgetItem(str(equipo[8])))  # paradas

    def editar_equipo(self):
        """Abre la vista de edición del equipo seleccionado"""
        fila_seleccionada = self.ui.tableWidget_lista_equipos.currentRow()
        
        if fila_seleccionada < 0:
            QMessageBox.warning(self, "Sin selección", "Debe seleccionar un equipo para editar.")
            return
        
        # Obtener el ID del equipo
        item = self.ui.tableWidget_lista_equipos.item(fila_seleccionada, 0)
        equipo_id = item.data(Qt.UserRole)
        
        # Cambiar a la vista de registro de equipos en modo edición
        if self.parent_controller:
            self.parent_controller.vista_equipos.configurar_modo_edicion(equipo_id)
            self.parent_controller.ui.stackedWidget.setCurrentWidget(self.parent_controller.vista_equipos)
            self.parent_controller.ui.titulo.setText("📝 Editar Equipo 📝")

    def configurar_estatica(self):

        estilo_botones = (
            "font-size: 11pt; font-weight: bold; color: #267E7E; "
            "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
        )

        self.ui.pushButton_buscar_equipos.setStyleSheet(estilo_botones)
        self.ui.pushButton_buscar_equipos.setText("🔎 Buscar")
        
        self.ui.pushButton_editar_equipos.setStyleSheet(estilo_botones)
        self.ui.pushButton_editar_equipos.setText("📝 Editar")
        
        self.ui.pushButton_lista_equipos_volver.setStyleSheet(estilo_botones)
        self.ui.pushButton_lista_equipos_volver.setText("↩️ Volver")

        self.ui.groupBox_datos_equipo.setTitle("Filtros de Busqueda 📋")

        self.ui.lineEdit_nombre_equipo_filtro.setPlaceholderText("👕 Nombre Equipo")

        # Desactivar colores alternados
        self.ui.tableWidget_lista_equipos.setAlternatingRowColors(False)
        
        header = self.ui.tableWidget_lista_equipos.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)



        # --- CABECERAS DE LA TABLA ---
        headers = [
            "👕 Equipo", "🏆 Partidos Ganados", "⚽ Goles", 
             "🗣️❌ Faltas", "🟨 Amarillas", "🟥 Rojas", "🧤Paradas"
        ]
        for i, text in enumerate(headers):
            item = self.ui.tableWidget_lista_equipos.horizontalHeaderItem(i)
            if item:
                item.setText(text)


