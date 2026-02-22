# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informes.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(533, 496)
        Dialog.setStyleSheet(u"background-color: rgb(94, 207, 207);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo_informes = QLabel(Dialog)
        self.titulo_informes.setObjectName(u"titulo_informes")
        self.titulo_informes.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.titulo_informes.setFont(font)
        self.titulo_informes.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.titulo_informes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titulo_informes)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_tipo_informe = QComboBox(self.groupBox)
        self.comboBox_tipo_informe.addItem("")
        self.comboBox_tipo_informe.addItem("")
        self.comboBox_tipo_informe.addItem("")
        self.comboBox_tipo_informe.setObjectName(u"comboBox_tipo_informe")
        self.comboBox_tipo_informe.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_4.addWidget(self.comboBox_tipo_informe)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.comboBox_filtro_equipo = QComboBox(self.groupBox_2)
        self.comboBox_filtro_equipo.setObjectName(u"comboBox_filtro_equipo")
        self.comboBox_filtro_equipo.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_filtro_equipo)

        self.comboBox_filtro_ronda = QComboBox(self.groupBox_2)
        self.comboBox_filtro_ronda.setObjectName(u"comboBox_filtro_ronda")
        self.comboBox_filtro_ronda.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_filtro_ronda)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)


        self.horizontalLayout_3.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_ruta_destino = QLineEdit(self.groupBox_3)
        self.lineEdit_ruta_destino.setObjectName(u"lineEdit_ruta_destino")
        self.lineEdit_ruta_destino.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")
        self.lineEdit_ruta_destino.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_ruta_destino)

        self.toolButton_selec_ruta = QToolButton(self.groupBox_3)
        self.toolButton_selec_ruta.setObjectName(u"toolButton_selec_ruta")
        self.toolButton_selec_ruta.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout.addWidget(self.toolButton_selec_ruta)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_generar_pdf = QPushButton(Dialog)
        self.pushButton_generar_pdf.setObjectName(u"pushButton_generar_pdf")
        self.pushButton_generar_pdf.setMinimumSize(QSize(140, 45))
        self.pushButton_generar_pdf.setFont(font1)
        self.pushButton_generar_pdf.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_generar_pdf)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titulo_informes.setText(QCoreApplication.translate("Dialog", u"Informes", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Seleccion informes", None))
        self.comboBox_tipo_informe.setItemText(0, QCoreApplication.translate("Dialog", u"Equipos y Jugadores", None))
        self.comboBox_tipo_informe.setItemText(1, QCoreApplication.translate("Dialog", u"Partidos y resultados", None))
        self.comboBox_tipo_informe.setItemText(2, QCoreApplication.translate("Dialog", u"Clasificacion y Eliminatorias", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Filtros ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Filtar por Ronda/Eliminatoria", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filtrar por Equipo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Carpeta Destino", None))
        self.toolButton_selec_ruta.setText(QCoreApplication.translate("Dialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_generar_pdf.setToolTip(QCoreApplication.translate("Dialog", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_generar_pdf.setText(QCoreApplication.translate("Dialog", u"Generar Informe PDF", None))
    # retranslateUi

