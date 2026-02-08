# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendario.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Calendario(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(919, 583)
        Form.setMinimumSize(QSize(0, 40))
        Form.setStyleSheet(u"background-color: rgb(94, 207, 207);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_calendario = QTableWidget(Form)
        if (self.tableWidget_calendario.columnCount() < 3):
            self.tableWidget_calendario.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_calendario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_calendario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_calendario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_calendario.setObjectName(u"tableWidget_calendario")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tableWidget_calendario.setFont(font)
        self.tableWidget_calendario.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_calendario.setAlternatingRowColors(True)
        self.tableWidget_calendario.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_calendario.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_calendario.setSortingEnabled(True)
        self.tableWidget_calendario.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget_calendario)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.dateEdit_fecha = QDateEdit(Form)
        self.dateEdit_fecha.setObjectName(u"dateEdit_fecha")
        self.dateEdit_fecha.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.dateEdit_fecha.setFont(font1)
        self.dateEdit_fecha.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.dateEdit_fecha)

        self.pushButton_asignar_fecha = QPushButton(Form)
        self.pushButton_asignar_fecha.setObjectName(u"pushButton_asignar_fecha")
        self.pushButton_asignar_fecha.setMinimumSize(QSize(140, 45))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_asignar_fecha.setFont(font2)
        self.pushButton_asignar_fecha.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.pushButton_asignar_fecha)

        self.comboBox_seleccion_fases = QComboBox(Form)
        self.comboBox_seleccion_fases.addItem("")
        self.comboBox_seleccion_fases.addItem("")
        self.comboBox_seleccion_fases.addItem("")
        self.comboBox_seleccion_fases.addItem("")
        self.comboBox_seleccion_fases.addItem("")
        self.comboBox_seleccion_fases.setObjectName(u"comboBox_seleccion_fases")
        self.comboBox_seleccion_fases.setMinimumSize(QSize(140, 45))
        self.comboBox_seleccion_fases.setFont(font2)
        self.comboBox_seleccion_fases.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.comboBox_seleccion_fases)

        self.pushButton_volver_calendario = QPushButton(Form)
        self.pushButton_volver_calendario.setObjectName(u"pushButton_volver_calendario")
        self.pushButton_volver_calendario.setMinimumSize(QSize(140, 45))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_volver_calendario.setFont(font3)
        self.pushButton_volver_calendario.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_volver_calendario)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_asignar_fecha.setText("")
        self.comboBox_seleccion_fases.setItemText(0, QCoreApplication.translate("Form", u"Seleccion Fase", None))
        self.comboBox_seleccion_fases.setItemText(1, QCoreApplication.translate("Form", u"Octavos", None))
        self.comboBox_seleccion_fases.setItemText(2, QCoreApplication.translate("Form", u"Cuartos", None))
        self.comboBox_seleccion_fases.setItemText(3, QCoreApplication.translate("Form", u"Semifinales", None))
        self.comboBox_seleccion_fases.setItemText(4, QCoreApplication.translate("Form", u"Final", None))

#if QT_CONFIG(tooltip)
        self.pushButton_volver_calendario.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_calendario.setText("")
    # retranslateUi

