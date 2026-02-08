# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_equipos.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Registro_Equipos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(934, 668)
        Form.setStyleSheet(u"QWidget#Form {\n"
"	background-color: rgb(94, 207, 207);\n"
"}")
        self.verticalLayout_main = QVBoxLayout(Form)
        self.verticalLayout_main.setSpacing(15)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_contenido = QHBoxLayout()
        self.horizontalLayout_contenido.setSpacing(20)
        self.horizontalLayout_contenido.setObjectName(u"horizontalLayout_contenido")
        self.verticalLayout_izquierda = QVBoxLayout()
        self.verticalLayout_izquierda.setSpacing(5)
        self.verticalLayout_izquierda.setObjectName(u"verticalLayout_izquierda")
        self.groupBox_datos_equipo = QGroupBox(Form)
        self.groupBox_datos_equipo.setObjectName(u"groupBox_datos_equipo")
        self.groupBox_datos_equipo.setMinimumSize(QSize(0, 120))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox_datos_equipo.setFont(font)
        self.verticalLayout_formulario = QVBoxLayout(self.groupBox_datos_equipo)
        self.verticalLayout_formulario.setSpacing(10)
        self.verticalLayout_formulario.setObjectName(u"verticalLayout_formulario")
        self.verticalLayout_formulario.setContentsMargins(15, 20, 15, 15)
        self.horizontalLayout_campos = QHBoxLayout()
        self.horizontalLayout_campos.setSpacing(10)
        self.horizontalLayout_campos.setObjectName(u"horizontalLayout_campos")
        self.lineEdit_nombre_equipo = QLineEdit(self.groupBox_datos_equipo)
        self.lineEdit_nombre_equipo.setObjectName(u"lineEdit_nombre_equipo")
        self.lineEdit_nombre_equipo.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_nombre_equipo.setFont(font1)
        self.lineEdit_nombre_equipo.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.horizontalLayout_campos.addWidget(self.lineEdit_nombre_equipo)

        self.comboBox_curso_equipo = QComboBox(self.groupBox_datos_equipo)
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.addItem("")
        self.comboBox_curso_equipo.setObjectName(u"comboBox_curso_equipo")
        self.comboBox_curso_equipo.setMinimumSize(QSize(150, 40))
        self.comboBox_curso_equipo.setFont(font1)
        self.comboBox_curso_equipo.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.horizontalLayout_campos.addWidget(self.comboBox_curso_equipo)

        self.lineEdit_color_equipo = QLineEdit(self.groupBox_datos_equipo)
        self.lineEdit_color_equipo.setObjectName(u"lineEdit_color_equipo")
        self.lineEdit_color_equipo.setMinimumSize(QSize(150, 40))
        self.lineEdit_color_equipo.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_color_equipo.setFont(font1)
        self.lineEdit_color_equipo.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.horizontalLayout_campos.addWidget(self.lineEdit_color_equipo)


        self.verticalLayout_formulario.addLayout(self.horizontalLayout_campos)


        self.verticalLayout_izquierda.addWidget(self.groupBox_datos_equipo)

        self.tableWidget_jugadores_equipo = QTableWidget(Form)
        if (self.tableWidget_jugadores_equipo.columnCount() < 4):
            self.tableWidget_jugadores_equipo.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_jugadores_equipo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_jugadores_equipo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_jugadores_equipo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_jugadores_equipo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_jugadores_equipo.setObjectName(u"tableWidget_jugadores_equipo")
        self.tableWidget_jugadores_equipo.setFont(font1)
        self.tableWidget_jugadores_equipo.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_jugadores_equipo.setAlternatingRowColors(True)
        self.tableWidget_jugadores_equipo.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_jugadores_equipo.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_jugadores_equipo.setSortingEnabled(True)
        self.tableWidget_jugadores_equipo.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_izquierda.addWidget(self.tableWidget_jugadores_equipo)

        self.verticalLayout_izquierda.setStretch(1, 10)

        self.horizontalLayout_contenido.addLayout(self.verticalLayout_izquierda)

        self.verticalLayout_derecha = QVBoxLayout()
        self.verticalLayout_derecha.setSpacing(4)
        self.verticalLayout_derecha.setObjectName(u"verticalLayout_derecha")
        self.groupBox_escudo = QGroupBox(Form)
        self.groupBox_escudo.setObjectName(u"groupBox_escudo")
        self.groupBox_escudo.setMinimumSize(QSize(0, 200))
        self.groupBox_escudo.setFont(font)
        self.verticalLayout_escudo = QVBoxLayout(self.groupBox_escudo)
        self.verticalLayout_escudo.setSpacing(10)
        self.verticalLayout_escudo.setObjectName(u"verticalLayout_escudo")
        self.label_imagen_escudo = QLabel(self.groupBox_escudo)
        self.label_imagen_escudo.setObjectName(u"label_imagen_escudo")
        self.label_imagen_escudo.setMinimumSize(QSize(150, 150))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_imagen_escudo.setFont(font2)
        self.label_imagen_escudo.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;\n"
