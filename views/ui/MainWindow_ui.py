# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(970, 658)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 207, 207);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"QToolButton {\n"
"    color: black;\n"
"}")
        self.actionRegistrar_Equipo = QAction(MainWindow)
        self.actionRegistrar_Equipo.setObjectName(u"actionRegistrar_Equipo")
        self.actionRegistrar_participante = QAction(MainWindow)
        self.actionRegistrar_participante.setObjectName(u"actionRegistrar_participante")
        self.actionEquipos = QAction(MainWindow)
        self.actionEquipos.setObjectName(u"actionEquipos")
        self.actionParticipantes = QAction(MainWindow)
        self.actionParticipantes.setObjectName(u"actionParticipantes")
        self.actionCrear_partido = QAction(MainWindow)
        self.actionCrear_partido.setObjectName(u"actionCrear_partido")
        self.actionInicio_Partido = QAction(MainWindow)
        self.actionInicio_Partido.setObjectName(u"actionInicio_Partido")
        icon = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.actionInicio_Partido.setIcon(icon)
        self.actionGuia = QAction(MainWindow)
        self.actionGuia.setObjectName(u"actionGuia")
        font = QFont()
        self.actionGuia.setFont(font)
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.actionCalendario = QAction(MainWindow)
        self.actionCalendario.setObjectName(u"actionCalendario")
        icon1 = QIcon(QIcon.fromTheme(u"document-open-recent"))
        self.actionCalendario.setIcon(icon1)
        self.actionInicio = QAction(MainWindow)
        self.actionInicio.setObjectName(u"actionInicio")
        icon2 = QIcon(QIcon.fromTheme(u"go-home"))
        self.actionInicio.setIcon(icon2)
        self.actionInicio.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_equipo1 = QLabel(self.page)
        self.label_equipo1.setObjectName(u"label_equipo1")
        self.label_equipo1.setMinimumSize(QSize(0, 40))
        self.label_equipo1.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_equipo1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer)

        self.label_equipo2 = QLabel(self.page)
        self.label_equipo2.setObjectName(u"label_equipo2")
        self.label_equipo2.setMinimumSize(QSize(0, 40))
        self.label_equipo2.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_equipo2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_37)

        self.line_45 = QFrame(self.page)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.Shape.VLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_45)

        self.line_46 = QFrame(self.page)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_46)

        self.horizontalLayout_23.setStretch(0, 5)
        self.horizontalLayout_23.setStretch(1, 1)
        self.horizontalLayout_23.setStretch(2, 2)

        self.verticalLayout_36.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_8)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_equipo3 = QLabel(self.page)
        self.label_equipo3.setObjectName(u"label_equipo3")
        self.label_equipo3.setMinimumSize(QSize(0, 40))
        self.label_equipo3.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_equipo3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_2)

        self.label_equipo4 = QLabel(self.page)
        self.label_equipo4.setObjectName(u"label_equipo4")
        self.label_equipo4.setMinimumSize(QSize(0, 40))
        self.label_equipo4.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_equipo4)


        self.horizontalLayout_24.addLayout(self.verticalLayout_38)

        self.line_47 = QFrame(self.page)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.Shape.VLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_24.addWidget(self.line_47)

        self.line_48 = QFrame(self.page)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.Shape.HLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_24.addWidget(self.line_48)

        self.horizontalLayout_24.setStretch(0, 5)
        self.horizontalLayout_24.setStretch(1, 1)
        self.horizontalLayout_24.setStretch(2, 2)

        self.verticalLayout_36.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_9)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_equipo5 = QLabel(self.page)
        self.label_equipo5.setObjectName(u"label_equipo5")
        self.label_equipo5.setMinimumSize(QSize(0, 40))
        self.label_equipo5.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_equipo5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_3)

        self.label_equipo6 = QLabel(self.page)
        self.label_equipo6.setObjectName(u"label_equipo6")
        self.label_equipo6.setMinimumSize(QSize(0, 40))
        self.label_equipo6.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_equipo6)


        self.horizontalLayout_25.addLayout(self.verticalLayout_39)

        self.line_49 = QFrame(self.page)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_25.addWidget(self.line_49)

        self.line_50 = QFrame(self.page)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_25.addWidget(self.line_50)

        self.horizontalLayout_25.setStretch(0, 5)
        self.horizontalLayout_25.setStretch(1, 1)
        self.horizontalLayout_25.setStretch(2, 2)

        self.verticalLayout_36.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_10)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_equipo7 = QLabel(self.page)
        self.label_equipo7.setObjectName(u"label_equipo7")
        self.label_equipo7.setMinimumSize(QSize(0, 40))
        self.label_equipo7.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_equipo7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_4)

        self.label_equipo8 = QLabel(self.page)
        self.label_equipo8.setObjectName(u"label_equipo8")
        self.label_equipo8.setMinimumSize(QSize(0, 40))
        self.label_equipo8.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_equipo8)


        self.horizontalLayout_26.addLayout(self.verticalLayout_40)

        self.line_51 = QFrame(self.page)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_26.addWidget(self.line_51)

        self.line_52 = QFrame(self.page)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.Shape.HLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_26.addWidget(self.line_52)

        self.horizontalLayout_26.setStretch(0, 5)
        self.horizontalLayout_26.setStretch(1, 1)
        self.horizontalLayout_26.setStretch(2, 2)

        self.verticalLayout_36.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_29.addLayout(self.verticalLayout_36)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_cuartos1 = QLabel(self.page)
        self.label_cuartos1.setObjectName(u"label_cuartos1")
        self.label_cuartos1.setMinimumSize(QSize(0, 40))
        self.label_cuartos1.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_cuartos1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_5)

        self.label_cuartos2 = QLabel(self.page)
        self.label_cuartos2.setObjectName(u"label_cuartos2")
        self.label_cuartos2.setMinimumSize(QSize(0, 40))
        self.label_cuartos2.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_cuartos2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_34)

        self.line_41 = QFrame(self.page)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_41)

        self.line_42 = QFrame(self.page)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.Shape.HLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_42)

        self.horizontalLayout_21.setStretch(0, 5)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 2)

        self.verticalLayout_33.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_cuartos3 = QLabel(self.page)
        self.label_cuartos3.setObjectName(u"label_cuartos3")
        self.label_cuartos3.setMinimumSize(QSize(0, 40))
        self.label_cuartos3.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_cuartos3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_6)

        self.label_cuartos4 = QLabel(self.page)
        self.label_cuartos4.setObjectName(u"label_cuartos4")
        self.label_cuartos4.setMinimumSize(QSize(0, 40))
        self.label_cuartos4.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_cuartos4)


        self.horizontalLayout_22.addLayout(self.verticalLayout_35)

        self.line_43 = QFrame(self.page)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_22.addWidget(self.line_43)

        self.line_44 = QFrame(self.page)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.Shape.HLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_22.addWidget(self.line_44)

        self.horizontalLayout_22.setStretch(0, 5)
        self.horizontalLayout_22.setStretch(1, 1)
        self.horizontalLayout_22.setStretch(2, 2)

        self.verticalLayout_33.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_21)

        self.verticalLayout_33.setStretch(0, 2)
        self.verticalLayout_33.setStretch(1, 8)
        self.verticalLayout_33.setStretch(2, 6)
        self.verticalLayout_33.setStretch(3, 8)
        self.verticalLayout_33.setStretch(4, 2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_33)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_15)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_semi1 = QLabel(self.page)
        self.label_semi1.setObjectName(u"label_semi1")
        self.label_semi1.setMinimumSize(QSize(0, 40))
        self.label_semi1.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_semi1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_semi1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_7)

        self.label_semi2 = QLabel(self.page)
        self.label_semi2.setObjectName(u"label_semi2")
        self.label_semi2.setMinimumSize(QSize(0, 40))
        self.label_semi2.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_semi2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_semi2)


        self.horizontalLayout_20.addLayout(self.verticalLayout_31)

        self.line_39 = QFrame(self.page)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_39)

        self.line_40 = QFrame(self.page)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.HLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_40)

        self.horizontalLayout_20.setStretch(0, 5)
        self.horizontalLayout_20.setStretch(1, 1)
        self.horizontalLayout_20.setStretch(2, 2)

        self.verticalLayout_30.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_16)

        self.verticalLayout_30.setStretch(0, 1)
        self.verticalLayout_30.setStretch(1, 3)
        self.verticalLayout_30.setStretch(2, 1)

        self.horizontalLayout_29.addLayout(self.verticalLayout_30)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_17)

        self.label_final1 = QLabel(self.page)
        self.label_final1.setObjectName(u"label_final1")
        self.label_final1.setMinimumSize(QSize(0, 40))
        self.label_final1.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_final1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_final1)

        self.label_45 = QLabel(self.page)
        self.label_45.setObjectName(u"label_45")
        font2 = QFont()
        font2.setPointSize(40)
        self.label_45.setFont(font2)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_45)

        self.label_final2 = QLabel(self.page)
        self.label_final2.setObjectName(u"label_final2")
        self.label_final2.setMinimumSize(QSize(0, 40))
        self.label_final2.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_final2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_final2)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_18)

        self.verticalLayout_32.setStretch(0, 5)
        self.verticalLayout_32.setStretch(1, 1)
        self.verticalLayout_32.setStretch(2, 3)
        self.verticalLayout_32.setStretch(3, 1)
        self.verticalLayout_32.setStretch(4, 5)

        self.horizontalLayout_29.addLayout(self.verticalLayout_32)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.line_29 = QFrame(self.page)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.HLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_29)

        self.line_30 = QFrame(self.page)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_30)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_semi3 = QLabel(self.page)
        self.label_semi3.setObjectName(u"label_semi3")
        self.label_semi3.setMinimumSize(QSize(0, 40))
        self.label_semi3.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_semi3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_semi3)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_32)

        self.label_semi4 = QLabel(self.page)
        self.label_semi4.setObjectName(u"label_semi4")
        self.label_semi4.setMinimumSize(QSize(0, 40))
        self.label_semi4.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_semi4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_semi4)


        self.horizontalLayout_15.addLayout(self.verticalLayout_24)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 5)

        self.verticalLayout_23.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_14)

        self.verticalLayout_23.setStretch(0, 1)
        self.verticalLayout_23.setStretch(1, 3)
        self.verticalLayout_23.setStretch(2, 1)

        self.horizontalLayout_29.addLayout(self.verticalLayout_23)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_22)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.line_53 = QFrame(self.page)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.Shape.HLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_53)

        self.line_54 = QFrame(self.page)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_54)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_cuartos5 = QLabel(self.page)
        self.label_cuartos5.setObjectName(u"label_cuartos5")
        self.label_cuartos5.setMinimumSize(QSize(0, 40))
        self.label_cuartos5.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_cuartos5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_11)

        self.label_cuartos6 = QLabel(self.page)
        self.label_cuartos6.setObjectName(u"label_cuartos6")
        self.label_cuartos6.setMinimumSize(QSize(0, 40))
        self.label_cuartos6.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_cuartos6)


        self.horizontalLayout_27.addLayout(self.verticalLayout_42)

        self.horizontalLayout_27.setStretch(0, 2)
        self.horizontalLayout_27.setStretch(1, 1)
        self.horizontalLayout_27.setStretch(2, 5)

        self.verticalLayout_41.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_23)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.line_55 = QFrame(self.page)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.Shape.HLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_28.addWidget(self.line_55)

        self.line_56 = QFrame(self.page)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_28.addWidget(self.line_56)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_cuartos7 = QLabel(self.page)
        self.label_cuartos7.setObjectName(u"label_cuartos7")
        self.label_cuartos7.setMinimumSize(QSize(0, 40))
        self.label_cuartos7.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_cuartos7)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_12)

        self.label_cuartos8 = QLabel(self.page)
        self.label_cuartos8.setObjectName(u"label_cuartos8")
        self.label_cuartos8.setMinimumSize(QSize(0, 40))
        self.label_cuartos8.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_cuartos8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_cuartos8)


        self.horizontalLayout_28.addLayout(self.verticalLayout_43)

        self.horizontalLayout_28.setStretch(0, 2)
        self.horizontalLayout_28.setStretch(1, 1)
        self.horizontalLayout_28.setStretch(2, 5)

        self.verticalLayout_41.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_24)

        self.verticalLayout_41.setStretch(0, 2)
        self.verticalLayout_41.setStretch(1, 8)
        self.verticalLayout_41.setStretch(2, 6)
        self.verticalLayout_41.setStretch(3, 8)
        self.verticalLayout_41.setStretch(4, 2)

        self.horizontalLayout_29.addLayout(self.verticalLayout_41)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.line_31 = QFrame(self.page)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.HLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_31)

        self.line_32 = QFrame(self.page)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_32)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_equipo9 = QLabel(self.page)
        self.label_equipo9.setObjectName(u"label_equipo9")
        self.label_equipo9.setMinimumSize(QSize(0, 40))
        self.label_equipo9.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_equipo9)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_25)

        self.label_equipo10 = QLabel(self.page)
        self.label_equipo10.setObjectName(u"label_equipo10")
        self.label_equipo10.setMinimumSize(QSize(0, 40))
        self.label_equipo10.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_equipo10)


        self.horizontalLayout_16.addLayout(self.verticalLayout_26)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 5)

        self.verticalLayout_25.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_31)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.line_33 = QFrame(self.page)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_17.addWidget(self.line_33)

        self.line_34 = QFrame(self.page)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_17.addWidget(self.line_34)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_equipo11 = QLabel(self.page)
        self.label_equipo11.setObjectName(u"label_equipo11")
        self.label_equipo11.setMinimumSize(QSize(0, 40))
        self.label_equipo11.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_equipo11)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_26)

        self.label_equipo12 = QLabel(self.page)
        self.label_equipo12.setObjectName(u"label_equipo12")
        self.label_equipo12.setMinimumSize(QSize(0, 40))
        self.label_equipo12.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_equipo12)


        self.horizontalLayout_17.addLayout(self.verticalLayout_27)

        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 1)
        self.horizontalLayout_17.setStretch(2, 5)

        self.verticalLayout_25.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_30)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.line_35 = QFrame(self.page)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.HLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_35)

        self.line_36 = QFrame(self.page)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_36)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_equipo13 = QLabel(self.page)
        self.label_equipo13.setObjectName(u"label_equipo13")
        self.label_equipo13.setMinimumSize(QSize(0, 40))
        self.label_equipo13.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_equipo13)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_27)

        self.label_equipo14 = QLabel(self.page)
        self.label_equipo14.setObjectName(u"label_equipo14")
        self.label_equipo14.setMinimumSize(QSize(0, 40))
        self.label_equipo14.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_equipo14)


        self.horizontalLayout_18.addLayout(self.verticalLayout_28)

        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(1, 1)
        self.horizontalLayout_18.setStretch(2, 5)

        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_29)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.line_37 = QFrame(self.page)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.HLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_37)

        self.line_38 = QFrame(self.page)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_38)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_equipo15 = QLabel(self.page)
        self.label_equipo15.setObjectName(u"label_equipo15")
        self.label_equipo15.setMinimumSize(QSize(0, 40))
        self.label_equipo15.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_equipo15)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_28)

        self.label_equipo16 = QLabel(self.page)
        self.label_equipo16.setObjectName(u"label_equipo16")
        self.label_equipo16.setMinimumSize(QSize(0, 40))
        self.label_equipo16.setStyleSheet(u"background-color: rgb(38, 126, 126);\n"
"color: rgb(255, 160, 6);\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 10pt;\n"
"font-weight: bold;")
        self.label_equipo16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_equipo16)


        self.horizontalLayout_19.addLayout(self.verticalLayout_29)

        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 5)

        self.verticalLayout_25.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_29.addLayout(self.verticalLayout_25)

        self.horizontalLayout_29.setStretch(0, 9)
        self.horizontalLayout_29.setStretch(1, 9)
        self.horizontalLayout_29.setStretch(2, 9)
        self.horizontalLayout_29.setStretch(3, 10)
        self.horizontalLayout_29.setStretch(4, 9)
        self.horizontalLayout_29.setStretch(5, 9)
        self.horizontalLayout_29.setStretch(6, 9)

        self.horizontalLayout.addLayout(self.horizontalLayout_29)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 970, 33))
        self.menuNuevo = QMenu(self.menubar)
        self.menuNuevo.setObjectName(u"menuNuevo")
        self.menuListados = QMenu(self.menubar)
        self.menuListados.setObjectName(u"menuListados")
        self.menuGeston_torneo = QMenu(self.menubar)
        self.menuGeston_torneo.setObjectName(u"menuGeston_torneo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuNuevo.menuAction())
        self.menubar.addAction(self.menuListados.menuAction())
        self.menubar.addAction(self.menuGeston_torneo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuNuevo.addAction(self.actionRegistrar_Equipo)
        self.menuNuevo.addAction(self.actionRegistrar_participante)
        self.menuListados.addAction(self.actionEquipos)
        self.menuListados.addAction(self.actionParticipantes)
        self.menuListados.addAction(self.actionCalendario)
        self.menuGeston_torneo.addAction(self.actionCrear_partido)
        self.menuGeston_torneo.addAction(self.actionInicio_Partido)
        self.menuAyuda.addAction(self.actionGuia)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.toolBar.addAction(self.actionInicio)
        self.toolBar.addAction(self.actionCalendario)
        self.toolBar.addAction(self.actionInicio_Partido)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRegistrar_Equipo.setText(QCoreApplication.translate("MainWindow", u"Registrar Equipo", None))
        self.actionRegistrar_participante.setText(QCoreApplication.translate("MainWindow", u"Registrar participante", None))
        self.actionEquipos.setText(QCoreApplication.translate("MainWindow", u"Equipos", None))
        self.actionParticipantes.setText(QCoreApplication.translate("MainWindow", u"Participantes", None))
        self.actionCrear_partido.setText(QCoreApplication.translate("MainWindow", u"Crear Partido", None))
        self.actionInicio_Partido.setText(QCoreApplication.translate("MainWindow", u"Iniciar Partido", None))
        self.actionGuia.setText(QCoreApplication.translate("MainWindow", u"Guia", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.actionCalendario.setText(QCoreApplication.translate("MainWindow", u"Calendario", None))
        self.actionInicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Torneo 2025-2026", None))
        self.label_equipo1.setText("")
        self.label_equipo2.setText("")
        self.label_equipo3.setText("")
        self.label_equipo4.setText("")
        self.label_equipo5.setText("")
        self.label_equipo6.setText("")
        self.label_equipo7.setText("")
        self.label_equipo8.setText("")
        self.label_cuartos1.setText("")
        self.label_cuartos2.setText("")
        self.label_cuartos3.setText("")
        self.label_cuartos4.setText("")
        self.label_semi1.setText("")
        self.label_semi2.setText("")
        self.label_final1.setText("")
        self.label_45.setText("")
        self.label_final2.setText("")
        self.label_semi3.setText("")
        self.label_semi4.setText("")
        self.label_cuartos5.setText("")
        self.label_cuartos6.setText("")
        self.label_cuartos7.setText("")
        self.label_cuartos8.setText("")
        self.label_equipo9.setText("")
        self.label_equipo10.setText("")
        self.label_equipo11.setText("")
        self.label_equipo12.setText("")
        self.label_equipo13.setText("")
        self.label_equipo14.setText("")
        self.label_equipo15.setText("")
        self.label_equipo16.setText("")
        self.menuNuevo.setTitle(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.menuListados.setTitle(QCoreApplication.translate("MainWindow", u"Listados", None))
        self.menuGeston_torneo.setTitle(QCoreApplication.translate("MainWindow", u"Gestion torneo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

