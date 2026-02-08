# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eventos_partido.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from widgets.reloj_digital import RelojDigital

class Ui_EventosPartido(object):
    def setupUi(self, EventosPartido):
        if not EventosPartido.objectName():
            EventosPartido.setObjectName(u"EventosPartido")
        EventosPartido.resize(939, 598)
        EventosPartido.setStyleSheet(u"QWidget#EventosPartido {\n"
"	background-color: rgb(94, 207, 207);\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(EventosPartido)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.comboBox_seleccion_partido_eventos = QComboBox(EventosPartido)
        self.comboBox_seleccion_partido_eventos.addItem("")
        self.comboBox_seleccion_partido_eventos.setObjectName(u"comboBox_seleccion_partido_eventos")
        self.comboBox_seleccion_partido_eventos.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(10)
        self.comboBox_seleccion_partido_eventos.setFont(font)
        self.comboBox_seleccion_partido_eventos.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.comboBox_seleccion_partido_eventos)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 10)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo_equipoA_eventos = QLabel(EventosPartido)
        self.titulo_equipoA_eventos.setObjectName(u"titulo_equipoA_eventos")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.titulo_equipoA_eventos.setFont(font1)
        self.titulo_equipoA_eventos.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.titulo_equipoA_eventos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titulo_equipoA_eventos)

        self.tableWidget_eventos_equipoA = QTableWidget(EventosPartido)
        if (self.tableWidget_eventos_equipoA.columnCount() < 3):
            self.tableWidget_eventos_equipoA.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_eventos_equipoA.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_eventos_equipoA.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_eventos_equipoA.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_eventos_equipoA.setObjectName(u"tableWidget_eventos_equipoA")
        self.tableWidget_eventos_equipoA.setFont(font)
        self.tableWidget_eventos_equipoA.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_eventos_equipoA.setAlternatingRowColors(True)
        self.tableWidget_eventos_equipoA.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_eventos_equipoA.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_eventos_equipoA.setSortingEnabled(True)
        self.tableWidget_eventos_equipoA.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget_eventos_equipoA)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_reloj = QVBoxLayout()
        self.verticalLayout_reloj.setObjectName(u"verticalLayout_reloj")
        self.widget_reloj = RelojDigital(EventosPartido)
        self.widget_reloj.setObjectName(u"widget_reloj")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_reloj.sizePolicy().hasHeightForWidth())
        self.widget_reloj.setSizePolicy(sizePolicy)
        self.widget_reloj.setMinimumSize(QSize(250, 200))

        self.verticalLayout_reloj.addWidget(self.widget_reloj)


        self.horizontalLayout.addLayout(self.verticalLayout_reloj)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titulo_equipoB_eventos = QLabel(EventosPartido)
        self.titulo_equipoB_eventos.setObjectName(u"titulo_equipoB_eventos")
        self.titulo_equipoB_eventos.setFont(font1)
        self.titulo_equipoB_eventos.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.titulo_equipoB_eventos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titulo_equipoB_eventos)

        self.tableWidget_eventos_equipoB = QTableWidget(EventosPartido)
        if (self.tableWidget_eventos_equipoB.columnCount() < 3):
            self.tableWidget_eventos_equipoB.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_eventos_equipoB.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_eventos_equipoB.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_eventos_equipoB.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_eventos_equipoB.setObjectName(u"tableWidget_eventos_equipoB")
        self.tableWidget_eventos_equipoB.setFont(font)
        self.tableWidget_eventos_equipoB.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_eventos_equipoB.setAlternatingRowColors(True)
        self.tableWidget_eventos_equipoB.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_eventos_equipoB.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_eventos_equipoB.setSortingEnabled(True)
        self.tableWidget_eventos_equipoB.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget_eventos_equipoB)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 10)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox_datos_equipo = QGroupBox(EventosPartido)
        self.groupBox_datos_equipo.setObjectName(u"groupBox_datos_equipo")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.groupBox_datos_equipo.setFont(font2)
        self.verticalLayout_formulario = QVBoxLayout(self.groupBox_datos_equipo)
        self.verticalLayout_formulario.setSpacing(7)
        self.verticalLayout_formulario.setObjectName(u"verticalLayout_formulario")
        self.verticalLayout_formulario.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_intro_equipo_evento = QComboBox(self.groupBox_datos_equipo)
        self.comboBox_intro_equipo_evento.addItem("")
        self.comboBox_intro_equipo_evento.setObjectName(u"comboBox_intro_equipo_evento")
        self.comboBox_intro_equipo_evento.setMinimumSize(QSize(150, 40))
        self.comboBox_intro_equipo_evento.setFont(font)
        self.comboBox_intro_equipo_evento.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.comboBox_intro_equipo_evento)

        self.comboBox_intro_jugador_evento = QComboBox(self.groupBox_datos_equipo)
        self.comboBox_intro_jugador_evento.addItem("")
        self.comboBox_intro_jugador_evento.setObjectName(u"comboBox_intro_jugador_evento")
        self.comboBox_intro_jugador_evento.setMinimumSize(QSize(150, 40))
        self.comboBox_intro_jugador_evento.setFont(font)
        self.comboBox_intro_jugador_evento.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.comboBox_intro_jugador_evento)

        self.comboBox_selector_evento = QComboBox(self.groupBox_datos_equipo)
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.addItem("")
        self.comboBox_selector_evento.setObjectName(u"comboBox_selector_evento")
        self.comboBox_selector_evento.setMinimumSize(QSize(150, 40))
        self.comboBox_selector_evento.setFont(font)
        self.comboBox_selector_evento.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.comboBox_selector_evento)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.label = QLabel(self.groupBox_datos_equipo)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.spinBox_min_evento = QSpinBox(self.groupBox_datos_equipo)
        self.spinBox_min_evento.setObjectName(u"spinBox_min_evento")
        self.spinBox_min_evento.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.spinBox_min_evento)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_formulario.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_datos_equipo)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pushButton_registrar_evento = QPushButton(EventosPartido)
        self.pushButton_registrar_evento.setObjectName(u"pushButton_registrar_evento")
        self.pushButton_registrar_evento.setMinimumSize(QSize(140, 45))
        self.pushButton_registrar_evento.setFont(font2)
        self.pushButton_registrar_evento.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.pushButton_registrar_evento)

        self.pushButton_finalizar_partido = QPushButton(EventosPartido)
        self.pushButton_finalizar_partido.setObjectName(u"pushButton_finalizar_partido")
        self.pushButton_finalizar_partido.setMinimumSize(QSize(140, 45))
        self.pushButton_finalizar_partido.setFont(font2)
        self.pushButton_finalizar_partido.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.pushButton_finalizar_partido)

        self.pushButton_volver_eventos = QPushButton(EventosPartido)
        self.pushButton_volver_eventos.setObjectName(u"pushButton_volver_eventos")
        self.pushButton_volver_eventos.setMinimumSize(QSize(140, 45))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton_volver_eventos.setFont(font4)
        self.pushButton_volver_eventos.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_volver_eventos)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(EventosPartido)

        QMetaObject.connectSlotsByName(EventosPartido)
    # setupUi

    def retranslateUi(self, EventosPartido):
        EventosPartido.setWindowTitle(QCoreApplication.translate("EventosPartido", u"Form", None))
        self.comboBox_seleccion_partido_eventos.setItemText(0, QCoreApplication.translate("EventosPartido", u"Selecciona Partido", None))

