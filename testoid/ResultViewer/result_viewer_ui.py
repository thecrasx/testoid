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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ResultViewer(object):
    def setupUi(self, ResultViewer):
        if not ResultViewer.objectName():
            ResultViewer.setObjectName(u"ResultViewer")
        ResultViewer.resize(764, 704)
        self.resultViewerLayout = QVBoxLayout(ResultViewer)
        self.resultViewerLayout.setSpacing(100)
        self.resultViewerLayout.setObjectName(u"resultViewerLayout")
        self.resultViewerLayout.setContentsMargins(0, 0, 0, 0)
        self.resultFrame = QFrame(ResultViewer)
        self.resultFrame.setObjectName(u"resultFrame")
        self.resultFrame.setStyleSheet(u"QFrame {\n"
"	border-top: 2px solid #BE9ADA;\n"
"	border-bottom: 2px solid #BE9ADA;\n"
"	padding-top: 20px;\n"
"	padding-bottom: 20px;\n"
"}")
        self.resultFrame.setFrameShape(QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QFrame.Raised)
        self.resultFrameLayout = QHBoxLayout(self.resultFrame)
        self.resultFrameLayout.setSpacing(0)
        self.resultFrameLayout.setObjectName(u"resultFrameLayout")
        self.resultFrameLayout.setContentsMargins(0, -1, 0, 0)
        self.resultLabel = QLabel(self.resultFrame)
        self.resultLabel.setObjectName(u"resultLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(48)
        font.setBold(True)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"}")

        self.resultFrameLayout.addWidget(self.resultLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.resultViewerLayout.addWidget(self.resultFrame)

        self.bottomFrame = QFrame(ResultViewer)
        self.bottomFrame.setObjectName(u"bottomFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.bottomFrameLayout = QVBoxLayout(self.bottomFrame)
        self.bottomFrameLayout.setSpacing(24)
        self.bottomFrameLayout.setObjectName(u"bottomFrameLayout")
        self.bottomFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.statsFrame = QFrame(self.bottomFrame)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsFrame.setMinimumSize(QSize(461, 295))
        self.statsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #715A83;\n"
"	padding: 10px;\n"
"	border-radius: 25px;\n"
"}")
        self.statsFrame.setFrameShape(QFrame.StyledPanel)
        self.statsFrame.setFrameShadow(QFrame.Raised)
        self.statsFrameLayout = QVBoxLayout(self.statsFrame)
        self.statsFrameLayout.setSpacing(4)
        self.statsFrameLayout.setObjectName(u"statsFrameLayout")
        self.statsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.accuracyFrame = QFrame(self.statsFrame)
        self.accuracyFrame.setObjectName(u"accuracyFrame")
        self.accuracyFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #8F75A3;\n"
"	padding: 0px 51px 0px 20px;\n"
"	border-radius: 0px;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;\n"
"}")
        self.accuracyFrame.setFrameShape(QFrame.StyledPanel)
        self.accuracyFrame.setFrameShadow(QFrame.Raised)
        self.accuracyFrameLayout = QHBoxLayout(self.accuracyFrame)
        self.accuracyFrameLayout.setSpacing(0)
        self.accuracyFrameLayout.setObjectName(u"accuracyFrameLayout")
        self.accuracyFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.accuracyLabel = QLabel(self.accuracyFrame)
        self.accuracyLabel.setObjectName(u"accuracyLabel")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.accuracyLabel.setFont(font1)
        self.accuracyLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.accuracyFrameLayout.addWidget(self.accuracyLabel)

        self.accuracyValueLabel = QLabel(self.accuracyFrame)
        self.accuracyValueLabel.setObjectName(u"accuracyValueLabel")
        font2 = QFont()
        font2.setFamilies([u"Iosevka NF Medium"])
        font2.setPointSize(14)
        self.accuracyValueLabel.setFont(font2)
        self.accuracyValueLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.accuracyFrameLayout.addWidget(self.accuracyValueLabel, 0, Qt.AlignRight)


        self.statsFrameLayout.addWidget(self.accuracyFrame)

        self.mistakesFrame = QFrame(self.statsFrame)
        self.mistakesFrame.setObjectName(u"mistakesFrame")
        self.mistakesFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #8F75A3;\n"
"	padding: 0px 10px 0px 20px;\n"
"	border-radius: 0px;\n"
"}")
        self.mistakesFrame.setFrameShape(QFrame.StyledPanel)
        self.mistakesFrame.setFrameShadow(QFrame.Raised)
        self.mistakesFrameLayout = QHBoxLayout(self.mistakesFrame)
        self.mistakesFrameLayout.setSpacing(0)
        self.mistakesFrameLayout.setObjectName(u"mistakesFrameLayout")
        self.mistakesFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mistakesLabel = QLabel(self.mistakesFrame)
        self.mistakesLabel.setObjectName(u"mistakesLabel")
        self.mistakesLabel.setFont(font2)
        self.mistakesLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.mistakesFrameLayout.addWidget(self.mistakesLabel, 0, Qt.AlignLeft)

        self.mistakesValueFrame = QFrame(self.mistakesFrame)
        self.mistakesValueFrame.setObjectName(u"mistakesValueFrame")
        self.mistakesValueFrame.setStyleSheet(u"QFrame {\n"
"	padding: 0px;\n"
"}")
        self.mistakesValueFrame.setFrameShape(QFrame.StyledPanel)
        self.mistakesValueFrame.setFrameShadow(QFrame.Raised)
        self.mistakesValueFrameLayout = QHBoxLayout(self.mistakesValueFrame)
        self.mistakesValueFrameLayout.setSpacing(5)
        self.mistakesValueFrameLayout.setObjectName(u"mistakesValueFrameLayout")
        self.mistakesValueFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mistakesValueLabel = QLabel(self.mistakesValueFrame)
        self.mistakesValueLabel.setObjectName(u"mistakesValueLabel")
        self.mistakesValueLabel.setFont(font2)

        self.mistakesValueFrameLayout.addWidget(self.mistakesValueLabel)

        self.showMistakesBtn = QPushButton(self.mistakesValueFrame)
        self.showMistakesBtn.setObjectName(u"showMistakesBtn")
        self.showMistakesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.showMistakesBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding: 0px;\n"
