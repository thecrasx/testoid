# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-menu-widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TestWidget(object):
    def setupUi(self, TestWidget):
        if not TestWidget.objectName():
            TestWidget.setObjectName(u"TestWidget")
        TestWidget.resize(559, 326)
        self.verticalLayout_2 = QVBoxLayout(TestWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.mainFrame = QFrame(TestWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #5F4F6B;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scoreFrame = QFrame(self.topFrame)
        self.scoreFrame.setObjectName(u"scoreFrame")
        self.scoreFrame.setFrameShape(QFrame.StyledPanel)
        self.scoreFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.scoreFrame, 0, Qt.AlignLeft)

        self.favBtnFrame = QFrame(self.topFrame)
        self.favBtnFrame.setObjectName(u"favBtnFrame")
        self.favBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.favBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.favBtnFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 13, 8, 0)
        self.favoriteBtn = QPushButton(self.favBtnFrame)
        self.favoriteBtn.setObjectName(u"favoriteBtn")
        self.favoriteBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/icons/test-menu-widget-fav-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.favoriteBtn.setIcon(icon)
        self.favoriteBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.favoriteBtn)


        self.horizontalLayout.addWidget(self.favBtnFrame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.topFrame, 0, Qt.AlignTop)

        self.middleFrame = QFrame(self.mainFrame)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy)
        self.middleFrame.setFrameShape(QFrame.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.middleFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.testLabel = QLabel(self.middleFrame)
        self.testLabel.setObjectName(u"testLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.testLabel.setFont(font)
        self.testLabel.setAlignment(Qt.AlignCenter)
        self.testLabel.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.testLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.middleFrame)

        self.bottomFrame = QFrame(self.mainFrame)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.statsBtnFrame = QFrame(self.bottomFrame)
        self.statsBtnFrame.setObjectName(u"statsBtnFrame")
        self.statsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.statsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.statsBtnFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(14, 0, 0, 3)
        self.statsBtn = QPushButton(self.statsBtnFrame)
        self.statsBtn.setObjectName(u"statsBtn")
        self.statsBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../res/icons/stats-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsBtn.setIcon(icon1)
        self.statsBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_5.addWidget(self.statsBtn)


        self.horizontalLayout_4.addWidget(self.statsBtnFrame, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.bottomFrame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.mainFrame)


        self.retranslateUi(TestWidget)

        QMetaObject.connectSlotsByName(TestWidget)
    # setupUi

    def retranslateUi(self, TestWidget):
        TestWidget.setWindowTitle(QCoreApplication.translate("TestWidget", u"Form", None))
        self.favoriteBtn.setText("")
        self.testLabel.setText(QCoreApplication.translate("TestWidget", u"Test", None))
        self.statsBtn.setText("")
    # retranslateUi

