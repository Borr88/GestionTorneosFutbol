from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from views.ui.calendario_ui import Ui_Calendario

class CalendarioController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_controller = parent
        self.ui = Ui_Calendario()
        self.ui.setupUi(self)

        self.configurar_estatica()
        self.setup_conexiones()
        self.cargar_partidos()

    def setup_conexiones(self):
        """Conecta los botones y combobox con sus funciones"""
        self.ui.comboBox_seleccion_fases.currentIndexChanged.connect(self.cambiar_fase)
        self.ui.pushButton_asignar_fecha.clicked.connect(self.asignar_fecha)
        self.ui.tableWidget_calendario.itemSelectionChanged.connect(self.seleccion_cambiada)

    def cargar_partidos(self):
        """Carga todos los partidos en la tabla según la fase seleccionada"""
        fase = self.ui.comboBox_seleccion_fases.currentText()
        
        if fase == "Selección Fase" or not fase:
            # Obtener todos los partidos sin filtro de fase, solo los que tienen fecha
            todos_partidos = self.db.obtener_partidos_por_fase(None)
            # Filtrar solo aquellos que tienen fecha asignada
            partidos = [p for p in todos_partidos if p[3] is not None]
        else:
            partidos = self.db.obtener_partidos_por_fase(fase)
        
        self.actualizar_tabla(partidos)

    def actualizar_tabla(self, partidos):
        """Actualiza la tabla con los datos de partidos"""
        self.ui.tableWidget_calendario.setRowCount(0)
        
        for partido in partidos:
            # partido: (id, equipo_local, equipo_visitante, fecha_hora, fase, goles_local, goles_visitante)
            fila = self.ui.tableWidget_calendario.rowCount()
            self.ui.tableWidget_calendario.insertRow(fila)
            
            # Guardar el ID en la primera columna (Equipo A)
            item_local = QTableWidgetItem(partido[1])
            item_local.setData(Qt.UserRole, partido[0])  # Guardar ID del partido
            self.ui.tableWidget_calendario.setItem(fila, 0, item_local)
            
            # Fecha
            if partido[3]:
                fecha_str = str(partido[3])
            else:
                fecha_str = "Sin fecha asignada"
            self.ui.tableWidget_calendario.setItem(fila, 1, QTableWidgetItem(fecha_str))
            
            # Equipo visitante (Equipo B)
            self.ui.tableWidget_calendario.setItem(fila, 2, QTableWidgetItem(partido[2]))

    def cambiar_fase(self):
        """Maneja el cambio de fase en el combobox"""
        fase = self.ui.comboBox_seleccion_fases.currentText()
        
        # Mostrar u ocultar controles de fecha según la fase
        if fase in ["Cuartos", "Semifinales", "Final"]:
            self.ui.dateEdit_fecha.setVisible(True)
            self.ui.pushButton_asignar_fecha.setVisible(True)
        else:
            self.ui.dateEdit_fecha.setVisible(False)
            self.ui.pushButton_asignar_fecha.setVisible(False)
        
        # Recargar partidos
        self.cargar_partidos()

    def seleccion_cambiada(self):
        """Se ejecuta cuando se selecciona un partido en la tabla"""
        pass  # Por ahora no hace nada, pero está listo para futuras funcionalidades

    def asignar_fecha(self):
        """Asigna una fecha al partido seleccionado"""
        fila_seleccionada = self.ui.tableWidget_calendario.currentRow()
        
        if fila_seleccionada < 0:
            QMessageBox.warning(self, "Sin selección", "Debe seleccionar un partido para asignar fecha.")
            return
        
        # Obtener el ID del partido
        item = self.ui.tableWidget_calendario.item(fila_seleccionada, 0)
        partido_id = item.data(Qt.UserRole)
        
        # Obtener la fecha seleccionada
        fecha = self.ui.dateEdit_fecha.date().toString("yyyy-MM-dd HH:mm:ss")
        
        # Actualizar la fecha en la base de datos
        exito = self.db.actualizar_fecha_partido(partido_id, fecha)
        
        if exito:
            QMessageBox.information(self, "Fecha asignada", "La fecha ha sido asignada correctamente al partido.")
            self.cargar_partidos()  # Recargar la tabla
        else:
            QMessageBox.critical(self, "Error", "No se pudo asignar la fecha al partido.")

    def configurar_estatica(self):

        estilo_botones = (
            "font-size: 11pt; font-weight: bold; color: #267E7E; "
            "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
        )

        self.ui.pushButton_volver_calendario.setStyleSheet(estilo_botones)
        self.ui.pushButton_volver_calendario.setText("Volver")
        self.ui.pushButton_asignar_fecha.setText("Asignar Fecha")

        # Desactivar colores alternados y establecer un estilo uniforme
        self.ui.tableWidget_calendario.setAlternatingRowColors(False)
        estilo_tabla = (
            "QTableWidget { background-color: #1B5A5A; color: white; }"
            "QTableWidget::item { padding: 5px; background-color: #1B5A5A; color: white; border: 1px solid #267E7E; }"
            "QTableWidget::item:selected { background-color: #267E7E; }"
            "QHeaderView::section { background-color: #0D3A3A; color: white; padding: 5px; border: 1px solid #267E7E; }"
        )
        self.ui.tableWidget_calendario.setStyleSheet(estilo_tabla)

        self.ui.tableWidget_calendario.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        headers = [
            "Equipo A", "Fecha", "Equipo B"
        ]

        for i, text in enumerate(headers):
            item = self.ui.tableWidget_calendario.horizontalHeaderItem(i)
            if item:
                item.setText(text)