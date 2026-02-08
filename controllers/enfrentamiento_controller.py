from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from views.ui.enfrentamiento_ui import Ui_Enfrentamiento


class EnfrentamientoController(QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_controller = parent
        self.ui = Ui_Enfrentamiento()
        self.ui.setupUi(self)

        self.configurar_estatica()
        self.setup_conexiones()
        self.cargar_datos_iniciales()
        self.cargar_partidos_existentes()

    def setup_conexiones(self):
        """Conecta los botones y combobox con sus funciones"""
        self.ui.pushButton_enfrentar.clicked.connect(self.crear_enfrentamiento)
        self.ui.comboBox_equipoA_enfrentamiento.currentIndexChanged.connect(self.cargar_escudo_equipoA)
        self.ui.comboBox_equipoB_enfrentamiento.currentIndexChanged.connect(self.cargar_escudo_equipoB)
        self.ui.dateEdit_fecha_enfrentamiento.dateChanged.connect(self.actualizar_arbitros_disponibles)

    def cargar_datos_iniciales(self):
        """Carga los equipos y árbitros en los combobox"""
        # Obtener equipos disponibles (no comprometidos en partidos)
        equipos_disponibles = self.obtener_equipos_disponibles()
        
        # Cargar equipos
        self.ui.comboBox_equipoA_enfrentamiento.clear()
        self.ui.comboBox_equipoB_enfrentamiento.clear()
        self.ui.comboBox_equipoA_enfrentamiento.addItem("Seleccionar Equipo A", 0)
        self.ui.comboBox_equipoB_enfrentamiento.addItem("Seleccionar Equipo B", 0)
        
        for equipo_id, nombre in equipos_disponibles:
            self.ui.comboBox_equipoA_enfrentamiento.addItem(nombre, equipo_id)
            self.ui.comboBox_equipoB_enfrentamiento.addItem(nombre, equipo_id)
        
        # Cargar árbitros
        self.actualizar_arbitros_disponibles()
    
    def obtener_equipos_disponibles(self):
        """Obtiene solo los equipos que no están comprometidos en partidos octavos"""
        todos_equipos = self.db.obtener_equipos()
        
        # Obtener equipos que ya tienen un partido en Octavos
        partidos_octavos = self.db.obtener_partidos_por_fase("Octavos")
        equipos_comprometidos = set()
        
        for partido in partidos_octavos:
            # partido: (id, equipo_local, equipo_visitante, fecha_hora, fase, goles_local, goles_visitante)
            if partido[1]:  # equipo_local
                # Buscar el ID del equipo por nombre
                for equipo_id, nombre in todos_equipos:
                    if nombre == partido[1]:
                        equipos_comprometidos.add(equipo_id)
                        break
            if partido[2]:  # equipo_visitante
                for equipo_id, nombre in todos_equipos:
                    if nombre == partido[2]:
                        equipos_comprometidos.add(equipo_id)
                        break
        
        # Retornar solo equipos no comprometidos
        equipos_disponibles = [
            (equipo_id, nombre) for equipo_id, nombre in todos_equipos 
            if equipo_id not in equipos_comprometidos
        ]
        
        return equipos_disponibles

    def actualizar_arbitros_disponibles(self):
        """Actualiza la lista de árbitros disponibles según la fecha seleccionada"""
        fecha = self.ui.dateEdit_fecha_enfrentamiento.date().toString("yyyy-MM-dd")
        
        self.ui.comboBox_arbitro_enfrentamiento.clear()
        self.ui.comboBox_arbitro_enfrentamiento.addItem("Seleccionar Árbitro", 0)
        
        arbitros = self.db.obtener_arbitros_disponibles(fecha)
        for arbitro_id, nombre, apellido in arbitros:
            nombre_completo = f"{nombre} {apellido}"
            self.ui.comboBox_arbitro_enfrentamiento.addItem(nombre_completo, arbitro_id)

    def cargar_escudo_equipoA(self):
        """Carga el escudo del equipo A cuando se selecciona"""
        equipo_id = self.ui.comboBox_equipoA_enfrentamiento.currentData()
        if equipo_id and equipo_id != 0:
            equipo = self.db.obtener_equipo_por_id(equipo_id)
            if equipo and equipo[4]:  # escudo_path
                pixmap = QPixmap(equipo[4])
                self.ui.label_campo_izq.setPixmap(pixmap.scaled(
                    self.ui.label_campo_izq.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.ui.label_campo_izq.clear()
                self.ui.label_campo_izq.setText("Sin escudo")
        else:
            self.ui.label_campo_izq.clear()
            self.ui.label_campo_izq.setText("Equipo A")

    def cargar_escudo_equipoB(self):
        """Carga el escudo del equipo B cuando se selecciona"""
        equipo_id = self.ui.comboBox_equipoB_enfrentamiento.currentData()
        if equipo_id and equipo_id != 0:
            equipo = self.db.obtener_equipo_por_id(equipo_id)
            if equipo and equipo[4]:  # escudo_path
                pixmap = QPixmap(equipo[4])
                self.ui.label_campo_der.setPixmap(pixmap.scaled(
                    self.ui.label_campo_der.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.ui.label_campo_der.clear()
                self.ui.label_campo_der.setText("Sin escudo")
        else:
            self.ui.label_campo_der.clear()
            self.ui.label_campo_der.setText("Equipo B")

    def crear_enfrentamiento(self):
        """Crea un nuevo enfrentamiento/partido"""
        # Validaciones
        equipo_a_id = self.ui.comboBox_equipoA_enfrentamiento.currentData()
        equipo_b_id = self.ui.comboBox_equipoB_enfrentamiento.currentData()
        arbitro_id = self.ui.comboBox_arbitro_enfrentamiento.currentData()
        fecha = self.ui.dateEdit_fecha_enfrentamiento.date().toString("yyyy-MM-dd HH:mm:ss")
        
        errores = []
        
        if not equipo_a_id or equipo_a_id == 0:
            errores.append("- Debe seleccionar el Equipo A")
        
        if not equipo_b_id or equipo_b_id == 0:
            errores.append("- Debe seleccionar el Equipo B")
        
        if equipo_a_id == equipo_b_id and equipo_a_id != 0:
            errores.append("- Los equipos A y B no pueden ser el mismo")
        
        if not arbitro_id or arbitro_id == 0:
            errores.append("- Debe seleccionar un árbitro")
        
        if errores:
            mensaje = "Por favor, corrija los siguientes errores:\n" + "\n".join(errores)
            QMessageBox.warning(self, "Datos incompletos", mensaje)
            return
        
        # Insertar el partido en la base de datos
        exito = self.db.insertar_partido(equipo_a_id, equipo_b_id, arbitro_id, fecha, "Octavos")
        
        if exito:
            nombre_a = self.ui.comboBox_equipoA_enfrentamiento.currentText()
            nombre_b = self.ui.comboBox_equipoB_enfrentamiento.currentText()
            QMessageBox.information(
                self,
                "Enfrentamiento creado",
                f"El enfrentamiento entre {nombre_a} y {nombre_b} ha sido registrado correctamente."
            )
            # Limpiar formulario
            self.limpiar_formulario()
            # Recargar datos iniciales para actualizar equipos disponibles
            self.cargar_datos_iniciales()
            # Actualizar lista de árbitros
            self.actualizar_arbitros_disponibles()
            # Mostrar partidos actualizados
            self.cargar_partidos_existentes()
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el enfrentamiento.")

    def limpiar_formulario(self):
        """Limpia el formulario de enfrentamientos"""
        self.ui.comboBox_equipoA_enfrentamiento.setCurrentIndex(0)
        self.ui.comboBox_equipoB_enfrentamiento.setCurrentIndex(0)
        self.ui.comboBox_arbitro_enfrentamiento.setCurrentIndex(0)
        self.ui.label_campo_izq.clear()
        self.ui.label_campo_izq.setText("Equipo A")
        self.ui.label_campo_der.clear()
        self.ui.label_campo_der.setText("Equipo B")

    def configurar_estatica(self):

        estilo_botones = (
            "font-size: 11pt; font-weight: bold; color: #267E7E; "
            "background-color: #FF9501; border-radius: 10px; border: 2px solid #A35F00;"
        )

        self.ui.pushButton_enfrentar.setStyleSheet(estilo_botones)
        self.ui.pushButton_enfrentar.setText("⚔️ Enfrentar")

        self.ui.pushButton_volver_enfrentamientos.setStyleSheet(estilo_botones)
        self.ui.pushButton_volver_enfrentamientos.setText("↩️ Volver")
    
    def cargar_partidos_existentes(self):
        """Carga y muestra los partidos ya configurados en la consola"""
        partidos = self.db.obtener_partidos_por_fase(None)
        
        if partidos:
            print("\n" + "="*80)
            print("PARTIDOS CONFIGURADOS")
            print("="*80)
            for idx, partido in enumerate(partidos, 1):
                # partido: (id, equipo_local, equipo_visitante, fecha_hora, fase, goles_local, goles_visitante)
                partido_id = partido[0]
                equipo_local = partido[1]
                equipo_visitante = partido[2]
                fecha_hora = partido[3] if partido[3] else "Sin fecha asignada"
                fase = partido[4]
                goles_local = partido[5]
                goles_visitante = partido[6]
                
                print(f"\n{idx}. {equipo_local} vs {equipo_visitante}")
                print(f"   Fase: {fase} | Fecha: {fecha_hora}")
                print(f"   Resultado: {goles_local} - {goles_visitante}")
            print("\n" + "="*80 + "\n")
        else:
            print("\nNo hay partidos configurados aun.\n")