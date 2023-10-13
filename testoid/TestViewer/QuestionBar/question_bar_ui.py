# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question-bar.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_QuestionBar(object):
    def setupUi(self, QuestionBar):
        if not QuestionBar.objectName():
            QuestionBar.setObjectName(u"QuestionBar")
        QuestionBar.resize(351, 112)
        QuestionBar.setMaximumSize(QSize(16777215, 16777215))
        QuestionBar.setStyleSheet(u"QWidget{\n"
"	background-color: #463851;\n"
"	border: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(QuestionBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(QuestionBar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"QWidget{\n"
"	border: 4px solid #7037E8;\n"
"	border-radius: 10px;\n"
"	background-color: #83527E;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #83527E;\n"
"	height: 4px;\n"
"	margin: 0px 10px 0px 10px;\n"
"	border-radius: 0px;\n"
"	padding: 0px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #FE8BF2;\n"
"	min-width: 30px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color:  #83527E;\n"
"	width: 15px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius:5px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"	background-color: #83527E;\n"
"}\n"
"QScrollBar::sub-line:h"
                        "orizontal:pressed {	\n"
"	background-color: #83527E\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: #83527E;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"	background-color: #83527E;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {	\n"
"	background-color: #83527E;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 339, 100))
        self.SAWC.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.SAWC)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonsFrame = QFrame(self.SAWC)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy)
        self.buttonsFrame.setStyleSheet(u"QWidget {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: #83527E;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 20pt \"Iosevka NF Heavy\";\n"
"}")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.buttonsFrameLayout = QHBoxLayout(self.buttonsFrame)
        self.buttonsFrameLayout.setSpacing(0)
        self.buttonsFrameLayout.setObjectName(u"buttonsFrameLayout")
        self.buttonsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.testBtn = QPushButton(self.buttonsFrame)
        self.testBtn.setObjectName(u"testBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy1)
        self.testBtn.setMinimumSize(QSize(50, 0))
        self.testBtn.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.testBtn.setFont(font)
        self.testBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #83527E;\n"
"	border-right: 2px solid #DF7C7C;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(238, 80, 80, 255), stop:0.429268 rgba(131, 82, 126, 255));\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.501, y1:0.00568182, x2:0.510467, y2:1, stop:0 rgba(131, 82, 126, 255), stop:1 rgba(234, 108, 221, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.15122 rgba(238, 80, 80, 255), stop:0.473171 rgba(223, 106, 211, 255))\n"
"}")

        self.buttonsFrameLayout.addWidget(self.testBtn)


        self.horizontalLayout_2.addWidget(self.buttonsFrame, 0, Qt.AlignLeft)

        self.scrollArea.setWidget(self.SAWC)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(QuestionBar)

        QMetaObject.connectSlotsByName(QuestionBar)
    # setupUi

    def retranslateUi(self, QuestionBar):
        QuestionBar.setWindowTitle(QCoreApplication.translate("QuestionBar", u"Form", None))
        self.testBtn.setText(QCoreApplication.translate("QuestionBar", u"1", None))
    # retranslateUi

