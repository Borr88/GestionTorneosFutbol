# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_participantes.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Registro_Participante(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1140, 670)
        Form.setStyleSheet(u"QWidget#Form {\n"
"	background-color: rgb(94, 207, 207);\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_datos_participante = QGroupBox(Form)
        self.groupBox_datos_participante.setObjectName(u"groupBox_datos_participante")
        self.groupBox_datos_participante.setMinimumSize(QSize(0, 120))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox_datos_participante.setFont(font)
        self.verticalLayout_formulario = QVBoxLayout(self.groupBox_datos_participante)
        self.verticalLayout_formulario.setSpacing(10)
        self.verticalLayout_formulario.setObjectName(u"verticalLayout_formulario")
        self.verticalLayout_formulario.setContentsMargins(15, 20, 15, 15)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_nombre_participante = QLineEdit(self.groupBox_datos_participante)
        self.lineEdit_nombre_participante.setObjectName(u"lineEdit_nombre_participante")
        self.lineEdit_nombre_participante.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_nombre_participante.setFont(font1)
        self.lineEdit_nombre_participante.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout.addWidget(self.lineEdit_nombre_participante)

        self.lineEdit_apellido_participante = QLineEdit(self.groupBox_datos_participante)
        self.lineEdit_apellido_participante.setObjectName(u"lineEdit_apellido_participante")
        self.lineEdit_apellido_participante.setMinimumSize(QSize(0, 40))
        self.lineEdit_apellido_participante.setFont(font1)
        self.lineEdit_apellido_participante.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout.addWidget(self.lineEdit_apellido_participante)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateEdit_fecha_nacimiento = QDateEdit(self.groupBox_datos_participante)
        self.dateEdit_fecha_nacimiento.setObjectName(u"dateEdit_fecha_nacimiento")
        self.dateEdit_fecha_nacimiento.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.dateEdit_fecha_nacimiento)

        self.comboBox_curso_participante = QComboBox(self.groupBox_datos_participante)
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.addItem("")
        self.comboBox_curso_participante.setObjectName(u"comboBox_curso_participante")
        self.comboBox_curso_participante.setMinimumSize(QSize(150, 40))
        self.comboBox_curso_participante.setFont(font1)
        self.comboBox_curso_participante.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.comboBox_curso_participante)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_formulario.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addWidget(self.groupBox_datos_participante)

        self.groupBox_tipo_participante = QGroupBox(Form)
        self.groupBox_tipo_participante.setObjectName(u"groupBox_tipo_participante")
        self.groupBox_tipo_participante.setMinimumSize(QSize(0, 120))
        self.groupBox_tipo_participante.setFont(font)
        self.verticalLayout_formulario_2 = QVBoxLayout(self.groupBox_tipo_participante)
        self.verticalLayout_formulario_2.setSpacing(10)
        self.verticalLayout_formulario_2.setObjectName(u"verticalLayout_formulario_2")
        self.verticalLayout_formulario_2.setContentsMargins(15, 20, 15, 15)
        self.radioButton_jugador = QRadioButton(self.groupBox_tipo_participante)
        self.radioButton_jugador.setObjectName(u"radioButton_jugador")
        self.radioButton_jugador.setStyleSheet(u"QRadioButton {\n"
"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 7px; \n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"}")

        self.verticalLayout_formulario_2.addWidget(self.radioButton_jugador)

        self.radioButton_arbitro = QRadioButton(self.groupBox_tipo_participante)
        self.radioButton_arbitro.setObjectName(u"radioButton_arbitro")
        self.radioButton_arbitro.setStyleSheet(u"QRadioButton {\n"
"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 7px; \n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"}")

        self.verticalLayout_formulario_2.addWidget(self.radioButton_arbitro)


        self.horizontalLayout_4.addWidget(self.groupBox_tipo_participante)

        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tableWidget_participante = QTableWidget(Form)
        if (self.tableWidget_participante.columnCount() < 7):
            self.tableWidget_participante.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_participante.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_participante.setObjectName(u"tableWidget_participante")
        self.tableWidget_participante.setFont(font1)
        self.tableWidget_participante.setStyleSheet(u"background-color: rgb(27, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_participante.setAlternatingRowColors(True)
        self.tableWidget_participante.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_participante.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_participante.setSortingEnabled(True)
        self.tableWidget_participante.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableWidget_participante)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_escudo = QGroupBox(Form)
        self.groupBox_escudo.setObjectName(u"groupBox_escudo")
        self.groupBox_escudo.setMinimumSize(QSize(0, 200))
        self.groupBox_escudo.setFont(font)
        self.verticalLayout_escudo = QVBoxLayout(self.groupBox_escudo)
        self.verticalLayout_escudo.setSpacing(10)
        self.verticalLayout_escudo.setObjectName(u"verticalLayout_escudo")
        self.label_imagen_participante = QLabel(self.groupBox_escudo)
        self.label_imagen_participante.setObjectName(u"label_imagen_participante")
        self.label_imagen_participante.setMinimumSize(QSize(150, 150))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_imagen_participante.setFont(font2)
        self.label_imagen_participante.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;\n"
