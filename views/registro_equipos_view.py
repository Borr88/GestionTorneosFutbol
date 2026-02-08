"""
Vista para el registro de equipos del torneo de fútbol
Incluye carga de iconos y manejo de eventos
"""
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, Signal
from ui.registro_equipos_ui import Ui_Form  # Importar el .ui compilado


class RegistroEquiposView(QWidget):
    """Vista para registro y gestión de equipos"""
    
    # Señales para comunicación con el controlador
    equipo_registrado = Signal(dict)
    jugador_creado = Signal()
    jugador_eliminado = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Variables para almacenar rutas de imágenes
        self.ruta_escudo = None
        self.ruta_equipacion = None
        
        # Configurar interfaz
        self._configurar_iconos()
        self._conectar_senales()
        self._configurar_tabla()
        
    def _configurar_iconos(self):
        """Configura los iconos de los botones usando la librería de iconos"""
        ruta_iconos = Path("resources/iconos")
        
        # Iconos para botones principales
        self.ui.pushButton_registrar.setIcon(
            QIcon(str(ruta_iconos / "save.png"))
        )
        self.ui.pushButton_limpiar.setIcon(
            QIcon(str(ruta_iconos / "clean.png"))
        )
        self.ui.pushButton_crear_jugador.setIcon(
            QIcon(str(ruta_iconos / "add-user.png"))
        )
        self.ui.pushButton_eliminar_jugador.setIcon(
            QIcon(str(ruta_iconos / "remove-user.png"))
        )
        self.ui.pushButton_cargar_escudo.setIcon(
            QIcon(str(ruta_iconos / "upload.png"))
        )
        self.ui.pushButton_cargar_equipacion.setIcon(
            QIcon(str(ruta_iconos / "upload.png"))
        )
        
        # Configurar icono de la ventana
        self.setWindowIcon(QIcon(str(ruta_iconos / "football.png")))
        
    def _conectar_senales(self):
        """Conecta las señales de los widgets con los slots correspondientes"""
        # Botones principales
        self.ui.pushButton_registrar.clicked.connect(self._registrar_equipo)
        self.ui.pushButton_limpiar.clicked.connect(self._limpiar_formulario)
        self.ui.pushButton_crear_jugador.clicked.connect(self._crear_jugador)
        self.ui.pushButton_eliminar_jugador.clicked.connect(self._eliminar_jugador)
        
        # Botones de carga de imágenes
        self.ui.pushButton_cargar_escudo.clicked.connect(self._cargar_escudo)
        self.ui.pushButton_cargar_equipacion.clicked.connect(self._cargar_equipacion)
        
    def _configurar_tabla(self):
        """Configura las propiedades de la tabla de jugadores"""
        # Ajustar ancho de columnas
        header = self.ui.tableWidget_jugadores.horizontalHeader()
        header.setStretchLastSection(True)
        
        # Configurar selección
        self.ui.tableWidget_jugadores.setSelectionBehavior(
            self.ui.tableWidget_jugadores.SelectionBehavior.SelectRows
        )
        
    def _cargar_escudo(self):
        """Abre un diálogo para seleccionar la imagen del escudo"""
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar escudo del equipo",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )
        
        if archivo:
            self.ruta_escudo = archivo
            pixmap = QPixmap(archivo)
            # Escalar la imagen manteniendo la proporción
            pixmap_escalado = pixmap.scaled(
                150, 150,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.label_escudo.setPixmap(pixmap_escalado)
            self.ui.label_escudo.setText("")
            
    def _cargar_equipacion(self):
        """Abre un diálogo para seleccionar la imagen de la equipación"""
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar imagen de equipación",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )
        
        if archivo:
            self.ruta_equipacion = archivo
            pixmap = QPixmap(archivo)
            pixmap_escalado = pixmap.scaled(
                150, 150,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.label_equipacion.setPixmap(pixmap_escalado)
            self.ui.label_equipacion.setText("")
            
    def _registrar_equipo(self):
        """Valida y registra un nuevo equipo"""
        # Validar campos obligatorios
        nombre = self.ui.lineEdit_nombre_equipo.text().strip()
        curso = self.ui.comboBox_curso.currentText()
        color = self.ui.lineEdit_equipacion.text().strip()
        
        if not nombre:
            QMessageBox.warning(
                self,
                "Campo requerido",
                "El nombre del equipo es obligatorio"
            )
            self.ui.lineEdit_nombre_equipo.setFocus()
            return
            
        if curso == "Seleccionar Curso":
            QMessageBox.warning(
                self,
                "Campo requerido",
                "Debe seleccionar un curso"
            )
            self.ui.comboBox_curso.setFocus()
            return
            
        if not color:
            QMessageBox.warning(
                self,
                "Campo requerido",
                "El color de la equipación es obligatorio"
            )
            self.ui.lineEdit_equipacion.setFocus()
            return
        
        # Crear diccionario con los datos del equipo
        datos_equipo = {
            'nombre': nombre,
            'curso': curso,
            'color': color,
            'escudo': self.ruta_escudo,
            'equipacion': self.ruta_equipacion
        }
        
        # Emitir señal con los datos
        self.equipo_registrado.emit(datos_equipo)
        
        # Mensaje de confirmación
        QMessageBox.information(
            self,
            "Equipo registrado",
            f"El equipo '{nombre}' ha sido registrado correctamente"
        )
        
        # Limpiar formulario
        self._limpiar_formulario()
        
    def _limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        self.ui.lineEdit_nombre_equipo.clear()
        self.ui.comboBox_curso.setCurrentIndex(0)
        self.ui.lineEdit_equipacion.clear()
        
        # Limpiar imágenes
        self.ui.label_escudo.clear()
        self.ui.label_escudo.setText("Sin imagen")
        self.ui.label_equipacion.clear()
        self.ui.label_equipacion.setText("Sin imagen")
        
        self.ruta_escudo = None
        self.ruta_equipacion = None
        
        # Establecer foco en el primer campo
        self.ui.lineEdit_nombre_equipo.setFocus()
        
    def _crear_jugador(self):
        """Emite señal para abrir diálogo de creación de jugador"""
        self.jugador_creado.emit()
        
    def _eliminar_jugador(self):
        """Elimina el jugador seleccionado de la tabla"""
        fila_seleccionada = self.ui.tableWidget_jugadores.currentRow()
        
        if fila_seleccionada < 0:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Debe seleccionar un jugador para eliminar"
            )
            return
        
        # Obtener nombre del jugador para confirmación
        nombre = self.ui.tableWidget_jugadores.item(fila_seleccionada, 0).text()
        apellido = self.ui.tableWidget_jugadores.item(fila_seleccionada, 1).text()
        
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de eliminar a {nombre} {apellido}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            # Emitir señal con el ID del jugador (asumiendo que está en los datos)
            self.jugador_eliminado.emit(fila_seleccionada)
            self.ui.tableWidget_jugadores.removeRow(fila_seleccionada)
            
    def agregar_jugador_tabla(self, datos_jugador):
        """
        Agrega un jugador a la tabla
        
        Args:
            datos_jugador (dict): Diccionario con nombre, apellido, curso, posicion
        """
        fila = self.ui.tableWidget_jugadores.rowCount()
        self.ui.tableWidget_jugadores.insertRow(fila)
        
        self.ui.tableWidget_jugadores.setItem(fila, 0, 
            QTableWidgetItem(datos_jugador.get('nombre', '')))
        self.ui.tableWidget_jugadores.setItem(fila, 1, 
            QTableWidgetItem(datos_jugador.get('apellido', '')))
        self.ui.tableWidget_jugadores.setItem(fila, 2, 
            QTableWidgetItem(datos_jugador.get('curso', '')))
        self.ui.tableWidget_jugadores.setItem(fila, 3, 
            QTableWidgetItem(datos_jugador.get('posicion', '')))
            
    def actualizar_tabla_jugadores(self, lista_jugadores):
        """
        Actualiza la tabla con una lista completa de jugadores
        
        Args:
            lista_jugadores (list): Lista de diccionarios con datos de jugadores
        """
        self.ui.tableWidget_jugadores.setRowCount(0)
        for jugador in lista_jugadores:
            self.agregar_jugador_tabla(jugador)


def main():
    """Función principal para pruebas"""
    app = QApplication(sys.argv)
    
    # Cargar hoja de estilos
    try:
        with open("resources/qss/style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Advertencia: No se encontró el archivo de estilos")
    
    ventana = RegistroEquiposView()
    ventana.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()