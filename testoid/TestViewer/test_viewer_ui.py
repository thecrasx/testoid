# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-viewer.ui'
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
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TestViewer(object):
    def setupUi(self, TestViewer):
        if not TestViewer.objectName():
            TestViewer.setObjectName(u"TestViewer")
        TestViewer.resize(1090, 825)
        TestViewer.setStyleSheet(u"QWidget {\n"
"	border: none;\n"
"}")
        self.testViewerLayout = QVBoxLayout(TestViewer)
        self.testViewerLayout.setSpacing(30)
        self.testViewerLayout.setObjectName(u"testViewerLayout")
        self.testViewerLayout.setContentsMargins(0, 0, 0, 15)
        self.topFrame = QFrame(TestViewer)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.topFrameLayout = QVBoxLayout(self.topFrame)
        self.topFrameLayout.setSpacing(30)
        self.topFrameLayout.setObjectName(u"topFrameLayout")
        self.topFrameLayout.setContentsMargins(0, 20, 0, 0)
        self.subTopFrame = QFrame(self.topFrame)
        self.subTopFrame.setObjectName(u"subTopFrame")
        self.subTopFrame.setFrameShape(QFrame.StyledPanel)
        self.subTopFrame.setFrameShadow(QFrame.Raised)
        self.subTopFrameLayout = QHBoxLayout(self.subTopFrame)
        self.subTopFrameLayout.setSpacing(0)
        self.subTopFrameLayout.setObjectName(u"subTopFrameLayout")
        self.subTopFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.quitBtn = QPushButton(self.subTopFrame)
        self.quitBtn.setObjectName(u"quitBtn")
        font = QFont()
        font.setFamilies([u"Iosevka NFP ExtraBold"])
        font.setPointSize(11)
        font.setBold(True)
        self.quitBtn.setFont(font)
        self.quitBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #F8A48A;\n"
"	border: none;\n"
"	padding: 5px 25px 5px 25px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #F0977C;\n"
"}")

        self.subTopFrameLayout.addWidget(self.quitBtn, 0, Qt.AlignLeft)

        self.testLabel = QLabel(self.subTopFrame)
        self.testLabel.setObjectName(u"testLabel")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Heavy"])
        font1.setPointSize(16)
        self.testLabel.setFont(font1)

        self.subTopFrameLayout.addWidget(self.testLabel, 0, Qt.AlignHCenter)

        self.finishBtn = QPushButton(self.subTopFrame)
        self.finishBtn.setObjectName(u"finishBtn")
        font2 = QFont()
        font2.setFamilies([u"Iosevka NFM ExtraBold"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.finishBtn.setFont(font2)
        self.finishBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #F8A48A;\n"
"	border: none;\n"
"	padding: 5px 25px 5px 25px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #F0977C;\n"
"}")

        self.subTopFrameLayout.addWidget(self.finishBtn, 0, Qt.AlignRight)


        self.topFrameLayout.addWidget(self.subTopFrame, 0, Qt.AlignTop)

        self.questionFrame = QFrame(self.topFrame)
        self.questionFrame.setObjectName(u"questionFrame")
        self.questionFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.questionFrame.setFrameShape(QFrame.StyledPanel)
        self.questionFrame.setFrameShadow(QFrame.Raised)
        self.questionFrameLayout = QVBoxLayout(self.questionFrame)
        self.questionFrameLayout.setSpacing(0)
        self.questionFrameLayout.setObjectName(u"questionFrameLayout")
        self.questionFrameLayout.setContentsMargins(50, 0, 50, 0)
        self.questionNTypeFrame = QFrame(self.questionFrame)
        self.questionNTypeFrame.setObjectName(u"questionNTypeFrame")
        self.questionNTypeFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #4E4C6C;\n"
"	border: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"	padding: 3px 5px 3px 5px;\n"
"	color: #F1DADA;\n"
"}")
        self.questionNTypeFrame.setFrameShape(QFrame.StyledPanel)
        self.questionNTypeFrame.setFrameShadow(QFrame.Raised)
        self.questionNTypeFrameLayout = QVBoxLayout(self.questionNTypeFrame)
        self.questionNTypeFrameLayout.setSpacing(0)
        self.questionNTypeFrameLayout.setObjectName(u"questionNTypeFrameLayout")
        self.questionNTypeFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.question = QPlainTextEdit(self.questionNTypeFrame)
        self.question.setObjectName(u"question")
        font3 = QFont()
        font3.setFamilies([u"Iosevka NF Medium"])
        font3.setPointSize(12)
        self.question.setFont(font3)
        self.question.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	padding: 7px 10px 7px 10px;\n"
