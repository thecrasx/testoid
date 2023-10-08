# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TestMenu(object):
    def setupUi(self, TestMenu):
        if not TestMenu.objectName():
            TestMenu.setObjectName(u"TestMenu")
        TestMenu.resize(1018, 671)
        TestMenu.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(TestMenu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(TestMenu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1018, 671))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: #463851;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.scrollAreaWidgetContents)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setMinimumSize(QSize(0, 0))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #463851;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QGridLayout(self.mainFrame)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.addTestBtn = QPushButton(self.mainFrame)
        self.addTestBtn.setObjectName(u"addTestBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTestBtn.sizePolicy().hasHeightForWidth())
        self.addTestBtn.setSizePolicy(sizePolicy)
        self.addTestBtn.setMinimumSize(QSize(0, 139))
        self.addTestBtn.setStyleSheet(u"QPushButton {\n"
"	background: #4F405B;\n"
"	border: 2px solid #5A4E64;\n"
"	border-radius: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"}")

        self.mainFrameLayout.addWidget(self.addTestBtn, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.mainFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(TestMenu)

        QMetaObject.connectSlotsByName(TestMenu)





    # setupUi
    def retranslateUi(self, TestMenu):
        TestMenu.setWindowTitle(QCoreApplication.translate("TestMenu", u"Form", None))
        self.addTestBtn.setText(QCoreApplication.translate("TestMenu", u"ADD", None))
    # retranslateUi

