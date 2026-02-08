# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reloj_digital.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(302, 208)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_message = QLabel(Form)
        self.lbl_message.setObjectName(u"lbl_message")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.lbl_message.setFont(font)
        self.lbl_message.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")
        self.lbl_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_message)

        self.lcd_time = QLCDNumber(Form)
        self.lcd_time.setObjectName(u"lcd_time")
        self.lcd_time.setStyleSheet(u"    background-color: rgb(27, 90, 90);\n"
"    color: rgb(94, 207, 207);\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 10px;")

        self.verticalLayout.addWidget(self.lcd_time)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_message.setText(QCoreApplication.translate("Form", u"ALERTAS", None))
    # retranslateUi