"	color: #F1DADA;\n"
"}")
        self.question.setReadOnly(True)

        self.questionNTypeFrameLayout.addWidget(self.question)

        self.answerTypeLabel = QLabel(self.questionNTypeFrame)
        self.answerTypeLabel.setObjectName(u"answerTypeLabel")
        font4 = QFont()
        font4.setFamilies([u"Iosevka NF Medium"])
        font4.setPointSize(13)
        self.answerTypeLabel.setFont(font4)
        self.answerTypeLabel.setStyleSheet(u"QLabel {\n"
"	color: #605E80;\n"
"}")

        self.questionNTypeFrameLayout.addWidget(self.answerTypeLabel, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.answerTypeLabel.raise_()
        self.question.raise_()

        self.questionFrameLayout.addWidget(self.questionNTypeFrame)

        self.questionButtonsFrame = QFrame(self.questionFrame)
        self.questionButtonsFrame.setObjectName(u"questionButtonsFrame")
        self.questionButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.questionButtonsFrame.setFrameShadow(QFrame.Raised)
        self.questionButtonsFrameLayout = QHBoxLayout(self.questionButtonsFrame)
        self.questionButtonsFrameLayout.setSpacing(0)
        self.questionButtonsFrameLayout.setObjectName(u"questionButtonsFrameLayout")
        self.questionButtonsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.prevNNextBtnFrame = QFrame(self.questionButtonsFrame)
        self.prevNNextBtnFrame.setObjectName(u"prevNNextBtnFrame")
        self.prevNNextBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.prevNNextBtnFrame.setFrameShadow(QFrame.Raised)
        self.prevNNextBtnFrameLayout = QHBoxLayout(self.prevNNextBtnFrame)
        self.prevNNextBtnFrameLayout.setSpacing(0)
        self.prevNNextBtnFrameLayout.setObjectName(u"prevNNextBtnFrameLayout")
        self.prevNNextBtnFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.prevBtn = QPushButton(self.prevNNextBtnFrame)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #875DA8;\n"
"	border: none;	\n"
"	border-right: 1px solid #5C3E74;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding: 5px 25px 5px 25px;\n"
"}")

        self.prevNNextBtnFrameLayout.addWidget(self.prevBtn)

        self.nextBtn = QPushButton(self.prevNNextBtnFrame)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #875DA8;\n"
"	border: none;\n"
"	border-left: 1px solid #5C3E74;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding: 5px 25px 5px 25px;\n"
"}")

        self.prevNNextBtnFrameLayout.addWidget(self.nextBtn)


        self.questionButtonsFrameLayout.addWidget(self.prevNNextBtnFrame, 0, Qt.AlignLeft)

        self.markBtn = QPushButton(self.questionButtonsFrame)
        self.markBtn.setObjectName(u"markBtn")
        self.markBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #875DA8;\n"
"	border: none;\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding: 5px 25px 5px 25px;\n"
"}")

        self.questionButtonsFrameLayout.addWidget(self.markBtn, 0, Qt.AlignRight)


        self.questionFrameLayout.addWidget(self.questionButtonsFrame)


        self.topFrameLayout.addWidget(self.questionFrame)


        self.testViewerLayout.addWidget(self.topFrame)

        self.bottomFrame = QFrame(TestViewer)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.answersSA = QScrollArea(self.bottomFrame)
        self.answersSA.setObjectName(u"answersSA")
        self.answersSA.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 1030, 487))
        self.SAWCLayout = QVBoxLayout(self.SAWC)
        self.SAWCLayout.setSpacing(0)
        self.SAWCLayout.setObjectName(u"SAWCLayout")
        self.SAWCLayout.setContentsMargins(20, 0, 20, 0)
        self.answersFrame = QFrame(self.SAWC)
        self.answersFrame.setObjectName(u"answersFrame")
        self.answersFrame.setFrameShape(QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QFrame.Raised)
        self.answersFrameLayout = QVBoxLayout(self.answersFrame)
        self.answersFrameLayout.setSpacing(20)
        self.answersFrameLayout.setObjectName(u"answersFrameLayout")
        self.answersFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.answersFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	padding: 20px 10px 20px 10px;\n"
"	background: #191d31;\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border-radius: 15px;\n"
"}")

        self.answersFrameLayout.addWidget(self.label)


        self.SAWCLayout.addWidget(self.answersFrame, 0, Qt.AlignTop)

        self.answersSA.setWidget(self.SAWC)

        self.verticalLayout_3.addWidget(self.answersSA)

        self.questionBarFrame = QFrame(self.bottomFrame)
        self.questionBarFrame.setObjectName(u"questionBarFrame")
        self.questionBarFrame.setFrameShape(QFrame.StyledPanel)
        self.questionBarFrame.setFrameShadow(QFrame.Raised)
        self.questionBarFrameLayout = QHBoxLayout(self.questionBarFrame)
        self.questionBarFrameLayout.setSpacing(0)
        self.questionBarFrameLayout.setObjectName(u"questionBarFrameLayout")
        self.questionBarFrameLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.questionBarFrame, 0, Qt.AlignBottom)


        self.testViewerLayout.addWidget(self.bottomFrame)

        self.testViewerLayout.setStretch(0, 3)
        self.testViewerLayout.setStretch(1, 5)

        self.retranslateUi(TestViewer)

        QMetaObject.connectSlotsByName(TestViewer)
    # setupUi

    def retranslateUi(self, TestViewer):
        TestViewer.setWindowTitle(QCoreApplication.translate("TestViewer", u"Form", None))
        self.quitBtn.setText(QCoreApplication.translate("TestViewer", u"Quit", None))
        self.testLabel.setText(QCoreApplication.translate("TestViewer", u"Test", None))
        self.finishBtn.setText(QCoreApplication.translate("TestViewer", u"Overview", None))
        self.question.setPlainText(QCoreApplication.translate("TestViewer", u"aaaa", None))
        self.answerTypeLabel.setText(QCoreApplication.translate("TestViewer", u"answer type: multiple choice", None))
        self.prevBtn.setText("")
        self.nextBtn.setText("")
        self.markBtn.setText(QCoreApplication.translate("TestViewer", u"Mark", None))
        self.label.setText(QCoreApplication.translate("TestViewer", u"text", None))
    # retranslateUi