#if QT_CONFIG(tooltip)
        self.comboBox_seleccion_partido_eventos.setToolTip(QCoreApplication.translate("EventosPartido", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.titulo_equipoA_eventos.setText(QCoreApplication.translate("EventosPartido", u"Equipo  A", None))
        self.titulo_equipoB_eventos.setText(QCoreApplication.translate("EventosPartido", u"Equipo  B", None))
        self.groupBox_datos_equipo.setTitle("")
        self.comboBox_intro_equipo_evento.setItemText(0, QCoreApplication.translate("EventosPartido", u"Equipo", None))

#if QT_CONFIG(tooltip)
        self.comboBox_intro_equipo_evento.setToolTip(QCoreApplication.translate("EventosPartido", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_intro_jugador_evento.setItemText(0, QCoreApplication.translate("EventosPartido", u"Jugador", None))

#if QT_CONFIG(tooltip)
        self.comboBox_intro_jugador_evento.setToolTip(QCoreApplication.translate("EventosPartido", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_selector_evento.setItemText(0, QCoreApplication.translate("EventosPartido", u"Evento", None))
        self.comboBox_selector_evento.setItemText(1, QCoreApplication.translate("EventosPartido", u"Gol \u26bd", None))
        self.comboBox_selector_evento.setItemText(2, QCoreApplication.translate("EventosPartido", u"Asistencia", None))
        self.comboBox_selector_evento.setItemText(3, QCoreApplication.translate("EventosPartido", u"Falta \u274c", None))
        self.comboBox_selector_evento.setItemText(4, QCoreApplication.translate("EventosPartido", u"Amarilla", None))
        self.comboBox_selector_evento.setItemText(5, QCoreApplication.translate("EventosPartido", u"Roja", None))
        self.comboBox_selector_evento.setItemText(6, QCoreApplication.translate("EventosPartido", u"Parada", None))

#if QT_CONFIG(tooltip)
        self.comboBox_selector_evento.setToolTip(QCoreApplication.translate("EventosPartido", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("EventosPartido", u"Minuto", None))
#if QT_CONFIG(tooltip)
        self.pushButton_registrar_evento.setToolTip(QCoreApplication.translate("EventosPartido", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_registrar_evento.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_finalizar_partido.setToolTip(QCoreApplication.translate("EventosPartido", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_finalizar_partido.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_volver_eventos.setToolTip(QCoreApplication.translate("EventosPartido", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_eventos.setText("")
    # retranslateUi

