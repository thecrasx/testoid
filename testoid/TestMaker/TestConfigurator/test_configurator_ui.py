# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-configurator.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_TestConfigurator(object):
    def setupUi(self, TestConfigurator):
        if not TestConfigurator.objectName():
            TestConfigurator.setObjectName(u"TestConfigurator")
        TestConfigurator.resize(754, 620)
        TestConfigurator.setStyleSheet(u"")
        self.testMakerLayout = QVBoxLayout(TestConfigurator)
        self.testMakerLayout.setSpacing(0)
        self.testMakerLayout.setObjectName(u"testMakerLayout")
        self.testMakerLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(TestConfigurator)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 754, 620))
        self.SAWCLayout = QVBoxLayout(self.SAWC)
        self.SAWCLayout.setSpacing(0)
        self.SAWCLayout.setObjectName(u"SAWCLayout")
        self.SAWCLayout.setContentsMargins(0, 0, 0, 0)
        self.testMakerFrame = QFrame(self.SAWC)
        self.testMakerFrame.setObjectName(u"testMakerFrame")
        self.testMakerFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	background-color: #463851;\n"
"}")
        self.testMakerFrame.setFrameShape(QFrame.StyledPanel)
        self.testMakerFrame.setFrameShadow(QFrame.Raised)
        self.testMakerFrameLayout = QVBoxLayout(self.testMakerFrame)
        self.testMakerFrameLayout.setSpacing(51)
        self.testMakerFrameLayout.setObjectName(u"testMakerFrameLayout")
        self.testMakerFrameLayout.setContentsMargins(10, 10, 10, 10)
        self.descriptionRegion = QFrame(self.testMakerFrame)
        self.descriptionRegion.setObjectName(u"descriptionRegion")
        self.descriptionRegion.setFrameShape(QFrame.StyledPanel)
        self.descriptionRegion.setFrameShadow(QFrame.Raised)
        self.descriptionRegionLayout = QVBoxLayout(self.descriptionRegion)
        self.descriptionRegionLayout.setSpacing(10)
        self.descriptionRegionLayout.setObjectName(u"descriptionRegionLayout")
        self.descriptionRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.descriptionLabel = QLabel(self.descriptionRegion)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"	color: #EDDEF9;\n"
"}")

        self.descriptionRegionLayout.addWidget(self.descriptionLabel, 0, Qt.AlignLeft)

        self.descriptionFrame = QFrame(self.descriptionRegion)
        self.descriptionFrame.setObjectName(u"descriptionFrame")
        self.descriptionFrame.setFrameShape(QFrame.StyledPanel)
        self.descriptionFrame.setFrameShadow(QFrame.Raised)
        self.descriptionFrameLayout = QVBoxLayout(self.descriptionFrame)
        self.descriptionFrameLayout.setSpacing(8)
        self.descriptionFrameLayout.setObjectName(u"descriptionFrameLayout")
        self.descriptionFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.nameFrame = QFrame(self.descriptionFrame)
        self.nameFrame.setObjectName(u"nameFrame")
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.nameFrame.setFont(font1)
        self.nameFrame.setFrameShape(QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Raised)
        self.nameFrameLayout = QHBoxLayout(self.nameFrame)
        self.nameFrameLayout.setSpacing(150)
        self.nameFrameLayout.setObjectName(u"nameFrameLayout")
        self.nameFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.nameFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font2 = QFont()
        font2.setFamilies([u"Iosevka NF Medium"])
        font2.setPointSize(14)
        font2.setItalic(False)
        self.nameLabel.setFont(font2)

        self.nameFrameLayout.addWidget(self.nameLabel, 0, Qt.AlignLeft)

        self.nameInput = QLineEdit(self.nameFrame)
        self.nameInput.setObjectName(u"nameInput")
        font3 = QFont()
        font3.setFamilies([u"Iosevka NF Medium"])
        font3.setPointSize(12)
        font3.setItalic(False)
        self.nameInput.setFont(font3)
        self.nameInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: #715A83;\n"
