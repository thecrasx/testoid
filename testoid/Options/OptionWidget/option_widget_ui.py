# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option-widget.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_OptionWidget(object):
    def setupUi(self, OptionWidget):
        if not OptionWidget.objectName():
            OptionWidget.setObjectName(u"OptionWidget")
        OptionWidget.resize(311, 56)
        self.optionWidgetLayout = QHBoxLayout(OptionWidget)
        self.optionWidgetLayout.setSpacing(150)
        self.optionWidgetLayout.setObjectName(u"optionWidgetLayout")
        self.optionWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.optionLabel = QLabel(OptionWidget)
        self.optionLabel.setObjectName(u"optionLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Medium"])
        font.setPointSize(12)
        self.optionLabel.setFont(font)
        self.optionLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.optionWidgetLayout.addWidget(self.optionLabel, 0, Qt.AlignLeft)

        self.optionsFrame = QFrame(OptionWidget)
        self.optionsFrame.setObjectName(u"optionsFrame")
        self.optionsFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.optionsFrame.setFrameShape(QFrame.StyledPanel)
        self.optionsFrame.setFrameShadow(QFrame.Raised)
        self.optionsFrameLayout = QHBoxLayout(self.optionsFrame)
        self.optionsFrameLayout.setSpacing(0)
        self.optionsFrameLayout.setObjectName(u"optionsFrameLayout")
        self.optionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.prevBtn = QPushButton(self.optionsFrame)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/icons/chevron-left-rounded-hover.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevBtn.setIcon(icon)
        self.prevBtn.setIconSize(QSize(32, 32))

        self.optionsFrameLayout.addWidget(self.prevBtn, 0, Qt.AlignLeft)

        self.currentOptionLabel = QLabel(self.optionsFrame)
        self.currentOptionLabel.setObjectName(u"currentOptionLabel")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(11)
        self.currentOptionLabel.setFont(font1)
        self.currentOptionLabel.setStyleSheet(u"QLabel {\n"
"	color: #F3D6D6;\n"
"}")

        self.optionsFrameLayout.addWidget(self.currentOptionLabel, 0, Qt.AlignHCenter)

        self.nextBtn = QPushButton(self.optionsFrame)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../res/icons/chevron-right-rounded-hover.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon1)
        self.nextBtn.setIconSize(QSize(32, 32))

        self.optionsFrameLayout.addWidget(self.nextBtn, 0, Qt.AlignRight)


        self.optionWidgetLayout.addWidget(self.optionsFrame)


        self.retranslateUi(OptionWidget)

        QMetaObject.connectSlotsByName(OptionWidget)





    # setupUi
    def retranslateUi(self, OptionWidget):
        OptionWidget.setWindowTitle(QCoreApplication.translate("OptionWidget", u"Form", None))
        self.optionLabel.setText(QCoreApplication.translate("OptionWidget", u"Text", None))
        self.prevBtn.setText("")
        self.currentOptionLabel.setText(QCoreApplication.translate("OptionWidget", u"current", None))
        self.nextBtn.setText("")
    # retranslateUi