"}")
        self.label_imagen_escudo.setScaledContents(True)
        self.label_imagen_escudo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_escudo.addWidget(self.label_imagen_escudo)

        self.pushButton_cargar_escudo = QPushButton(self.groupBox_escudo)
        self.pushButton_cargar_escudo.setObjectName(u"pushButton_cargar_escudo")
        self.pushButton_cargar_escudo.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_cargar_escudo.setFont(font3)
        self.pushButton_cargar_escudo.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.verticalLayout_escudo.addWidget(self.pushButton_cargar_escudo)


        self.verticalLayout_derecha.addWidget(self.groupBox_escudo)

        self.groupBox_equipacion = QGroupBox(Form)
        self.groupBox_equipacion.setObjectName(u"groupBox_equipacion")
        self.groupBox_equipacion.setMinimumSize(QSize(0, 200))
        self.groupBox_equipacion.setFont(font)
        self.verticalLayout_equipacion = QVBoxLayout(self.groupBox_equipacion)
        self.verticalLayout_equipacion.setSpacing(10)
        self.verticalLayout_equipacion.setObjectName(u"verticalLayout_equipacion")
        self.label_imagen_equipacion = QLabel(self.groupBox_equipacion)
        self.label_imagen_equipacion.setObjectName(u"label_imagen_equipacion")
        self.label_imagen_equipacion.setMinimumSize(QSize(150, 150))
        self.label_imagen_equipacion.setFont(font2)
        self.label_imagen_equipacion.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(27, 90, 90);\n"
"	color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;\n"
"}")
        self.label_imagen_equipacion.setScaledContents(True)
        self.label_imagen_equipacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_equipacion.addWidget(self.label_imagen_equipacion)

        self.pushButton_cargar_equipacion = QPushButton(self.groupBox_equipacion)
        self.pushButton_cargar_equipacion.setObjectName(u"pushButton_cargar_equipacion")
        self.pushButton_cargar_equipacion.setMinimumSize(QSize(0, 40))
        self.pushButton_cargar_equipacion.setFont(font3)
        self.pushButton_cargar_equipacion.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.verticalLayout_equipacion.addWidget(self.pushButton_cargar_equipacion)


        self.verticalLayout_derecha.addWidget(self.groupBox_equipacion)

        self.verticalLayout_derecha.setStretch(0, 10)
        self.verticalLayout_derecha.setStretch(1, 10)

        self.horizontalLayout_contenido.addLayout(self.verticalLayout_derecha)

        self.horizontalLayout_contenido.setStretch(0, 10)
        self.horizontalLayout_contenido.setStretch(1, 1)

        self.verticalLayout_main.addLayout(self.horizontalLayout_contenido)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_main.addWidget(self.line)

        self.horizontalLayout_botones = QHBoxLayout()
        self.horizontalLayout_botones.setSpacing(10)
        self.horizontalLayout_botones.setObjectName(u"horizontalLayout_botones")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_botones.addItem(self.horizontalSpacer)

        self.pushButton_registrar_equipo = QPushButton(Form)
        self.pushButton_registrar_equipo.setObjectName(u"pushButton_registrar_equipo")
        self.pushButton_registrar_equipo.setMinimumSize(QSize(140, 45))
        self.pushButton_registrar_equipo.setFont(font)
        self.pushButton_registrar_equipo.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_botones.addWidget(self.pushButton_registrar_equipo)

        self.pushButton_limpiar_equipo = QPushButton(Form)
        self.pushButton_limpiar_equipo.setObjectName(u"pushButton_limpiar_equipo")
        self.pushButton_limpiar_equipo.setMinimumSize(QSize(140, 45))
        self.pushButton_limpiar_equipo.setFont(font)
        self.pushButton_limpiar_equipo.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_botones.addWidget(self.pushButton_limpiar_equipo)

        self.pushButton_crear_jugador_equipo = QPushButton(Form)
        self.pushButton_crear_jugador_equipo.setObjectName(u"pushButton_crear_jugador_equipo")
        self.pushButton_crear_jugador_equipo.setMinimumSize(QSize(140, 45))
        self.pushButton_crear_jugador_equipo.setFont(font)
        self.pushButton_crear_jugador_equipo.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_botones.addWidget(self.pushButton_crear_jugador_equipo)

        self.pushButton_eliminar_equipo = QPushButton(Form)
        self.pushButton_eliminar_equipo.setObjectName(u"pushButton_eliminar_equipo")
        self.pushButton_eliminar_equipo.setMinimumSize(QSize(140, 45))
        self.pushButton_eliminar_equipo.setFont(font)
        self.pushButton_eliminar_equipo.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_botones.addWidget(self.pushButton_eliminar_equipo)

        self.pushButton_volver_equipos = QPushButton(Form)
        self.pushButton_volver_equipos.setObjectName(u"pushButton_volver_equipos")
        self.pushButton_volver_equipos.setMinimumSize(QSize(140, 45))
        self.pushButton_volver_equipos.setFont(font3)
        self.pushButton_volver_equipos.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_botones.addWidget(self.pushButton_volver_equipos)

        self.horizontalLayout_botones.setStretch(0, 1)
        self.horizontalLayout_botones.setStretch(1, 3)
        self.horizontalLayout_botones.setStretch(2, 3)
        self.horizontalLayout_botones.setStretch(3, 3)
        self.horizontalLayout_botones.setStretch(4, 3)
        self.horizontalLayout_botones.setStretch(5, 3)

        self.verticalLayout_main.addLayout(self.horizontalLayout_botones)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Gesti\u00f3n de Equipos - Torneo de F\u00fatbol", None))
        self.groupBox_datos_equipo.setTitle("")
