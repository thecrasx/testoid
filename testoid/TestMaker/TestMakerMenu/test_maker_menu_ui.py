# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-maker-menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TestMakerMenu(object):
    def setupUi(self, TestMakerMenu):
        if not TestMakerMenu.objectName():
            TestMakerMenu.setObjectName(u"TestMakerMenu")
        TestMakerMenu.resize(258, 531)
        TestMakerMenu.setStyleSheet(u"QWidget {\n"
"	border: none;	\n"
"	background-color: #221B2B;\n"
"}")
        self.testMakerMenuLayout = QVBoxLayout(TestMakerMenu)
        self.testMakerMenuLayout.setSpacing(0)
        self.testMakerMenuLayout.setObjectName(u"testMakerMenuLayout")
        self.testMakerMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(TestMakerMenu)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.topFrameLayout = QVBoxLayout(self.topFrame)
        self.topFrameLayout.setSpacing(0)
        self.topFrameLayout.setObjectName(u"topFrameLayout")
        self.topFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.topButtonFrame = QFrame(self.topFrame)
        self.topButtonFrame.setObjectName(u"topButtonFrame")
        self.topButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.topButtonFrame.setFrameShadow(QFrame.Raised)
        self.topButtonFrameLayout = QVBoxLayout(self.topButtonFrame)
        self.topButtonFrameLayout.setSpacing(10)
        self.topButtonFrameLayout.setObjectName(u"topButtonFrameLayout")
        self.topButtonFrameLayout.setContentsMargins(20, 26, 20, 0)
        self.testConfiguratorBtn = QPushButton(self.topButtonFrame)
        self.testConfiguratorBtn.setObjectName(u"testConfiguratorBtn")
        self.testConfiguratorBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.topButtonFrameLayout.addWidget(self.testConfiguratorBtn)

        self.questionMakerBtn = QPushButton(self.topButtonFrame)
        self.questionMakerBtn.setObjectName(u"questionMakerBtn")
        self.questionMakerBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.topButtonFrameLayout.addWidget(self.questionMakerBtn)

        self.saveBtn = QPushButton(self.topButtonFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.topButtonFrameLayout.addWidget(self.saveBtn)


        self.topFrameLayout.addWidget(self.topButtonFrame, 0, Qt.AlignTop)


        self.testMakerMenuLayout.addWidget(self.topFrame)

        self.bottomFrame = QFrame(TestMakerMenu)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #221B2B;\n"
"}")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.bottomFrameLayout = QHBoxLayout(self.bottomFrame)
        self.bottomFrameLayout.setSpacing(0)
        self.bottomFrameLayout.setObjectName(u"bottomFrameLayout")
        self.bottomFrameLayout.setContentsMargins(15, 0, 0, 15)
        self.backBtn = QPushButton(self.bottomFrame)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px 5px 10px\n"
"}")

        self.bottomFrameLayout.addWidget(self.backBtn)


        self.testMakerMenuLayout.addWidget(self.bottomFrame, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.retranslateUi(TestMakerMenu)

        QMetaObject.connectSlotsByName(TestMakerMenu)
    # setupUi

    def retranslateUi(self, TestMakerMenu):
        TestMakerMenu.setWindowTitle(QCoreApplication.translate("TestMakerMenu", u"Form", None))
        self.testConfiguratorBtn.setText(QCoreApplication.translate("TestMakerMenu", u"Test Configuration", None))
        self.questionMakerBtn.setText(QCoreApplication.translate("TestMakerMenu", u"Questions", None))
        self.saveBtn.setText(QCoreApplication.translate("TestMakerMenu", u"Save", None))
        self.backBtn.setText(QCoreApplication.translate("TestMakerMenu", u"Back", None))
    # retranslateUi

