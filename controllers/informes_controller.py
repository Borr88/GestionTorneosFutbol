import os
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from views.ui.informes_ui import Ui_Dialog
from pyreportjasper import PyReportJasper


class InformesController(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db

        self.setWindowTitle("Generación de Informes - Torneo")
        self.cargar_filtros()
        self.actualizar_estado_filtros()
        self.setup_conexiones()

# CONEXIONES DE BOTONES --------------------------------------

    def setup_conexiones(self):
        """Conecta los controles de la vista con sus funciones"""
        self.ui.comboBox_tipo_informe.currentIndexChanged.connect(self.actualizar_estado_filtros)
        self.ui.toolButton_selec_ruta.clicked.connect(self.seleccionar_ruta)
        self.ui.pushButton_generar_pdf.clicked.connect(self.generar_pdf)

# CARGA DE FILTROS ------------------------------------------

    def cargar_filtros(self):
        """Carga los datos en los combobox de filtros desde la base de datos"""
        self.ui.comboBox_filtro_equipo.clear()
        self.ui.comboBox_filtro_equipo.addItem("Todos los Equipos")

        try:
            equipos = self.db.obtener_equipos()
            for equipo in equipos:
                self.ui.comboBox_filtro_equipo.addItem(equipo[1], userData=equipo[0])
        except Exception as e:
            print(f"Error al cargar equipos: {e}")

        self.ui.comboBox_filtro_ronda.clear()
        self.ui.comboBox_filtro_ronda.addItem("Todas las Rondas")
        rondas_fijas = ["Octavos", "Cuartos", "Semifinal", "Final"]
        self.ui.comboBox_filtro_ronda.addItems(rondas_fijas)

    def actualizar_estado_filtros(self, index=None):
        """Habilita o deshabilita los filtros según el tipo de informe seleccionado"""
        tipo_informe = self.ui.comboBox_tipo_informe.currentText()

        if tipo_informe == "Equipos y Jugadores":
            self.ui.comboBox_filtro_equipo.setEnabled(True)
            self.ui.comboBox_filtro_ronda.setEnabled(False)
        else:
            self.ui.comboBox_filtro_equipo.setEnabled(False)
            self.ui.comboBox_filtro_ronda.setEnabled(True)

# SELECCIÓN DE RUTA -----------------------------------------

    def seleccionar_ruta(self):
        """Abre un diálogo para seleccionar la carpeta donde se guardará el PDF"""
        directorio_inicial = os.path.join(os.getcwd(), "reports")
        if not os.path.exists(directorio_inicial):
            os.makedirs(directorio_inicial)

        carpeta_seleccionada = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar Carpeta Destino",
            directorio_inicial
        )

        if carpeta_seleccionada:
            self.ui.lineEdit_ruta_destino.setText(carpeta_seleccionada)

# GENERACIÓN DE INFORME PDF ----------------------------------

    def generar_pdf(self):
        """Determina el informe seleccionado, construye los parámetros y genera el PDF con Jasper"""
        tipo_informe = self.ui.comboBox_tipo_informe.currentText()
        ruta_destino_carpeta = self.ui.lineEdit_ruta_destino.text()

        if not ruta_destino_carpeta:
            QMessageBox.warning(self, "Atención", "Por favor, seleccione una carpeta de destino.")
            return

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_jar = os.path.join(base_dir, "reports", "sqlite-jdbc.jar")
        ruta_db = os.path.join(base_dir, "torneo_futbol.db")

        params = {}

        if tipo_informe == "Equipos y Jugadores":
            ruta_jrxml = os.path.join(base_dir, "reports", "equipos_jugadores.jrxml")
            ruta_pdf = os.path.join(ruta_destino_carpeta, "Informe_Equipos_Jugadores.pdf")
            if self.ui.comboBox_filtro_equipo.currentIndex() > 0:
                params['ID_EQUIPO'] = int(self.ui.comboBox_filtro_equipo.currentData())

        elif tipo_informe == "Partidos y resultados":
            ruta_jrxml = os.path.join(base_dir, "reports", "partidos.jrxml")
            ruta_pdf = os.path.join(ruta_destino_carpeta, "Informe_Partidos.pdf")
            if self.ui.comboBox_filtro_ronda.currentIndex() > 0:
                params['FASE'] = self.ui.comboBox_filtro_ronda.currentText()

        elif tipo_informe == "Clasificacion y Eliminatorias":
            ruta_jrxml = os.path.join(base_dir, "reports", "clasificacion.jrxml")
            ruta_pdf = os.path.join(ruta_destino_carpeta, "Informe_Clasificacion.pdf")
            if self.ui.comboBox_filtro_ronda.currentIndex() > 0:
                params['FASE'] = self.ui.comboBox_filtro_ronda.currentText()

        else:
            QMessageBox.warning(self, "Atención", "Este informe aún no está configurado.")
            return

        db_conn = {
            'driver': 'generic',
            'jdbc_driver': 'org.sqlite.JDBC',
            'jdbc_url': f'jdbc:sqlite:{ruta_db}',
            'jdbc_dir': ruta_jar
        }

        try:
            self.ui.pushButton_generar_pdf.setText("Generando...")
            self.ui.pushButton_generar_pdf.setEnabled(False)
            self.repaint()

            pyjasper = PyReportJasper()
            pyjasper.config(
                input_file=ruta_jrxml,
                output_file=ruta_pdf,
                output_formats=["pdf"],
                parameters=params,
                db_connection=db_conn
            )
            pyjasper.process_report()

            QMessageBox.information(self, "Éxito", f"Informe generado correctamente en:\n{ruta_pdf}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ha ocurrido un error al generar el PDF:\n{str(e)}")

        finally:
            self.ui.pushButton_generar_pdf.setText("Generar Informe PDF")
            self.ui.pushButton_generar_pdf.setEnabled(True)