"	icon-size: 64px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/icons/notes-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showMistakesBtn.setIcon(icon)
        self.showMistakesBtn.setIconSize(QSize(32, 32))

        self.mistakesValueFrameLayout.addWidget(self.showMistakesBtn)


        self.mistakesFrameLayout.addWidget(self.mistakesValueFrame, 0, Qt.AlignRight)


        self.statsFrameLayout.addWidget(self.mistakesFrame)

        self.attemptsFrame = QFrame(self.statsFrame)
        self.attemptsFrame.setObjectName(u"attemptsFrame")
        self.attemptsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #8F75A3;\n"
"	padding: 0px 51px 0px 20px;\n"
"	border-radius: 0px;\n"
"}")
        self.attemptsFrame.setFrameShape(QFrame.StyledPanel)
        self.attemptsFrame.setFrameShadow(QFrame.Raised)
        self.attemptsFrameLayout = QHBoxLayout(self.attemptsFrame)
        self.attemptsFrameLayout.setSpacing(0)
        self.attemptsFrameLayout.setObjectName(u"attemptsFrameLayout")
        self.attemptsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.attemptsLabel = QLabel(self.attemptsFrame)
        self.attemptsLabel.setObjectName(u"attemptsLabel")
        self.attemptsLabel.setFont(font2)
        self.attemptsLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.attemptsFrameLayout.addWidget(self.attemptsLabel, 0, Qt.AlignLeft)

        self.attemptsValueLabel = QLabel(self.attemptsFrame)
        self.attemptsValueLabel.setObjectName(u"attemptsValueLabel")
        self.attemptsValueLabel.setFont(font2)
        self.attemptsValueLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.attemptsFrameLayout.addWidget(self.attemptsValueLabel, 0, Qt.AlignRight)


        self.statsFrameLayout.addWidget(self.attemptsFrame)

        self.successRateFrame = QFrame(self.statsFrame)
        self.successRateFrame.setObjectName(u"successRateFrame")
        self.successRateFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #8F75A3;\n"
"	padding: 0px 51px 0px 20px;\n"
"	border-radius: 0px;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.successRateFrame.setFrameShape(QFrame.StyledPanel)
        self.successRateFrame.setFrameShadow(QFrame.Raised)
        self.successRateFrameLayout = QHBoxLayout(self.successRateFrame)
        self.successRateFrameLayout.setSpacing(0)
        self.successRateFrameLayout.setObjectName(u"successRateFrameLayout")
        self.successRateFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.successRateLabel = QLabel(self.successRateFrame)
        self.successRateLabel.setObjectName(u"successRateLabel")
        self.successRateLabel.setFont(font2)
        self.successRateLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.successRateFrameLayout.addWidget(self.successRateLabel, 0, Qt.AlignLeft)

        self.successRateValueLabel = QLabel(self.successRateFrame)
        self.successRateValueLabel.setObjectName(u"successRateValueLabel")
        self.successRateValueLabel.setFont(font2)
        self.successRateValueLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")

        self.successRateFrameLayout.addWidget(self.successRateValueLabel, 0, Qt.AlignRight)


        self.statsFrameLayout.addWidget(self.successRateFrame)


        self.bottomFrameLayout.addWidget(self.statsFrame)

        self.continueBtn = QPushButton(self.bottomFrame)
        self.continueBtn.setObjectName(u"continueBtn")
        self.continueBtn.setFont(font2)
        self.continueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.continueBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #8F75A3;\n"
"	padding: 3px 30px 3px 30px;\n"
"	border: 5px solid #715A83;\n"
"	border-radius: 19px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #957BA8;\n"
"	border-color: #78618A;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: #896F9C;\n"
"	border-color: #6B557D;\n"
"}")

        self.bottomFrameLayout.addWidget(self.continueBtn, 0, Qt.AlignHCenter)


        self.resultViewerLayout.addWidget(self.bottomFrame)


        self.retranslateUi(ResultViewer)

        QMetaObject.connectSlotsByName(ResultViewer)
    # setupUi

    def retranslateUi(self, ResultViewer):
        ResultViewer.setWindowTitle(QCoreApplication.translate("ResultViewer", u"Form", None))
        self.resultLabel.setText(QCoreApplication.translate("ResultViewer", u"PASS", None))
        self.accuracyLabel.setText(QCoreApplication.translate("ResultViewer", u"Accuracy", None))
        self.accuracyValueLabel.setText(QCoreApplication.translate("ResultViewer", u"0", None))
        self.mistakesLabel.setText(QCoreApplication.translate("ResultViewer", u"Mistakes", None))
        self.mistakesValueLabel.setText(QCoreApplication.translate("ResultViewer", u"0", None))
        self.showMistakesBtn.setText("")
        self.attemptsLabel.setText(QCoreApplication.translate("ResultViewer", u"Attempts", None))
        self.attemptsValueLabel.setText(QCoreApplication.translate("ResultViewer", u"0", None))
        self.successRateLabel.setText(QCoreApplication.translate("ResultViewer", u"Success Rate", None))
        self.successRateValueLabel.setText(QCoreApplication.translate("ResultViewer", u"0", None))
        self.continueBtn.setText(QCoreApplication.translate("ResultViewer", u"Continue", None))
    # retranslateUi