"}")
        self.label_imagen_participante.setScaledContents(True)
        self.label_imagen_participante.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_escudo.addWidget(self.label_imagen_participante)

        self.pushButton_cargar_participante = QPushButton(self.groupBox_escudo)
        self.pushButton_cargar_participante.setObjectName(u"pushButton_cargar_participante")
        self.pushButton_cargar_participante.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_cargar_participante.setFont(font3)
        self.pushButton_cargar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.verticalLayout_escudo.addWidget(self.pushButton_cargar_participante)


        self.verticalLayout_2.addWidget(self.groupBox_escudo)

        self.textEdit_resumen_participante = QTextEdit(Form)
        self.textEdit_resumen_participante.setObjectName(u"textEdit_resumen_participante")
        self.textEdit_resumen_participante.setStyleSheet(u"   background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.textEdit_resumen_participante)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 4)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5.setStretch(0, 15)
        self.horizontalLayout_5.setStretch(1, 5)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_asignar_participante = QPushButton(Form)
        self.pushButton_asignar_participante.setObjectName(u"pushButton_asignar_participante")
        self.pushButton_asignar_participante.setMinimumSize(QSize(140, 45))
        self.pushButton_asignar_participante.setFont(font)
        self.pushButton_asignar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_asignar_participante)

        self.pushButton_eliminar_participante = QPushButton(Form)
        self.pushButton_eliminar_participante.setObjectName(u"pushButton_eliminar_participante")
        self.pushButton_eliminar_participante.setMinimumSize(QSize(140, 45))
        self.pushButton_eliminar_participante.setFont(font)
        self.pushButton_eliminar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_eliminar_participante)

        self.pushButton_guardar_participante = QPushButton(Form)
        self.pushButton_guardar_participante.setObjectName(u"pushButton_guardar_participante")
        self.pushButton_guardar_participante.setMinimumSize(QSize(140, 45))
        self.pushButton_guardar_participante.setFont(font)
        self.pushButton_guardar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_guardar_participante)

        self.pushButton_limpiar_participante = QPushButton(Form)
        self.pushButton_limpiar_participante.setObjectName(u"pushButton_limpiar_participante")
        self.pushButton_limpiar_participante.setMinimumSize(QSize(140, 45))
        self.pushButton_limpiar_participante.setFont(font)
        self.pushButton_limpiar_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_limpiar_participante)

        self.pushButton_volver_participante = QPushButton(Form)
        self.pushButton_volver_participante.setObjectName(u"pushButton_volver_participante")
        self.pushButton_volver_participante.setMinimumSize(QSize(140, 45))
        self.pushButton_volver_participante.setFont(font3)
        self.pushButton_volver_participante.setStyleSheet(u"background-color: rgb(255, 149, 1);\n"
"color: rgb(38, 126, 126);\n"
"border:3px solid;\n"
"border-right-color: rgb(163, 95, 0);\n"
"border-bottom-color: rgb(163, 95, 0);\n"
"border-top-color: rgb(255, 187, 92);\n"
"border-left-color: rgb(255, 187, 92);\n"
"border-radius:10px;\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_volver_participante)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_datos_participante.setTitle("")
#if QT_CONFIG(tooltip)
        self.lineEdit_nombre_participante.setToolTip(QCoreApplication.translate("Form", u"Ingrese el nombre del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_nombre_participante.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_apellido_participante.setToolTip(QCoreApplication.translate("Form", u"Ingrese el nombre del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_apellido_participante.setPlaceholderText("")
        self.comboBox_curso_participante.setItemText(0, QCoreApplication.translate("Form", u"Seleccionar Curso", None))
        self.comboBox_curso_participante.setItemText(1, QCoreApplication.translate("Form", u"1\u00ba ESO A", None))
        self.comboBox_curso_participante.setItemText(2, QCoreApplication.translate("Form", u"1\u00ba ESO B", None))
        self.comboBox_curso_participante.setItemText(3, QCoreApplication.translate("Form", u"2\u00ba ESO A", None))
        self.comboBox_curso_participante.setItemText(4, QCoreApplication.translate("Form", u"2\u00ba ESO B", None))
        self.comboBox_curso_participante.setItemText(5, QCoreApplication.translate("Form", u"3\u00ba ESO A", None))
        self.comboBox_curso_participante.setItemText(6, QCoreApplication.translate("Form", u"3\u00ba ESO B", None))
        self.comboBox_curso_participante.setItemText(7, QCoreApplication.translate("Form", u"4\u00ba ESO A", None))
        self.comboBox_curso_participante.setItemText(8, QCoreApplication.translate("Form", u"4\u00ba ESO B", None))

#if QT_CONFIG(tooltip)
        self.comboBox_curso_participante.setToolTip(QCoreApplication.translate("Form", u"Seleccione el curso del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_tipo_participante.setTitle(QCoreApplication.translate("Form", u"Tipo Participante", None))
        self.radioButton_jugador.setText(QCoreApplication.translate("Form", u"Jugador", None))
        self.radioButton_arbitro.setText(QCoreApplication.translate("Form", u"Arbitro", None))
        self.groupBox_escudo.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_imagen_participante.setToolTip(QCoreApplication.translate("Form", u"Vista previa del escudo", None))
#endif // QT_CONFIG(tooltip)
        self.label_imagen_participante.setText(QCoreApplication.translate("Form", u"Sin imagen", None))
#if QT_CONFIG(tooltip)
        self.pushButton_cargar_participante.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_cargar_participante.setText("")
        self.textEdit_resumen_participante.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Historial:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Goles:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Asistencias</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\">- Faltas:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Amarillas:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Rojas:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_asignar_participante.setToolTip(QCoreApplication.translate("Form", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_asignar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_eliminar_participante.setToolTip(QCoreApplication.translate("Form", u"Eliminar el jugador seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_eliminar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_guardar_participante.setToolTip(QCoreApplication.translate("Form", u"Guardar equipo en la base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_guardar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_limpiar_participante.setToolTip(QCoreApplication.translate("Form", u"Limpiar todos los campos del formulario", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_limpiar_participante.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_volver_participante.setToolTip(QCoreApplication.translate("Form", u"Cargar imagen del escudo del equipo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_volver_participante.setText("")
    # retranslateUi

