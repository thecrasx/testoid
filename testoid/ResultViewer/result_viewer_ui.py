# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result-viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ResultViewer(object):
    def setupUi(self, ResultViewer):
        if not ResultViewer.objectName():
            ResultViewer.setObjectName(u"ResultViewer")
        ResultViewer.resize(423, 308)
        ResultViewer.setMinimumSize(QSize(399, 0))
        self.resultViewerLayout = QVBoxLayout(ResultViewer)
        self.resultViewerLayout.setSpacing(0)
        self.resultViewerLayout.setObjectName(u"resultViewerLayout")
        self.resultViewerLayout.setContentsMargins(0, 0, 0, 0)
        self.resultFrame = QFrame(ResultViewer)
        self.resultFrame.setObjectName(u"resultFrame")
        self.resultFrame.setMinimumSize(QSize(0, 200))
        self.resultFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #36AF49;\n"
"	border: none;\n"
"	border-top-left-radius: 50%;\n"
"	border-top-right-radius: 50%;\n"
"}")
        self.resultFrame.setFrameShape(QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QFrame.Raised)
        self.resultFrameLayout = QVBoxLayout(self.resultFrame)
        self.resultFrameLayout.setSpacing(0)
        self.resultFrameLayout.setObjectName(u"resultFrameLayout")
        self.resultFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.resultStatusLabel = QLabel(self.resultFrame)
        self.resultStatusLabel.setObjectName(u"resultStatusLabel")
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(26)
        font.setBold(True)
        self.resultStatusLabel.setFont(font)

        self.resultFrameLayout.addWidget(self.resultStatusLabel, 0, Qt.AlignHCenter)

        self.resultDetailsFrame = QFrame(self.resultFrame)
        self.resultDetailsFrame.setObjectName(u"resultDetailsFrame")
        self.resultDetailsFrame.setStyleSheet(u"QFrame {\n"
"	border-radius: 0px;\n"
"	background-color: #D9D9D9;\n"
"}")
        self.resultDetailsFrame.setFrameShape(QFrame.StyledPanel)
        self.resultDetailsFrame.setFrameShadow(QFrame.Raised)
        self.resultDetailsFrameLayout = QHBoxLayout(self.resultDetailsFrame)
        self.resultDetailsFrameLayout.setSpacing(0)
        self.resultDetailsFrameLayout.setObjectName(u"resultDetailsFrameLayout")
        self.resultDetailsFrameLayout.setContentsMargins(10, 0, 10, 0)
        self.resultPointsLabel = QLabel(self.resultDetailsFrame)
        self.resultPointsLabel.setObjectName(u"resultPointsLabel")
        self.resultPointsLabel.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"}")

        self.resultDetailsFrameLayout.addWidget(self.resultPointsLabel, 0, Qt.AlignLeft)

        self.resultMistakeLabel = QLabel(self.resultDetailsFrame)
        self.resultMistakeLabel.setObjectName(u"resultMistakeLabel")
        self.resultMistakeLabel.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"}")

        self.resultDetailsFrameLayout.addWidget(self.resultMistakeLabel, 0, Qt.AlignRight)


        self.resultFrameLayout.addWidget(self.resultDetailsFrame)


        self.resultViewerLayout.addWidget(self.resultFrame, 0, Qt.AlignTop)

        self.incorrectQuestionsSA = QScrollArea(ResultViewer)
        self.incorrectQuestionsSA.setObjectName(u"incorrectQuestionsSA")
        self.incorrectQuestionsSA.setStyleSheet(u"QScrollArea{\n"
"	border: none;\n"
"}")
        self.incorrectQuestionsSA.setWidgetResizable(True)
        self.incorrectQuestionsSAWC = QWidget()
        self.incorrectQuestionsSAWC.setObjectName(u"incorrectQuestionsSAWC")
        self.incorrectQuestionsSAWC.setGeometry(QRect(0, 0, 423, 108))
        self.incorrectQuestionsSAWC.setStyleSheet(u"")
        self.incorrectQuestionsSAWCLayout = QVBoxLayout(self.incorrectQuestionsSAWC)
        self.incorrectQuestionsSAWCLayout.setSpacing(0)
        self.incorrectQuestionsSAWCLayout.setObjectName(u"incorrectQuestionsSAWCLayout")
        self.incorrectQuestionsSAWCLayout.setContentsMargins(0, 0, 0, 0)
        self.incorrectQuestionsFrame = QFrame(self.incorrectQuestionsSAWC)
        self.incorrectQuestionsFrame.setObjectName(u"incorrectQuestionsFrame")
        self.incorrectQuestionsFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.incorrectQuestionsFrame.setFrameShape(QFrame.StyledPanel)
        self.incorrectQuestionsFrame.setFrameShadow(QFrame.Raised)
        self.incorrectQuestionsFrameLayout = QVBoxLayout(self.incorrectQuestionsFrame)
        self.incorrectQuestionsFrameLayout.setSpacing(0)
        self.incorrectQuestionsFrameLayout.setObjectName(u"incorrectQuestionsFrameLayout")
        self.incorrectQuestionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.questionFrame = QFrame(self.incorrectQuestionsFrame)
        self.questionFrame.setObjectName(u"questionFrame")
        self.questionFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #994D4D;\n"
"}")
        self.questionFrame.setFrameShape(QFrame.StyledPanel)
        self.questionFrame.setFrameShadow(QFrame.Raised)
        self.questionFrameLayout = QVBoxLayout(self.questionFrame)
        self.questionFrameLayout.setObjectName(u"questionFrameLayout")
        self.label = QLabel(self.questionFrame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.questionFrameLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.answersFrame = QFrame(self.questionFrame)
        self.answersFrame.setObjectName(u"answersFrame")
        self.answersFrame.setFrameShape(QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QFrame.Raised)
        self.answersFrameLayout = QVBoxLayout(self.answersFrame)
        self.answersFrameLayout.setObjectName(u"answersFrameLayout")
        self.answer = QCheckBox(self.answersFrame)
        self.answer.setObjectName(u"answer")
        self.answer.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	background-color: #C10707;\n"
"	border: 7px solid transparent;\n"
"	border-radius: 10%;\n"
"}")
        self.answer.setCheckable(False)

        self.answersFrameLayout.addWidget(self.answer)


        self.questionFrameLayout.addWidget(self.answersFrame)


        self.incorrectQuestionsFrameLayout.addWidget(self.questionFrame)


        self.incorrectQuestionsSAWCLayout.addWidget(self.incorrectQuestionsFrame, 0, Qt.AlignTop)

        self.incorrectQuestionsSA.setWidget(self.incorrectQuestionsSAWC)

        self.resultViewerLayout.addWidget(self.incorrectQuestionsSA)


        self.retranslateUi(ResultViewer)

        QMetaObject.connectSlotsByName(ResultViewer)





    # setupUi
    def retranslateUi(self, ResultViewer):
        ResultViewer.setWindowTitle(QCoreApplication.translate("ResultViewer", u"Form", None))
        self.resultStatusLabel.setText(QCoreApplication.translate("ResultViewer", u"Pass", None))
        self.resultPointsLabel.setText(QCoreApplication.translate("ResultViewer", u"850 / 1000", None))
        self.resultMistakeLabel.setText(QCoreApplication.translate("ResultViewer", u"3 Mistakes", None))
        self.label.setText(QCoreApplication.translate("ResultViewer", u"TextLabel", None))
        self.answer.setText(QCoreApplication.translate("ResultViewer", u"Text", None))
    # retranslateUi