"	border-radius: 5%;\n"
"	padding: 3px 2px 3px 5px;\n"
"	color:  #F4E6E6;\n"
"}")

        self.nameFrameLayout.addWidget(self.nameInput, 0, Qt.AlignRight)


        self.descriptionFrameLayout.addWidget(self.nameFrame)

        self.authorFrame = QFrame(self.descriptionFrame)
        self.authorFrame.setObjectName(u"authorFrame")
        self.authorFrame.setFrameShape(QFrame.StyledPanel)
        self.authorFrame.setFrameShadow(QFrame.Raised)
        self.authorFrameLayout = QHBoxLayout(self.authorFrame)
        self.authorFrameLayout.setSpacing(0)
        self.authorFrameLayout.setObjectName(u"authorFrameLayout")
        self.authorFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.authorLabel = QLabel(self.authorFrame)
        self.authorLabel.setObjectName(u"authorLabel")
        font4 = QFont()
        font4.setFamilies([u"Iosevka NF Medium"])
        font4.setPointSize(14)
        self.authorLabel.setFont(font4)

        self.authorFrameLayout.addWidget(self.authorLabel, 0, Qt.AlignLeft)

        self.authorInput = QLineEdit(self.authorFrame)
        self.authorInput.setObjectName(u"authorInput")
        font5 = QFont()
        font5.setFamilies([u"Iosevka NF Medium"])
        font5.setPointSize(12)
        self.authorInput.setFont(font5)
        self.authorInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: #715A83;\n"
