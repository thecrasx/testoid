# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'make-question-answer.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Answer(object):
    def setupUi(self, Answer):
        if not Answer.objectName():
            Answer.setObjectName(u"Answer")
        Answer.resize(680, 200)
        Answer.setMinimumSize(QSize(408, 141))
        self.verticalLayout = QVBoxLayout(Answer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.answerRegionFrame = QFrame(Answer)
        self.answerRegionFrame.setObjectName(u"answerRegionFrame")
        self.answerRegionFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.answerRegionFrame.setFrameShape(QFrame.StyledPanel)
        self.answerRegionFrame.setFrameShadow(QFrame.Raised)
        self.answerRegionFrameLayout = QHBoxLayout(self.answerRegionFrame)
        self.answerRegionFrameLayout.setSpacing(5)
        self.answerRegionFrameLayout.setObjectName(u"answerRegionFrameLayout")
        self.answerRegionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.answerFrame = QFrame(self.answerRegionFrame)
        self.answerFrame.setObjectName(u"answerFrame")
        self.answerFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #715A83;\n"
"	border-radius: 20%;\n"
"}")
        self.answerFrame.setFrameShape(QFrame.StyledPanel)
        self.answerFrame.setFrameShadow(QFrame.Raised)
        self.answerFrameLayout = QHBoxLayout(self.answerFrame)
        self.answerFrameLayout.setSpacing(0)
        self.answerFrameLayout.setObjectName(u"answerFrameLayout")
        self.answerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.answerTextEdit = QPlainTextEdit(self.answerFrame)
        self.answerTextEdit.setObjectName(u"answerTextEdit")
        font = QFont()
        font.setFamilies([u"Iosevka NF Medium"])
        font.setPointSize(12)
        self.answerTextEdit.setFont(font)
        self.answerTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	border: none;\n"
"	padding: 7px 10px 7px 10px;\n"
"	color: #FAEAEA;\n"
"}")

        self.answerFrameLayout.addWidget(self.answerTextEdit)

        self.checkBtn = QPushButton(self.answerFrame)
        self.checkBtn.setObjectName(u"checkBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBtn.sizePolicy().hasHeightForWidth())
        self.checkBtn.setSizePolicy(sizePolicy)
        self.checkBtn.setMaximumSize(QSize(60, 16777215))
        self.checkBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #9B71BC;\n"
"	border-top-right-radius: 20%;\n"
"	border-bottom-right-radius: 20%\n"
" }")

        self.answerFrameLayout.addWidget(self.checkBtn)

        self.answerFrameLayout.setStretch(0, 8)
        self.answerFrameLayout.setStretch(1, 1)

        self.answerRegionFrameLayout.addWidget(self.answerFrame)

        self.removeBtn = QPushButton(self.answerRegionFrame)
        self.removeBtn.setObjectName(u"removeBtn")
        self.removeBtn.setStyleSheet(u"QPushButton {\n"
"	border : none;\n"
"	padding: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/round-close-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeBtn.setIcon(icon)
        self.removeBtn.setIconSize(QSize(32, 32))

        self.answerRegionFrameLayout.addWidget(self.removeBtn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.answerRegionFrame)

        self.explanationReginFrame = QFrame(Answer)
        self.explanationReginFrame.setObjectName(u"explanationReginFrame")
        self.explanationReginFrame.setMinimumSize(QSize(0, 0))
        self.explanationReginFrame.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border: none;\n"
"	margin-right: 37px;\n"
"}")
        self.explanationReginFrame.setFrameShape(QFrame.StyledPanel)
        self.explanationReginFrame.setFrameShadow(QFrame.Raised)
        self.explanationReginFrameLayout = QVBoxLayout(self.explanationReginFrame)
        self.explanationReginFrameLayout.setSpacing(0)
        self.explanationReginFrameLayout.setObjectName(u"explanationReginFrameLayout")
        self.explanationReginFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.addExplanationBtn = QPushButton(self.explanationReginFrame)
        self.addExplanationBtn.setObjectName(u"addExplanationBtn")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(11)
        self.addExplanationBtn.setFont(font1)
        self.addExplanationBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #8C61AD;\n"
"	border: none;\n"
"	padding: 5% 50% 5% 50%;\n"
"	border-bottom-left-radius: 10%;\n"
"	border-bottom-right-radius: 10%\n"
"}")

        self.explanationReginFrameLayout.addWidget(self.addExplanationBtn)


        self.verticalLayout.addWidget(self.explanationReginFrame, 0, Qt.AlignHCenter)


        self.retranslateUi(Answer)

        QMetaObject.connectSlotsByName(Answer)





    # setupUi
    def retranslateUi(self, Answer):
        Answer.setWindowTitle(QCoreApplication.translate("Answer", u"Form", None))
        self.answerTextEdit.setPlainText("")
        self.checkBtn.setText("")
        self.removeBtn.setText("")
        self.addExplanationBtn.setText(QCoreApplication.translate("Answer", u"Add Explanation", None))
    # retranslateUi

