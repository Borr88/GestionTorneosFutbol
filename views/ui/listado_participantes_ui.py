# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listado_participantes.ui'
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
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Listado_Participantes(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(867, 539)
        Form.setStyleSheet(u"QWidget#Form {\n"
"	background-color: rgb(94, 207, 207);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_filtro_participante = QGroupBox(Form)
        self.groupBox_filtro_participante.setObjectName(u"groupBox_filtro_participante")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox_filtro_participante.setFont(font)
        self.verticalLayout_formulario = QVBoxLayout(self.groupBox_filtro_participante)
        self.verticalLayout_formulario.setSpacing(10)
        self.verticalLayout_formulario.setObjectName(u"verticalLayout_formulario")
        self.verticalLayout_formulario.setContentsMargins(15, 10, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_nombre_participante_filtro = QLineEdit(self.groupBox_filtro_participante)
        self.lineEdit_nombre_participante_filtro.setObjectName(u"lineEdit_nombre_participante_filtro")
        self.lineEdit_nombre_participante_filtro.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_nombre_participante_filtro.setFont(font1)
        self.lineEdit_nombre_participante_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout.addWidget(self.lineEdit_nombre_participante_filtro)

        self.comboBox_curso_participante_filtro = QComboBox(self.groupBox_filtro_participante)
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.addItem("")
        self.comboBox_curso_participante_filtro.setObjectName(u"comboBox_curso_participante_filtro")
        self.comboBox_curso_participante_filtro.setMinimumSize(QSize(150, 40))
        self.comboBox_curso_participante_filtro.setFont(font1)
        self.comboBox_curso_participante_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout.addWidget(self.comboBox_curso_participante_filtro)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_posicion_filtro = QComboBox(self.groupBox_filtro_participante)
        self.comboBox_posicion_filtro.addItem("")
        self.comboBox_posicion_filtro.addItem("")
        self.comboBox_posicion_filtro.addItem("")
        self.comboBox_posicion_filtro.addItem("")
        self.comboBox_posicion_filtro.addItem("")
        self.comboBox_posicion_filtro.setObjectName(u"comboBox_posicion_filtro")
        self.comboBox_posicion_filtro.setMinimumSize(QSize(150, 40))
        self.comboBox_posicion_filtro.setFont(font1)
        self.comboBox_posicion_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.comboBox_posicion_filtro)

        self.comboBox_equipo_participante_filtro = QComboBox(self.groupBox_filtro_participante)
        self.comboBox_equipo_participante_filtro.addItem("")
        self.comboBox_equipo_participante_filtro.setObjectName(u"comboBox_equipo_participante_filtro")
        self.comboBox_equipo_participante_filtro.setMinimumSize(QSize(150, 40))
        self.comboBox_equipo_participante_filtro.setFont(font1)
        self.comboBox_equipo_participante_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.comboBox_equipo_participante_filtro)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_formulario.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_filtro_participante)

        self.tableWidget_lista_participantes = QTableWidget(Form)
        if (self.tableWidget_lista_participantes.columnCount() < 10):
            self.tableWidget_lista_participantes.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_lista_participantes.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget_lista_participantes.setObjectName(u"tableWidget_lista_participantes")
        self.tableWidget_lista_participantes.setFont(font1)
        self.tableWidget_lista_participantes.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_lista_participantes.setAlternatingRowColors(True)
        self.tableWidget_lista_participantes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_lista_participantes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_lista_participantes.setSortingEnabled(True)
        self.tableWidget_lista_participantes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableWidget_lista_participantes)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_buscar_participante = QPushButton(Form)
        self.pushButton_buscar_participante.setObjectName(u"pushButton_buscar_participante")
        self.pushButton_buscar_participante.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_buscar_participante.setFont(font2)
        self.pushButton_buscar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_buscar_participante)

        self.pushButton_editar_participante = QPushButton(Form)
        self.pushButton_editar_participante.setObjectName(u"pushButton_editar_participante")
        self.pushButton_editar_participante.setMinimumSize(QSize(0, 40))
        self.pushButton_editar_participante.setFont(font2)
        self.pushButton_editar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_editar_participante)

        self.pushButton_volver_lista_participantes = QPushButton(Form)
        self.pushButton_volver_lista_participantes.setObjectName(u"pushButton_volver_lista_participantes")
        self.pushButton_volver_lista_participantes.setMinimumSize(QSize(0, 40))
        self.pushButton_volver_lista_participantes.setFont(font2)
        self.pushButton_volver_lista_participantes.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_volver_lista_participantes)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_filtro_participante.setTitle("")
#if QT_CONFIG(tooltip)
        self.lineEdit_nombre_participante_filtro.setToolTip(QCoreApplication.translate("Form", u"Ingrese el nombre del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_nombre_participante_filtro.setPlaceholderText("")
        self.comboBox_curso_participante_filtro.setItemText(0, QCoreApplication.translate("Form", u"    Seleccionar Curso", None))
        self.comboBox_curso_participante_filtro.setItemText(1, QCoreApplication.translate("Form", u"1\u00ba ESO A", None))
        self.comboBox_curso_participante_filtro.setItemText(2, QCoreApplication.translate("Form", u"1\u00ba ESO B", None))
        self.comboBox_curso_participante_filtro.setItemText(3, QCoreApplication.translate("Form", u"2\u00ba ESO A", None))
        self.comboBox_curso_participante_filtro.setItemText(4, QCoreApplication.translate("Form", u"2\u00ba ESO B", None))
        self.comboBox_curso_participante_filtro.setItemText(5, QCoreApplication.translate("Form", u"3\u00ba ESO A", None))
        self.comboBox_curso_participante_filtro.setItemText(6, QCoreApplication.translate("Form", u"3\u00ba ESO B", None))
        self.comboBox_curso_participante_filtro.setItemText(7, QCoreApplication.translate("Form", u"4\u00ba ESO A", None))
        self.comboBox_curso_participante_filtro.setItemText(8, QCoreApplication.translate("Form", u"4\u00ba ESO B", None))

#if QT_CONFIG(tooltip)
        self.comboBox_curso_participante_filtro.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_posicion_filtro.setItemText(0, QCoreApplication.translate("Form", u"   Posicion/Arbitro", None))
        self.comboBox_posicion_filtro.setItemText(1, QCoreApplication.translate("Form", u"Arbitro", None))
        self.comboBox_posicion_filtro.setItemText(2, QCoreApplication.translate("Form", u"Defensa", None))
        self.comboBox_posicion_filtro.setItemText(3, QCoreApplication.translate("Form", u"Delantero", None))
        self.comboBox_posicion_filtro.setItemText(4, QCoreApplication.translate("Form", u"Portero", None))

#if QT_CONFIG(tooltip)
        self.comboBox_posicion_filtro.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_equipo_participante_filtro.setItemText(0, QCoreApplication.translate("Form", u"     Equipo", None))

#if QT_CONFIG(tooltip)
        self.comboBox_equipo_participante_filtro.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_buscar_participante.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_buscar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_editar_participante.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_editar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_volver_lista_participantes.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_lista_participantes.setText("")
    # retranslateUi

