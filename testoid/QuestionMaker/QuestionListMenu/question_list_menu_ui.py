# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question-list-menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_QuestionListMenu(object):
    def setupUi(self, QuestionListMenu):
        if not QuestionListMenu.objectName():
            QuestionListMenu.setObjectName(u"QuestionListMenu")
        QuestionListMenu.resize(237, 370)
        QuestionListMenu.setMinimumSize(QSize(237, 370))
        QuestionListMenu.setStyleSheet(u"QWidget {\n"
"	background-color: #3C2A49;\n"
"	border: none;\n"
"}")
        self.questionListMenuLayout = QVBoxLayout(QuestionListMenu)
        self.questionListMenuLayout.setSpacing(15)
        self.questionListMenuLayout.setObjectName(u"questionListMenuLayout")
        self.questionListMenuLayout.setContentsMargins(0, 20, 0, 0)
        self.addQuestionBtn = QPushButton(QuestionListMenu)
        self.addQuestionBtn.setObjectName(u"addQuestionBtn")
        font = QFont()
        font.setFamilies([u"Iosevka NF Medium"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.addQuestionBtn.setFont(font)
        self.addQuestionBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #5F4770;\n"
"	border-radius: 7%;\n"
"	padding: 5px 35px 5px  35px;\n"
"}\n"
"\n"
"QPushButton::hover  {\n"
"	background-color: #463255;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: #3F2A4F;\n"
"}")

        self.questionListMenuLayout.addWidget(self.addQuestionBtn, 0, Qt.AlignHCenter)

        self.questionsRegion = QFrame(QuestionListMenu)
        self.questionsRegion.setObjectName(u"questionsRegion")
        self.questionsRegion.setMinimumSize(QSize(0, 300))
        self.questionsRegion.setStyleSheet(u"")
        self.questionsRegion.setFrameShape(QFrame.StyledPanel)
        self.questionsRegion.setFrameShadow(QFrame.Raised)
        self.questionsRegionLayout = QVBoxLayout(self.questionsRegion)
        self.questionsRegionLayout.setSpacing(0)
        self.questionsRegionLayout.setObjectName(u"questionsRegionLayout")
        self.questionsRegionLayout.setContentsMargins(20, 20, 20, 15)
        self.lineLabel = QLabel(self.questionsRegion)
        self.lineLabel.setObjectName(u"lineLabel")
        self.lineLabel.setMinimumSize(QSize(0, 3))
        self.lineLabel.setMaximumSize(QSize(16777215, 3))
        self.lineLabel.setStyleSheet(u"QLabel {\n"
"	background-color: #7D6292\n"
"}")

        self.questionsRegionLayout.addWidget(self.lineLabel)

        self.scrollArea = QScrollArea(self.questionsRegion)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 197, 262))
        self.SAWC.setStyleSheet(u"QWidget {\n"
"	background-color: #392646;\n"
"	border-bottom-left-radius: 5%;\n"
"	border-bottom-right-radius: 5%\n"
"}")
        self.SAWCLayout = QVBoxLayout(self.SAWC)
        self.SAWCLayout.setSpacing(0)
        self.SAWCLayout.setObjectName(u"SAWCLayout")
        self.SAWCLayout.setContentsMargins(20, 15, 20, 0)
        self.questionsFrame = QFrame(self.SAWC)
        self.questionsFrame.setObjectName(u"questionsFrame")
        self.questionsFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.questionsFrame.setFrameShape(QFrame.StyledPanel)
        self.questionsFrame.setFrameShadow(QFrame.Raised)
        self.questionsFrameLayout = QVBoxLayout(self.questionsFrame)
        self.questionsFrameLayout.setSpacing(10)
        self.questionsFrameLayout.setObjectName(u"questionsFrameLayout")
        self.questionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.questionBtn = QPushButton(self.questionsFrame)
        self.questionBtn.setObjectName(u"questionBtn")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        self.questionBtn.setFont(font1)
        self.questionBtn.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	padding-bottom: 5px;\n"
"	border-radius: 0px;\n"
"	font-family: \"Iosevka NF Medium\";\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	padding-bottom: 3px;\n"
"	border-bottom: 2px solid #9267B1;\n"
"}")

        self.questionsFrameLayout.addWidget(self.questionBtn, 0, Qt.AlignLeft)


        self.SAWCLayout.addWidget(self.questionsFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.SAWC)

        self.questionsRegionLayout.addWidget(self.scrollArea)


        self.questionListMenuLayout.addWidget(self.questionsRegion)


        self.retranslateUi(QuestionListMenu)

        QMetaObject.connectSlotsByName(QuestionListMenu)





    # setupUi
    def retranslateUi(self, QuestionListMenu):
        QuestionListMenu.setWindowTitle(QCoreApplication.translate("QuestionListMenu", u"Form", None))
        self.addQuestionBtn.setText(QCoreApplication.translate("QuestionListMenu", u"Add Question", None))
        self.lineLabel.setText("")
        self.questionBtn.setText(QCoreApplication.translate("QuestionListMenu", u"-1. question test", None))
    # retranslateUi