"	border-radius: 5%;\n"
"	padding: 3px 2px 3px 5px;\n"
"	color:  #F4E6E6;\n"
"}")

        self.authorFrameLayout.addWidget(self.authorInput, 0, Qt.AlignRight)


        self.descriptionFrameLayout.addWidget(self.authorFrame)


        self.descriptionRegionLayout.addWidget(self.descriptionFrame, 0, Qt.AlignLeft)


        self.testMakerFrameLayout.addWidget(self.descriptionRegion)

        self.categoryNTagsRegion = QFrame(self.testMakerFrame)
        self.categoryNTagsRegion.setObjectName(u"categoryNTagsRegion")
        self.categoryNTagsRegion.setFrameShape(QFrame.StyledPanel)
        self.categoryNTagsRegion.setFrameShadow(QFrame.Raised)
        self.categoryNTagsRegionLayout = QVBoxLayout(self.categoryNTagsRegion)
        self.categoryNTagsRegionLayout.setSpacing(10)
        self.categoryNTagsRegionLayout.setObjectName(u"categoryNTagsRegionLayout")
        self.categoryNTagsRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryNTagsLabel = QLabel(self.categoryNTagsRegion)
        self.categoryNTagsLabel.setObjectName(u"categoryNTagsLabel")
        font6 = QFont()
        font6.setFamilies([u"Iosevka NF Heavy"])
        font6.setPointSize(20)
        font6.setBold(True)
        self.categoryNTagsLabel.setFont(font6)

        self.categoryNTagsRegionLayout.addWidget(self.categoryNTagsLabel, 0, Qt.AlignLeft)

        self.categoryNTagsFrame = QFrame(self.categoryNTagsRegion)
        self.categoryNTagsFrame.setObjectName(u"categoryNTagsFrame")
        self.categoryNTagsFrame.setFrameShape(QFrame.StyledPanel)
        self.categoryNTagsFrame.setFrameShadow(QFrame.Raised)
        self.categoryNTagsFrameLayout = QHBoxLayout(self.categoryNTagsFrame)
        self.categoryNTagsFrameLayout.setSpacing(8)
        self.categoryNTagsFrameLayout.setObjectName(u"categoryNTagsFrameLayout")
        self.categoryNTagsFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.categoryFrame = QFrame(self.categoryNTagsFrame)
        self.categoryFrame.setObjectName(u"categoryFrame")
        self.categoryFrame.setMinimumSize(QSize(100, 0))
        self.categoryFrame.setFrameShape(QFrame.StyledPanel)
        self.categoryFrame.setFrameShadow(QFrame.Raised)
        self.categoryFrameLayout = QHBoxLayout(self.categoryFrame)
        self.categoryFrameLayout.setSpacing(111)
        self.categoryFrameLayout.setObjectName(u"categoryFrameLayout")
        self.categoryFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryLabel = QLabel(self.categoryFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")
        font7 = QFont()
        font7.setFamilies([u"Iosevka NF Medium"])
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setItalic(False)
        self.categoryLabel.setFont(font7)

        self.categoryFrameLayout.addWidget(self.categoryLabel, 0, Qt.AlignLeft)

        self.categoryInput = QLineEdit(self.categoryFrame)
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setFont(font5)
        self.categoryInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: #715A83;\n"
"	border-radius: 5%;\n"
"	padding: 3px 2px 3px 5px;\n"
"	color:  #F4E6E6;\n"
"}")

        self.categoryFrameLayout.addWidget(self.categoryInput, 0, Qt.AlignRight)


        self.categoryNTagsFrameLayout.addWidget(self.categoryFrame)


        self.categoryNTagsRegionLayout.addWidget(self.categoryNTagsFrame, 0, Qt.AlignLeft)


        self.testMakerFrameLayout.addWidget(self.categoryNTagsRegion)

        self.requirementsRegion = QFrame(self.testMakerFrame)
        self.requirementsRegion.setObjectName(u"requirementsRegion")
        self.requirementsRegion.setFrameShape(QFrame.StyledPanel)
        self.requirementsRegion.setFrameShadow(QFrame.Raised)
        self.requirementsRegionLayout = QVBoxLayout(self.requirementsRegion)
        self.requirementsRegionLayout.setSpacing(10)
        self.requirementsRegionLayout.setObjectName(u"requirementsRegionLayout")
        self.requirementsRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.requirementsLabelFrame = QFrame(self.requirementsRegion)
        self.requirementsLabelFrame.setObjectName(u"requirementsLabelFrame")
        self.requirementsLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.requirementsLabelFrame.setFrameShadow(QFrame.Raised)
        self.requirementsLabelFrameLayout = QHBoxLayout(self.requirementsLabelFrame)
        self.requirementsLabelFrameLayout.setSpacing(8)
        self.requirementsLabelFrameLayout.setObjectName(u"requirementsLabelFrameLayout")
        self.requirementsLabelFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.requirementsLabel = QLabel(self.requirementsLabelFrame)
        self.requirementsLabel.setObjectName(u"requirementsLabel")
        self.requirementsLabel.setFont(font)

        self.requirementsLabelFrameLayout.addWidget(self.requirementsLabel)

        self.requrementsOptionalLabel = QLabel(self.requirementsLabelFrame)
        self.requrementsOptionalLabel.setObjectName(u"requrementsOptionalLabel")
        font8 = QFont()
        font8.setFamilies([u"Iosevka NF Heavy"])
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setItalic(True)
        self.requrementsOptionalLabel.setFont(font8)
        self.requrementsOptionalLabel.setStyleSheet(u"QLabel {\n"
"	margin-top: 1%;\n"
"	color: #675B71;\n"
"}")

        self.requirementsLabelFrameLayout.addWidget(self.requrementsOptionalLabel)


        self.requirementsRegionLayout.addWidget(self.requirementsLabelFrame, 0, Qt.AlignLeft)

        self.requirementsFrame = QFrame(self.requirementsRegion)
        self.requirementsFrame.setObjectName(u"requirementsFrame")
        self.requirementsFrame.setFrameShape(QFrame.StyledPanel)
        self.requirementsFrame.setFrameShadow(QFrame.Raised)
        self.requirementsFrameLayout = QVBoxLayout(self.requirementsFrame)
        self.requirementsFrameLayout.setSpacing(8)
        self.requirementsFrameLayout.setObjectName(u"requirementsFrameLayout")
        self.requirementsFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.timeToFinishFrame = QFrame(self.requirementsFrame)
        self.timeToFinishFrame.setObjectName(u"timeToFinishFrame")
        self.timeToFinishFrame.setFrameShape(QFrame.StyledPanel)
        self.timeToFinishFrame.setFrameShadow(QFrame.Raised)
        self.timeToFinishFrameLayout = QHBoxLayout(self.timeToFinishFrame)
        self.timeToFinishFrameLayout.setSpacing(45)
        self.timeToFinishFrameLayout.setObjectName(u"timeToFinishFrameLayout")
        self.timeToFinishFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.timeToFinishLabel = QLabel(self.timeToFinishFrame)
        self.timeToFinishLabel.setObjectName(u"timeToFinishLabel")
        self.timeToFinishLabel.setFont(font7)

        self.timeToFinishFrameLayout.addWidget(self.timeToFinishLabel, 0, Qt.AlignLeft)

        self.timerFrame = QFrame(self.timeToFinishFrame)
        self.timerFrame.setObjectName(u"timerFrame")
        self.timerFrame.setFrameShape(QFrame.StyledPanel)
        self.timerFrame.setFrameShadow(QFrame.Raised)
        self.timerFrameLayout = QHBoxLayout(self.timerFrame)
        self.timerFrameLayout.setSpacing(10)
        self.timerFrameLayout.setObjectName(u"timerFrameLayout")
        self.timerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.hourTimerFrame = QFrame(self.timerFrame)
        self.hourTimerFrame.setObjectName(u"hourTimerFrame")
        self.hourTimerFrame.setFrameShape(QFrame.StyledPanel)
        self.hourTimerFrame.setFrameShadow(QFrame.Raised)
        self.hourTimerFrameLayout = QHBoxLayout(self.hourTimerFrame)
        self.hourTimerFrameLayout.setSpacing(3)
        self.hourTimerFrameLayout.setObjectName(u"hourTimerFrameLayout")
        self.hourTimerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.timerHours = QSpinBox(self.hourTimerFrame)
        self.timerHours.setObjectName(u"timerHours")
        self.timerHours.setFont(font5)
        self.timerHours.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.timerHours.setMaximum(72)

        self.hourTimerFrameLayout.addWidget(self.timerHours)

        self.hourLabel = QLabel(self.hourTimerFrame)
        self.hourLabel.setObjectName(u"hourLabel")
        self.hourLabel.setFont(font5)

        self.hourTimerFrameLayout.addWidget(self.hourLabel)


        self.timerFrameLayout.addWidget(self.hourTimerFrame)

        self.minuteTimerFrame = QFrame(self.timerFrame)
        self.minuteTimerFrame.setObjectName(u"minuteTimerFrame")
        self.minuteTimerFrame.setFrameShape(QFrame.StyledPanel)
        self.minuteTimerFrame.setFrameShadow(QFrame.Raised)
        self.minuteTimerFrameLayout = QHBoxLayout(self.minuteTimerFrame)
        self.minuteTimerFrameLayout.setSpacing(3)
        self.minuteTimerFrameLayout.setObjectName(u"minuteTimerFrameLayout")
        self.minuteTimerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.minuteTimer = QSpinBox(self.minuteTimerFrame)
        self.minuteTimer.setObjectName(u"minuteTimer")
        self.minuteTimer.setFont(font5)
        self.minuteTimer.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.minuteTimer.setMaximum(60)

        self.minuteTimerFrameLayout.addWidget(self.minuteTimer)

        self.minuteLabel = QLabel(self.minuteTimerFrame)
        self.minuteLabel.setObjectName(u"minuteLabel")
        self.minuteLabel.setFont(font5)

        self.minuteTimerFrameLayout.addWidget(self.minuteLabel)


        self.timerFrameLayout.addWidget(self.minuteTimerFrame)

        self.secondTimerFrame = QFrame(self.timerFrame)
        self.secondTimerFrame.setObjectName(u"secondTimerFrame")
        self.secondTimerFrame.setFrameShape(QFrame.StyledPanel)
        self.secondTimerFrame.setFrameShadow(QFrame.Raised)
        self.secondTimerFrameLayout = QHBoxLayout(self.secondTimerFrame)
        self.secondTimerFrameLayout.setSpacing(3)
        self.secondTimerFrameLayout.setObjectName(u"secondTimerFrameLayout")
        self.secondTimerFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.secondTimer = QSpinBox(self.secondTimerFrame)
        self.secondTimer.setObjectName(u"secondTimer")
        self.secondTimer.setFont(font5)
        self.secondTimer.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.secondTimer.setMaximum(60)

        self.secondTimerFrameLayout.addWidget(self.secondTimer)

        self.secondLabel = QLabel(self.secondTimerFrame)
        self.secondLabel.setObjectName(u"secondLabel")
        self.secondLabel.setFont(font5)

        self.secondTimerFrameLayout.addWidget(self.secondLabel)


        self.timerFrameLayout.addWidget(self.secondTimerFrame)


        self.timeToFinishFrameLayout.addWidget(self.timerFrame, 0, Qt.AlignRight)


        self.requirementsFrameLayout.addWidget(self.timeToFinishFrame)

        self.pointsToPassFrame = QFrame(self.requirementsFrame)
        self.pointsToPassFrame.setObjectName(u"pointsToPassFrame")
        self.pointsToPassFrame.setFrameShape(QFrame.StyledPanel)
        self.pointsToPassFrame.setFrameShadow(QFrame.Raised)
        self.pointsToPassFrameLayout = QHBoxLayout(self.pointsToPassFrame)
        self.pointsToPassFrameLayout.setSpacing(0)
        self.pointsToPassFrameLayout.setObjectName(u"pointsToPassFrameLayout")
        self.pointsToPassFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.pointsToPassLabel = QLabel(self.pointsToPassFrame)
        self.pointsToPassLabel.setObjectName(u"pointsToPassLabel")
        self.pointsToPassLabel.setFont(font7)

        self.pointsToPassFrameLayout.addWidget(self.pointsToPassLabel, 0, Qt.AlignLeft)

        self.pointToPassInput = QSpinBox(self.pointsToPassFrame)
        self.pointToPassInput.setObjectName(u"pointToPassInput")
        self.pointToPassInput.setFont(font5)
        self.pointToPassInput.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.pointToPassInput.setMaximum(10000)

        self.pointsToPassFrameLayout.addWidget(self.pointToPassInput, 0, Qt.AlignRight)


        self.requirementsFrameLayout.addWidget(self.pointsToPassFrame)

        self.validAnswersFrame = QFrame(self.requirementsFrame)
        self.validAnswersFrame.setObjectName(u"validAnswersFrame")
        self.validAnswersFrame.setFrameShape(QFrame.StyledPanel)
        self.validAnswersFrame.setFrameShadow(QFrame.Raised)
        self.validAnswersFrameLayout = QHBoxLayout(self.validAnswersFrame)
        self.validAnswersFrameLayout.setSpacing(0)
        self.validAnswersFrameLayout.setObjectName(u"validAnswersFrameLayout")
        self.validAnswersFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.validAnswersLabel = QLabel(self.validAnswersFrame)
        self.validAnswersLabel.setObjectName(u"validAnswersLabel")
        self.validAnswersLabel.setFont(font7)

        self.validAnswersFrameLayout.addWidget(self.validAnswersLabel, 0, Qt.AlignLeft)

        self.validAnswersInput = QSpinBox(self.validAnswersFrame)
        self.validAnswersInput.setObjectName(u"validAnswersInput")
        self.validAnswersInput.setFont(font5)
        self.validAnswersInput.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.validAnswersInput.setMaximum(10000)

        self.validAnswersFrameLayout.addWidget(self.validAnswersInput, 0, Qt.AlignRight)


        self.requirementsFrameLayout.addWidget(self.validAnswersFrame)

        self.maxMistakesFrame = QFrame(self.requirementsFrame)
        self.maxMistakesFrame.setObjectName(u"maxMistakesFrame")
        self.maxMistakesFrame.setFrameShape(QFrame.StyledPanel)
        self.maxMistakesFrame.setFrameShadow(QFrame.Raised)
        self.maxMistakesFrameLayout = QHBoxLayout(self.maxMistakesFrame)
        self.maxMistakesFrameLayout.setSpacing(0)
        self.maxMistakesFrameLayout.setObjectName(u"maxMistakesFrameLayout")
        self.maxMistakesFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.maxMistakesLabel = QLabel(self.maxMistakesFrame)
        self.maxMistakesLabel.setObjectName(u"maxMistakesLabel")
        self.maxMistakesLabel.setFont(font7)

        self.maxMistakesFrameLayout.addWidget(self.maxMistakesLabel, 0, Qt.AlignLeft)

        self.maxMistakesInput = QSpinBox(self.maxMistakesFrame)
        self.maxMistakesInput.setObjectName(u"maxMistakesInput")
        self.maxMistakesInput.setFont(font5)
        self.maxMistakesInput.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}")
        self.maxMistakesInput.setMaximum(10000)

        self.maxMistakesFrameLayout.addWidget(self.maxMistakesInput, 0, Qt.AlignRight)


        self.requirementsFrameLayout.addWidget(self.maxMistakesFrame)


        self.requirementsRegionLayout.addWidget(self.requirementsFrame, 0, Qt.AlignLeft)


        self.testMakerFrameLayout.addWidget(self.requirementsRegion)

        self.continueBtnFrame = QFrame(self.testMakerFrame)
        self.continueBtnFrame.setObjectName(u"continueBtnFrame")
        self.continueBtnFrame.setMinimumSize(QSize(0, 0))
        self.continueBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.continueBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.continueBtnFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.continueBtn = QPushButton(self.continueBtnFrame)
        self.continueBtn.setObjectName(u"continueBtn")
        self.continueBtn.setMinimumSize(QSize(380, 0))
        self.continueBtn.setFont(font5)
        self.continueBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #6941BF;\n"
