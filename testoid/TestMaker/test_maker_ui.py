# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-maker.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_TestMaker(object):
    def setupUi(self, TestMaker):
        if not TestMaker.objectName():
            TestMaker.setObjectName(u"TestMaker")
        TestMaker.resize(682, 550)
        self.testMakerLayout = QVBoxLayout(TestMaker)
        self.testMakerLayout.setSpacing(0)
        self.testMakerLayout.setObjectName(u"testMakerLayout")
        self.testMakerLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(TestMaker)
        self.pages.setObjectName(u"pages")
        self.testConfiguratorPage = QWidget()
        self.testConfiguratorPage.setObjectName(u"testConfiguratorPage")
        self.testConfiguratorPageLayout = QVBoxLayout(self.testConfiguratorPage)
        self.testConfiguratorPageLayout.setSpacing(0)
        self.testConfiguratorPageLayout.setObjectName(u"testConfiguratorPageLayout")
        self.testConfiguratorPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.testConfiguratorPage)
        self.questionMakerPage = QWidget()
        self.questionMakerPage.setObjectName(u"questionMakerPage")
        self.questionMakerPageLayout = QVBoxLayout(self.questionMakerPage)
        self.questionMakerPageLayout.setSpacing(0)
        self.questionMakerPageLayout.setObjectName(u"questionMakerPageLayout")
        self.questionMakerPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.questionMakerPage)

        self.testMakerLayout.addWidget(self.pages)


        self.retranslateUi(TestMaker)

        QMetaObject.connectSlotsByName(TestMaker)





    # setupUi
    def retranslateUi(self, TestMaker):
        TestMaker.setWindowTitle(QCoreApplication.translate("TestMaker", u"Form", None))
    # retranslateUi