#if QT_CONFIG(tooltip)
        self.lineEdit_nombre_equipo.setToolTip(QCoreApplication.translate("Form", u"Ingrese el nombre del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_nombre_equipo.setPlaceholderText("")
        self.comboBox_curso_equipo.setItemText(0, QCoreApplication.translate("Form", u"Seleccionar Curso", None))
        self.comboBox_curso_equipo.setItemText(1, QCoreApplication.translate("Form", u"1\u00ba ESO A", None))
        self.comboBox_curso_equipo.setItemText(2, QCoreApplication.translate("Form", u"1\u00ba ESO B", None))
        self.comboBox_curso_equipo.setItemText(3, QCoreApplication.translate("Form", u"2\u00ba ESO A", None))
        self.comboBox_curso_equipo.setItemText(4, QCoreApplication.translate("Form", u"2\u00ba ESO B", None))
        self.comboBox_curso_equipo.setItemText(5, QCoreApplication.translate("Form", u"3\u00ba ESO A", None))
        self.comboBox_curso_equipo.setItemText(6, QCoreApplication.translate("Form", u"3\u00ba ESO B", None))
        self.comboBox_curso_equipo.setItemText(7, QCoreApplication.translate("Form", u"4\u00ba ESO A", None))
        self.comboBox_curso_equipo.setItemText(8, QCoreApplication.translate("Form", u"4\u00ba ESO B", None))

#if QT_CONFIG(tooltip)
        self.comboBox_curso_equipo.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_color_equipo.setToolTip(QCoreApplication.translate("Form", u"Color de la equipaci\u00f3n del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_color_equipo.setPlaceholderText("")
        self.groupBox_escudo.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_imagen_escudo.setToolTip(QCoreApplication.translate("Form", u"Vista previa del escudo", None))
#endif // QT_CONFIG(tooltip)
        self.label_imagen_escudo.setText(QCoreApplication.translate("Form", u"Sin imagen", None))
#if QT_CONFIG(tooltip)
        self.pushButton_cargar_escudo.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_cargar_escudo.setText("")
        self.groupBox_equipacion.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_imagen_equipacion.setToolTip(QCoreApplication.translate("Form", u"Vista previa de la equipaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.label_imagen_equipacion.setText(QCoreApplication.translate("Form", u"Sin imagen", None))
#if QT_CONFIG(tooltip)
        self.pushButton_cargar_equipacion.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen de la equipaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_cargar_equipacion.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_registrar_equipo.setToolTip(QCoreApplication.translate("Form", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_registrar_equipo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_limpiar_equipo.setToolTip(QCoreApplication.translate("Form", u"Limpiar todos los campos del formulario", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_limpiar_equipo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_crear_jugador_equipo.setToolTip(QCoreApplication.translate("Form", u"Agregar un nuevo jugador al equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_crear_jugador_equipo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_eliminar_equipo.setToolTip(QCoreApplication.translate("Form", u"Eliminar el jugador seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_eliminar_equipo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_volver_equipos.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_equipos.setText("")
    # retranslateUi

