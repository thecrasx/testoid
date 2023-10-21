# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overview-question.ui'
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

class Ui_QuestionOverview(object):
    def setupUi(self, QuestionOverview):
        if not QuestionOverview.objectName():
            QuestionOverview.setObjectName(u"QuestionOverview")
        QuestionOverview.resize(787, 482)
        self.overviewQuestionLayout = QVBoxLayout(QuestionOverview)
        self.overviewQuestionLayout.setSpacing(0)
        self.overviewQuestionLayout.setObjectName(u"overviewQuestionLayout")
        self.overviewQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(QuestionOverview)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #69537B;\n"
"	border: none;\n"
"	border-bottom: 5px solid #3C284D;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)
        self.mainFrameLayout.setSpacing(15)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.mainFrameLayout.setContentsMargins(15, 15, 15, 50)
        self.questionInfoFrame = QFrame(self.mainFrame)
        self.questionInfoFrame.setObjectName(u"questionInfoFrame")
        self.questionInfoFrame.setStyleSheet(u"border: none;")
        self.questionInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.questionInfoFrame.setFrameShadow(QFrame.Raised)
        self.questionInfoFrameLayout = QHBoxLayout(self.questionInfoFrame)
        self.questionInfoFrameLayout.setSpacing(0)
        self.questionInfoFrameLayout.setObjectName(u"questionInfoFrameLayout")
        self.questionInfoFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.questionNumberLabel = QLabel(self.questionInfoFrame)
        self.questionNumberLabel.setObjectName(u"questionNumberLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(21)
        self.questionNumberLabel.setFont(font)
        self.questionNumberLabel.setStyleSheet(u"QLabel {\n"
"	color: #C4AAD9;\n"
"}")

        self.questionInfoFrameLayout.addWidget(self.questionNumberLabel, 0, Qt.AlignLeft)

        self.jumpToQuestionBtn = QPushButton(self.questionInfoFrame)
        self.jumpToQuestionBtn.setObjectName(u"jumpToQuestionBtn")
        self.jumpToQuestionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.jumpToQuestionBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: none;\n"
"	padding: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/icons/link-question-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jumpToQuestionBtn.setIcon(icon)
        self.jumpToQuestionBtn.setIconSize(QSize(30, 30))

        self.questionInfoFrameLayout.addWidget(self.jumpToQuestionBtn, 0, Qt.AlignRight)


        self.mainFrameLayout.addWidget(self.questionInfoFrame, 0, Qt.AlignBottom)

        self.questionFrame = QFrame(self.mainFrame)
        self.questionFrame.setObjectName(u"questionFrame")
        self.questionFrame.setStyleSheet(u"border: none;")
        self.questionFrame.setFrameShape(QFrame.StyledPanel)
        self.questionFrame.setFrameShadow(QFrame.Raised)
        self.questionFrameLayout = QVBoxLayout(self.questionFrame)
        self.questionFrameLayout.setSpacing(30)
        self.questionFrameLayout.setObjectName(u"questionFrameLayout")
        self.questionFrameLayout.setContentsMargins(25, 0, 25, 0)
        self.questionLabel = QLabel(self.questionFrame)
        self.questionLabel.setObjectName(u"questionLabel")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(16)
        self.questionLabel.setFont(font1)
        self.questionLabel.setStyleSheet(u"")
        self.questionLabel.setWordWrap(True)

        self.questionFrameLayout.addWidget(self.questionLabel)

        self.answerFrame = QFrame(self.questionFrame)
        self.answerFrame.setObjectName(u"answerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerFrame.sizePolicy().hasHeightForWidth())
        self.answerFrame.setSizePolicy(sizePolicy)
        self.answerFrame.setFrameShape(QFrame.StyledPanel)
        self.answerFrame.setFrameShadow(QFrame.Raised)
        self.answerFrameLayout = QVBoxLayout(self.answerFrame)
        self.answerFrameLayout.setSpacing(20)
        self.answerFrameLayout.setObjectName(u"answerFrameLayout")
        self.answerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.userAnswersRegion = QFrame(self.answerFrame)
        self.userAnswersRegion.setObjectName(u"userAnswersRegion")
        self.userAnswersRegion.setStyleSheet(u"QFrame {\n"
"	background-color: #5D476F;\n"
"	padding: 15px;\n"
"}")
        self.userAnswersRegion.setFrameShape(QFrame.StyledPanel)
        self.userAnswersRegion.setFrameShadow(QFrame.Raised)
        self.userAnswersRegionLayout = QVBoxLayout(self.userAnswersRegion)
        self.userAnswersRegionLayout.setSpacing(15)
        self.userAnswersRegionLayout.setObjectName(u"userAnswersRegionLayout")
        self.userAnswersRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.userAnswerTitleLabel = QLabel(self.userAnswersRegion)
        self.userAnswerTitleLabel.setObjectName(u"userAnswerTitleLabel")
        font2 = QFont()
        font2.setFamilies([u"Iosevka NF Medium"])
        font2.setPointSize(14)
        self.userAnswerTitleLabel.setFont(font2)
        self.userAnswerTitleLabel.setStyleSheet(u"QLabel {\n"
"	color: #B098C2;\n"
"	padding: 0px;\n"
"}")

        self.userAnswersRegionLayout.addWidget(self.userAnswerTitleLabel, 0, Qt.AlignLeft)

        self.userAnswersFrame = QFrame(self.userAnswersRegion)
        self.userAnswersFrame.setObjectName(u"userAnswersFrame")
        sizePolicy.setHeightForWidth(self.userAnswersFrame.sizePolicy().hasHeightForWidth())
        self.userAnswersFrame.setSizePolicy(sizePolicy)
        self.userAnswersFrame.setFrameShape(QFrame.StyledPanel)
        self.userAnswersFrame.setFrameShadow(QFrame.Raised)
        self.userAnswersFrameLayout = QVBoxLayout(self.userAnswersFrame)
        self.userAnswersFrameLayout.setSpacing(15)
        self.userAnswersFrameLayout.setObjectName(u"userAnswersFrameLayout")
        self.userAnswersFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.userAnswerLabel = QLabel(self.userAnswersFrame)
        self.userAnswerLabel.setObjectName(u"userAnswerLabel")
        font3 = QFont()
        font3.setFamilies([u"Iosevka NF Medium"])
        font3.setPointSize(12)
        self.userAnswerLabel.setFont(font3)
        self.userAnswerLabel.setStyleSheet(u"QLabel {\n"
"	color: #D6C5E3;\n"
"	padding: 0px;\n"
"}")

        self.userAnswersFrameLayout.addWidget(self.userAnswerLabel)


        self.userAnswersRegionLayout.addWidget(self.userAnswersFrame)


        self.answerFrameLayout.addWidget(self.userAnswersRegion)

        self.correctAnswersRegion = QFrame(self.answerFrame)
        self.correctAnswersRegion.setObjectName(u"correctAnswersRegion")
        self.correctAnswersRegion.setStyleSheet(u"QFrame {\n"
"	background-color: #5B3579;\n"
"	padding: 15px;\n"
"}")
        self.correctAnswersRegion.setFrameShape(QFrame.StyledPanel)
        self.correctAnswersRegion.setFrameShadow(QFrame.Raised)
        self.correctAnswersRegionLayout = QVBoxLayout(self.correctAnswersRegion)
        self.correctAnswersRegionLayout.setSpacing(15)
        self.correctAnswersRegionLayout.setObjectName(u"correctAnswersRegionLayout")
        self.correctAnswersRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.correctAnswerTitleLabel = QLabel(self.correctAnswersRegion)
        self.correctAnswerTitleLabel.setObjectName(u"correctAnswerTitleLabel")
        self.correctAnswerTitleLabel.setFont(font2)
        self.correctAnswerTitleLabel.setStyleSheet(u"QLabel {\n"
"	color: #B690D3;\n"
"	padding: 0px;\n"
"}")

        self.correctAnswersRegionLayout.addWidget(self.correctAnswerTitleLabel, 0, Qt.AlignLeft|Qt.AlignTop)

        self.correctAnswersFrame = QFrame(self.correctAnswersRegion)
        self.correctAnswersFrame.setObjectName(u"correctAnswersFrame")
        sizePolicy.setHeightForWidth(self.correctAnswersFrame.sizePolicy().hasHeightForWidth())
        self.correctAnswersFrame.setSizePolicy(sizePolicy)
        self.correctAnswersFrame.setFrameShape(QFrame.StyledPanel)
        self.correctAnswersFrame.setFrameShadow(QFrame.Raised)
        self.correctAnswersFrameLayout = QVBoxLayout(self.correctAnswersFrame)
        self.correctAnswersFrameLayout.setSpacing(15)
        self.correctAnswersFrameLayout.setObjectName(u"correctAnswersFrameLayout")
        self.correctAnswersFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.correctAnswerLabel = QLabel(self.correctAnswersFrame)
        self.correctAnswerLabel.setObjectName(u"correctAnswerLabel")
        self.correctAnswerLabel.setFont(font3)
        self.correctAnswerLabel.setStyleSheet(u"QLabel {\n"
"	color: #DFC3F4;\n"
"	padding: 0px;\n"
"}")

        self.correctAnswersFrameLayout.addWidget(self.correctAnswerLabel)


        self.correctAnswersRegionLayout.addWidget(self.correctAnswersFrame)


        self.answerFrameLayout.addWidget(self.correctAnswersRegion)


        self.questionFrameLayout.addWidget(self.answerFrame)


        self.mainFrameLayout.addWidget(self.questionFrame, 0, Qt.AlignTop)


        self.overviewQuestionLayout.addWidget(self.mainFrame)


        self.retranslateUi(QuestionOverview)

        QMetaObject.connectSlotsByName(QuestionOverview)
    # setupUi

    def retranslateUi(self, QuestionOverview):
        QuestionOverview.setWindowTitle(QCoreApplication.translate("QuestionOverview", u"Form", None))
        self.questionNumberLabel.setText(QCoreApplication.translate("QuestionOverview", u"1", None))
        self.jumpToQuestionBtn.setText("")
        self.questionLabel.setText(QCoreApplication.translate("QuestionOverview", u"Question", None))
        self.userAnswerTitleLabel.setText(QCoreApplication.translate("QuestionOverview", u"Your Answer", None))
        self.userAnswerLabel.setText(QCoreApplication.translate("QuestionOverview", u"- answer", None))
        self.correctAnswerTitleLabel.setText(QCoreApplication.translate("QuestionOverview", u"Correct Answer", None))
        self.correctAnswerLabel.setText(QCoreApplication.translate("QuestionOverview", u"- answer", None))
    # retranslateUi

