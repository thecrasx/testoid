# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result-viewer-question.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_RVQuestion(object):
    def setupUi(self, RVQuestion):
        if not RVQuestion.objectName():
            RVQuestion.setObjectName(u"RVQuestion")
        RVQuestion.resize(443, 250)
        RVQuestion.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(RVQuestion)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.questionFrame = QFrame(RVQuestion)
        self.questionFrame.setObjectName(u"questionFrame")
        self.questionFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #994D4D;\n"
"	border-width: 0px 0px 15px 0px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.499686, y2:1, stop:0 rgba(153, 77, 77, 255), stop:1 rgba(0, 0, 0, 139))\n"
"}")
        self.questionFrame.setFrameShape(QFrame.StyledPanel)
        self.questionFrame.setFrameShadow(QFrame.Raised)
        self.questionFrameLayout_2 = QVBoxLayout(self.questionFrame)
        self.questionFrameLayout_2.setSpacing(30)
        self.questionFrameLayout_2.setObjectName(u"questionFrameLayout_2")
        self.questionFrameLayout_2.setContentsMargins(0, 0, 0, 50)
        self.questionLabel = QLabel(self.questionFrame)
        self.questionLabel.setObjectName(u"questionLabel")
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(14)
        self.questionLabel.setFont(font)
        self.questionLabel.setStyleSheet(u"QLabel {\n"
"	padding: 20px 10px 10px 10px ;\n"
"	border: none;\n"
"	color: #CFBDBD;\n"
"}")
        self.questionLabel.setWordWrap(True)

        self.questionFrameLayout_2.addWidget(self.questionLabel)

        self.answersFrame = QFrame(self.questionFrame)
        self.answersFrame.setObjectName(u"answersFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answersFrame.sizePolicy().hasHeightForWidth())
        self.answersFrame.setSizePolicy(sizePolicy)
        self.answersFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.answersFrame.setFrameShape(QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QFrame.Raised)
        self.answersFrameLayout_2 = QVBoxLayout(self.answersFrame)
        self.answersFrameLayout_2.setSpacing(10)
        self.answersFrameLayout_2.setObjectName(u"answersFrameLayout_2")
        self.answersFrameLayout_2.setContentsMargins(23, 0, 0, 0)
        self.wrongAnswerFrame = QFrame(self.answersFrame)
        self.wrongAnswerFrame.setObjectName(u"wrongAnswerFrame")
        sizePolicy.setHeightForWidth(self.wrongAnswerFrame.sizePolicy().hasHeightForWidth())
        self.wrongAnswerFrame.setSizePolicy(sizePolicy)
        self.wrongAnswerFrame.setFrameShape(QFrame.StyledPanel)
        self.wrongAnswerFrame.setFrameShadow(QFrame.Raised)
        self.wrongAnswerFrameLayout = QHBoxLayout(self.wrongAnswerFrame)
        self.wrongAnswerFrameLayout.setSpacing(7)
        self.wrongAnswerFrameLayout.setObjectName(u"wrongAnswerFrameLayout")
        self.wrongAnswerFrameLayout.setContentsMargins(0, 10, 0, 10)
        self.wrongIndicatorLabel = QLabel(self.wrongAnswerFrame)
        self.wrongIndicatorLabel.setObjectName(u"wrongIndicatorLabel")
        self.wrongIndicatorLabel.setMinimumSize(QSize(12, 15))
        self.wrongIndicatorLabel.setMaximumSize(QSize(12, 15))
        self.wrongIndicatorLabel.setStyleSheet(u"QLabel {\n"
"    background-color: #C10707;\n"
"	margin-top: 3px;\n"
"	border-radius: 6px;\n"
"}")
        self.wrongIndicatorLabel.setWordWrap(False)

        self.wrongAnswerFrameLayout.addWidget(self.wrongIndicatorLabel, 0, Qt.AlignTop)

        self.wrongAnswerLabel = QLabel(self.wrongAnswerFrame)
        self.wrongAnswerLabel.setObjectName(u"wrongAnswerLabel")
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(12)
        self.wrongAnswerLabel.setFont(font1)
        self.wrongAnswerLabel.setStyleSheet(u"QLabel {\n"
"	color: #5C0101;\n"
"}")
        self.wrongAnswerLabel.setScaledContents(False)
        self.wrongAnswerLabel.setWordWrap(True)

        self.wrongAnswerFrameLayout.addWidget(self.wrongAnswerLabel, 0, Qt.AlignTop)


        self.answersFrameLayout_2.addWidget(self.wrongAnswerFrame)

        self.correctAnswerFrame = QFrame(self.answersFrame)
        self.correctAnswerFrame.setObjectName(u"correctAnswerFrame")
        sizePolicy.setHeightForWidth(self.correctAnswerFrame.sizePolicy().hasHeightForWidth())
        self.correctAnswerFrame.setSizePolicy(sizePolicy)
        self.correctAnswerFrame.setFrameShape(QFrame.StyledPanel)
        self.correctAnswerFrame.setFrameShadow(QFrame.Raised)
        self.correctAnswerFrameLayout = QHBoxLayout(self.correctAnswerFrame)
        self.correctAnswerFrameLayout.setSpacing(7)
        self.correctAnswerFrameLayout.setObjectName(u"correctAnswerFrameLayout")
        self.correctAnswerFrameLayout.setContentsMargins(0, 10, 0, 10)
        self.correctIndicatorLabel = QLabel(self.correctAnswerFrame)
        self.correctIndicatorLabel.setObjectName(u"correctIndicatorLabel")
        self.correctIndicatorLabel.setMinimumSize(QSize(12, 15))
        self.correctIndicatorLabel.setMaximumSize(QSize(12, 15))
        self.correctIndicatorLabel.setStyleSheet(u"QLabel {\n"
"    background-color: #2EBC17;\n"
"	margin-top: 3px;\n"
"	border-radius: 6px;\n"
"}")
        self.correctIndicatorLabel.setWordWrap(False)

        self.correctAnswerFrameLayout.addWidget(self.correctIndicatorLabel, 0, Qt.AlignTop)

        self.correctAnswerLabel = QLabel(self.correctAnswerFrame)
        self.correctAnswerLabel.setObjectName(u"correctAnswerLabel")
        self.correctAnswerLabel.setFont(font1)
        self.correctAnswerLabel.setStyleSheet(u"QLabel {\n"
"	color: #17AF27;\n"
"}")
        self.correctAnswerLabel.setScaledContents(False)
        self.correctAnswerLabel.setWordWrap(True)

        self.correctAnswerFrameLayout.addWidget(self.correctAnswerLabel, 0, Qt.AlignTop)


        self.answersFrameLayout_2.addWidget(self.correctAnswerFrame)


        self.questionFrameLayout_2.addWidget(self.answersFrame)


        self.verticalLayout_2.addWidget(self.questionFrame)


        self.retranslateUi(RVQuestion)

        QMetaObject.connectSlotsByName(RVQuestion)





    # setupUi
    def retranslateUi(self, RVQuestion):
        RVQuestion.setWindowTitle(QCoreApplication.translate("RVQuestion", u"Form", None))
        self.questionLabel.setText(QCoreApplication.translate("RVQuestion", u"Text", None))
        self.wrongIndicatorLabel.setText("")
        self.wrongAnswerLabel.setText(QCoreApplication.translate("RVQuestion", u"Text", None))
        self.correctIndicatorLabel.setText("")
        self.correctAnswerLabel.setText(QCoreApplication.translate("RVQuestion", u"Text", None))
    # retranslateUi

