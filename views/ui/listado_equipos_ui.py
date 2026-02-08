# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listado_equipos.ui'
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

class Ui_ListadoEquipos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 538)
        Form.setStyleSheet(u"QWidget#Form {\n"
"	background-color: rgb(94, 207, 207);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_datos_equipo = QGroupBox(Form)
        self.groupBox_datos_equipo.setObjectName(u"groupBox_datos_equipo")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox_datos_equipo.setFont(font)
        self.verticalLayout_formulario = QVBoxLayout(self.groupBox_datos_equipo)
        self.verticalLayout_formulario.setSpacing(10)
        self.verticalLayout_formulario.setObjectName(u"verticalLayout_formulario")
        self.verticalLayout_formulario.setContentsMargins(15, 10, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_curso_equipo_filtro = QComboBox(self.groupBox_datos_equipo)
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.addItem("")
        self.comboBox_curso_equipo_filtro.setObjectName(u"comboBox_curso_equipo_filtro")
        self.comboBox_curso_equipo_filtro.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox_curso_equipo_filtro.setFont(font1)
        self.comboBox_curso_equipo_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.comboBox_curso_equipo_filtro)

        self.lineEdit_nombre_equipo_filtro = QLineEdit(self.groupBox_datos_equipo)
        self.lineEdit_nombre_equipo_filtro.setObjectName(u"lineEdit_nombre_equipo_filtro")
        self.lineEdit_nombre_equipo_filtro.setMinimumSize(QSize(0, 40))
        self.lineEdit_nombre_equipo_filtro.setFont(font1)
        self.lineEdit_nombre_equipo_filtro.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.lineEdit_nombre_equipo_filtro)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_formulario.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_datos_equipo)

        self.tableWidget_lista_equipos = QTableWidget(Form)
        if (self.tableWidget_lista_equipos.columnCount() < 7):
            self.tableWidget_lista_equipos.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_lista_equipos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_lista_equipos.setObjectName(u"tableWidget_lista_equipos")
        self.tableWidget_lista_equipos.setFont(font1)
        self.tableWidget_lista_equipos.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_lista_equipos.setAlternatingRowColors(True)
        self.tableWidget_lista_equipos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_lista_equipos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_lista_equipos.setSortingEnabled(True)
        self.tableWidget_lista_equipos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget_lista_equipos)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_buscar_equipos = QPushButton(Form)
        self.pushButton_buscar_equipos.setObjectName(u"pushButton_buscar_equipos")
        self.pushButton_buscar_equipos.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_buscar_equipos.setFont(font2)
        self.pushButton_buscar_equipos.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_buscar_equipos)

        self.pushButton_editar_equipos = QPushButton(Form)
        self.pushButton_editar_equipos.setObjectName(u"pushButton_editar_equipos")
        self.pushButton_editar_equipos.setMinimumSize(QSize(0, 40))
        self.pushButton_editar_equipos.setFont(font2)
        self.pushButton_editar_equipos.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_editar_equipos)

        self.pushButton_lista_equipos_volver = QPushButton(Form)
        self.pushButton_lista_equipos_volver.setObjectName(u"pushButton_lista_equipos_volver")
        self.pushButton_lista_equipos_volver.setMinimumSize(QSize(0, 40))
        self.pushButton_lista_equipos_volver.setFont(font2)
        self.pushButton_lista_equipos_volver.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_lista_equipos_volver)

        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_datos_equipo.setTitle("")
        self.comboBox_curso_equipo_filtro.setItemText(0, QCoreApplication.translate("Form", u"    Seleccionar Curso", None))
        self.comboBox_curso_equipo_filtro.setItemText(1, QCoreApplication.translate("Form", u"1\u00ba ESO A", None))
        self.comboBox_curso_equipo_filtro.setItemText(2, QCoreApplication.translate("Form", u"1\u00ba ESO B", None))
        self.comboBox_curso_equipo_filtro.setItemText(3, QCoreApplication.translate("Form", u"2\u00ba ESO A", None))
        self.comboBox_curso_equipo_filtro.setItemText(4, QCoreApplication.translate("Form", u"2\u00ba ESO B", None))
        self.comboBox_curso_equipo_filtro.setItemText(5, QCoreApplication.translate("Form", u"3\u00ba ESO A", None))
        self.comboBox_curso_equipo_filtro.setItemText(6, QCoreApplication.translate("Form", u"3\u00ba ESO B", None))
        self.comboBox_curso_equipo_filtro.setItemText(7, QCoreApplication.translate("Form", u"4\u00ba ESO A", None))
        self.comboBox_curso_equipo_filtro.setItemText(8, QCoreApplication.translate("Form", u"4\u00ba ESO B", None))

#if QT_CONFIG(tooltip)
        self.comboBox_curso_equipo_filtro.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_nombre_equipo_filtro.setToolTip(QCoreApplication.translate("Form", u"Ingrese el nombre del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_nombre_equipo_filtro.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.pushButton_buscar_equipos.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_buscar_equipos.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_editar_equipos.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_editar_equipos.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_lista_equipos_volver.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_lista_equipos_volver.setText("")
    # retranslateUi