"	color: #D6C1E5;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 7% 30% 7% 30%;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #845BDC;\n"
"}")

        self.verticalLayout.addWidget(self.continueBtn)


        self.testMakerFrameLayout.addWidget(self.continueBtnFrame, 0, Qt.AlignLeft)


        self.SAWCLayout.addWidget(self.testMakerFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.SAWC)

        self.testMakerLayout.addWidget(self.scrollArea)


        self.retranslateUi(TestConfigurator)

        QMetaObject.connectSlotsByName(TestConfigurator)





    # setupUi
    def retranslateUi(self, TestConfigurator):
        TestConfigurator.setWindowTitle(QCoreApplication.translate("TestConfigurator", u"Form", None))
        self.descriptionLabel.setText(QCoreApplication.translate("TestConfigurator", u"Description", None))
        self.nameLabel.setText(QCoreApplication.translate("TestConfigurator", u"Name", None))
        self.authorLabel.setText(QCoreApplication.translate("TestConfigurator", u"Author", None))
        self.categoryNTagsLabel.setText(QCoreApplication.translate("TestConfigurator", u"Category / Tags", None))
        self.categoryLabel.setText(QCoreApplication.translate("TestConfigurator", u"Category", None))
        self.requirementsLabel.setText(QCoreApplication.translate("TestConfigurator", u"Requirements", None))
        self.requrementsOptionalLabel.setText(QCoreApplication.translate("TestConfigurator", u"Optional ", None))
        self.timeToFinishLabel.setText(QCoreApplication.translate("TestConfigurator", u"Time To Finish", None))
        self.hourLabel.setText(QCoreApplication.translate("TestConfigurator", u"H", None))
        self.minuteLabel.setText(QCoreApplication.translate("TestConfigurator", u"M", None))
        self.secondTimer.setSuffix("")
        self.secondLabel.setText(QCoreApplication.translate("TestConfigurator", u"S", None))
        self.pointsToPassLabel.setText(QCoreApplication.translate("TestConfigurator", u"Points To Pass", None))
        self.validAnswersLabel.setText(QCoreApplication.translate("TestConfigurator", u"Valid Answers", None))
        self.validAnswersInput.setSuffix("")
        self.validAnswersInput.setPrefix("")
        self.maxMistakesLabel.setText(QCoreApplication.translate("TestConfigurator", u"Max Mistakes", None))
        self.maxMistakesInput.setSuffix("")
        self.maxMistakesInput.setPrefix("")
        self.continueBtn.setText(QCoreApplication.translate("TestConfigurator", u"Continue", None))
    # retranslateUi

