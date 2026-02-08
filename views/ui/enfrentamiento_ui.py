# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enfrentamiento.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from imagenes import recursos_rc

class Ui_Enfrentamiento(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1120, 777)
        Form.setStyleSheet(u"QWidget#Form {\n"
"      background-color: rgb(94, 207, 207);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.comboBox_equipoA_enfrentamiento = QComboBox(Form)
        self.comboBox_equipoA_enfrentamiento.addItem("")
        self.comboBox_equipoA_enfrentamiento.setObjectName(u"comboBox_equipoA_enfrentamiento")
        self.comboBox_equipoA_enfrentamiento.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.comboBox_equipoA_enfrentamiento.setFont(font)
        self.comboBox_equipoA_enfrentamiento.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.comboBox_equipoA_enfrentamiento)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.comboBox_equipoB_enfrentamiento = QComboBox(Form)
        self.comboBox_equipoB_enfrentamiento.addItem("")
        self.comboBox_equipoB_enfrentamiento.setObjectName(u"comboBox_equipoB_enfrentamiento")
        self.comboBox_equipoB_enfrentamiento.setMinimumSize(QSize(150, 40))
        self.comboBox_equipoB_enfrentamiento.setFont(font)
        self.comboBox_equipoB_enfrentamiento.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.comboBox_equipoB_enfrentamiento)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 2)
        self.horizontalLayout_4.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_campo = QHBoxLayout()
        self.horizontalLayout_campo.setSpacing(0)
        self.horizontalLayout_campo.setObjectName(u"horizontalLayout_campo")
        self.label_campo_izq = QLabel(Form)
        self.label_campo_izq.setObjectName(u"label_campo_izq")
        self.label_campo_izq.setStyleSheet(u"border-image: url(:/images/campo_izquierdo.jpg) 0 0 0 0 stretch stretch;")
        self.label_campo_izq.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_campo.addWidget(self.label_campo_izq)

        self.label_campo_der = QLabel(Form)
        self.label_campo_der.setObjectName(u"label_campo_der")
        self.label_campo_der.setStyleSheet(u"border-image: url(:/images/campo_derecho.jpg) 0 0 0 0 stretch stretch;")
        self.label_campo_der.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_campo.addWidget(self.label_campo_der)

        self.horizontalLayout_campo.setStretch(0, 1)
        self.horizontalLayout_campo.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_campo)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.comboBox_arbitro_enfrentamiento = QComboBox(Form)
        self.comboBox_arbitro_enfrentamiento.addItem("")
        self.comboBox_arbitro_enfrentamiento.setObjectName(u"comboBox_arbitro_enfrentamiento")
        self.comboBox_arbitro_enfrentamiento.setMinimumSize(QSize(150, 40))
        self.comboBox_arbitro_enfrentamiento.setFont(font)
        self.comboBox_arbitro_enfrentamiento.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.comboBox_arbitro_enfrentamiento)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.dateEdit_fecha_enfrentamiento = QDateEdit(Form)
        self.dateEdit_fecha_enfrentamiento.setObjectName(u"dateEdit_fecha_enfrentamiento")
        self.dateEdit_fecha_enfrentamiento.setMinimumSize(QSize(150, 40))
        self.dateEdit_fecha_enfrentamiento.setFont(font)
        self.dateEdit_fecha_enfrentamiento.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.dateEdit_fecha_enfrentamiento)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_enfrentar = QPushButton(Form)
        self.pushButton_enfrentar.setObjectName(u"pushButton_enfrentar")
        self.pushButton_enfrentar.setMinimumSize(QSize(140, 45))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton_enfrentar.setFont(font1)
        self.pushButton_enfrentar.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_enfrentar)

        self.pushButton_volver_enfrentamientos = QPushButton(Form)
        self.pushButton_volver_enfrentamientos.setObjectName(u"pushButton_volver_enfrentamientos")
        self.pushButton_volver_enfrentamientos.setMinimumSize(QSize(140, 45))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_volver_enfrentamientos.setFont(font2)
        self.pushButton_volver_enfrentamientos.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_volver_enfrentamientos)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Enfrentamiento", None))
        self.comboBox_equipoA_enfrentamiento.setItemText(0, QCoreApplication.translate("Form", u"Equipo A", None))

        self.comboBox_equipoB_enfrentamiento.setItemText(0, QCoreApplication.translate("Form", u"Equipo B", None))

        self.label_campo_izq.setText("")
        self.label_campo_der.setText("")
        self.comboBox_arbitro_enfrentamiento.setItemText(0, QCoreApplication.translate("Form", u"Arbitro", None))

        self.pushButton_enfrentar.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_volver_enfrentamientos.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_enfrentamientos.setText("")
    # retranslateUi

