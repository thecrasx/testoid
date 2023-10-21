# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overview.ui'
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
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Overview(object):
    def setupUi(self, Overview):
        if not Overview.objectName():
            Overview.setObjectName(u"Overview")
        Overview.resize(624, 449)
        Overview.setStyleSheet(u"background-color: #463851;\n"
"border: none;")
        self.overviewLayout = QVBoxLayout(Overview)
        self.overviewLayout.setSpacing(0)
        self.overviewLayout.setObjectName(u"overviewLayout")
        self.overviewLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(Overview)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)
        self.mainFrameLayout.setSpacing(15)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.mainFrameLayout.setContentsMargins(0, 0, 0, 30)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.topFrameLayout = QHBoxLayout(self.topFrame)
        self.topFrameLayout.setSpacing(0)
        self.topFrameLayout.setObjectName(u"topFrameLayout")
        self.topFrameLayout.setContentsMargins(0, 10, 10, 0)
        self.closeBtn = QPushButton(self.topFrame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../res/icons/round-close-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setIconSize(QSize(32, 32))

        self.topFrameLayout.addWidget(self.closeBtn, 0, Qt.AlignRight)


        self.mainFrameLayout.addWidget(self.topFrame)

        self.scrollArea = QScrollArea(self.mainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 624, 362))
        self.scrollAreaLayout = QVBoxLayout(self.SAWC)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.questionsFrame = QFrame(self.SAWC)
        self.questionsFrame.setObjectName(u"questionsFrame")
        self.questionsFrame.setFrameShape(QFrame.StyledPanel)
        self.questionsFrame.setFrameShadow(QFrame.Raised)
        self.questionsFrameLayout = QVBoxLayout(self.questionsFrame)
        self.questionsFrameLayout.setSpacing(20)
        self.questionsFrameLayout.setObjectName(u"questionsFrameLayout")
        self.questionsFrameLayout.setContentsMargins(30, 0, 15, 30)

        self.scrollAreaLayout.addWidget(self.questionsFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.SAWC)

        self.mainFrameLayout.addWidget(self.scrollArea)


        self.overviewLayout.addWidget(self.mainFrame)


        self.retranslateUi(Overview)

        QMetaObject.connectSlotsByName(Overview)
    # setupUi

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QCoreApplication.translate("Overview", u"Form", None))
        self.closeBtn.setText("")
    # retranslateUi

