# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question-maker.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_QuestionMaker(object):
    def setupUi(self, QuestionMaker):
        if not QuestionMaker.objectName():
            QuestionMaker.setObjectName(u"QuestionMaker")
        QuestionMaker.resize(1020, 726)
        self.horizontalLayout = QHBoxLayout(QuestionMaker)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.questionListMenuFrame = QFrame(QuestionMaker)
        self.questionListMenuFrame.setObjectName(u"questionListMenuFrame")
        self.questionListMenuFrame.setMinimumSize(QSize(0, 0))
        self.questionListMenuFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #3C2A49;\n"
"	border: none;\n"
"}")
        self.questionListMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.questionListMenuFrame.setFrameShadow(QFrame.Raised)
        self.questionListMenuFrameLayout = QVBoxLayout(self.questionListMenuFrame)
        self.questionListMenuFrameLayout.setSpacing(0)
        self.questionListMenuFrameLayout.setObjectName(u"questionListMenuFrameLayout")
        self.questionListMenuFrameLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.questionListMenuFrame, 0, Qt.AlignLeft)

        self.mainFrame = QFrame(QuestionMaker)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)
        self.mainFrameLayout.setSpacing(0)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.mainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.SAWC = QWidget()
        self.SAWC.setObjectName(u"SAWC")
        self.SAWC.setGeometry(QRect(0, 0, 1016, 722))
        self.SAWCLayout = QVBoxLayout(self.SAWC)
        self.SAWCLayout.setSpacing(0)
        self.SAWCLayout.setObjectName(u"SAWCLayout")
        self.SAWCLayout.setContentsMargins(0, 0, 0, 0)
        self.questionMakerFrame = QFrame(self.SAWC)
        self.questionMakerFrame.setObjectName(u"questionMakerFrame")
        self.questionMakerFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	background-color: #463851;\n"
"}")
        self.questionMakerFrame.setFrameShape(QFrame.StyledPanel)
        self.questionMakerFrame.setFrameShadow(QFrame.Raised)
        self.questionMakerFrameLayout = QVBoxLayout(self.questionMakerFrame)
        self.questionMakerFrameLayout.setSpacing(51)
        self.questionMakerFrameLayout.setObjectName(u"questionMakerFrameLayout")
        self.questionMakerFrameLayout.setContentsMargins(30, 30, 30, 30)
        self.questionFrame = QFrame(self.questionMakerFrame)
        self.questionFrame.setObjectName(u"questionFrame")
        self.questionFrame.setStyleSheet(u"")
        self.questionFrame.setFrameShape(QFrame.StyledPanel)
        self.questionFrame.setFrameShadow(QFrame.Raised)
        self.questionFrameLayout = QVBoxLayout(self.questionFrame)
        self.questionFrameLayout.setSpacing(10)
        self.questionFrameLayout.setObjectName(u"questionFrameLayout")
        self.questionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.questionLabel = QLabel(self.questionFrame)
        self.questionLabel.setObjectName(u"questionLabel")
        font = QFont()
        font.setFamilies([u"Iosevka NF Heavy"])
        font.setPointSize(20)
        font.setBold(True)
        self.questionLabel.setFont(font)
        self.questionLabel.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"	margin-left: 1%;\n"
"	color: #EDDEF9;\n"
"}")

        self.questionFrameLayout.addWidget(self.questionLabel, 0, Qt.AlignLeft)

        self.questionInput = QPlainTextEdit(self.questionFrame)
        self.questionInput.setObjectName(u"questionInput")
        self.questionInput.setMinimumSize(QSize(554, 192))
        font1 = QFont()
        font1.setFamilies([u"Iosevka NF Medium"])
        font1.setPointSize(12)
        self.questionInput.setFont(font1)
        self.questionInput.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: #4E4C6C;\n"
"	border: none;\n"
"	border-radius: 15%;\n"
"	padding: 7px 10px 7px 10px;\n"
"	color: #F1DADA;\n"
"}")

        self.questionFrameLayout.addWidget(self.questionInput)


        self.questionMakerFrameLayout.addWidget(self.questionFrame)

        self.answersRegion = QFrame(self.questionMakerFrame)
        self.answersRegion.setObjectName(u"answersRegion")
        self.answersRegion.setStyleSheet(u"")
        self.answersRegion.setFrameShape(QFrame.StyledPanel)
        self.answersRegion.setFrameShadow(QFrame.Raised)
        self.answersRegionLayout = QVBoxLayout(self.answersRegion)
        self.answersRegionLayout.setSpacing(15)
        self.answersRegionLayout.setObjectName(u"answersRegionLayout")
        self.answersRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.answersNTypeFrame = QFrame(self.answersRegion)
        self.answersNTypeFrame.setObjectName(u"answersNTypeFrame")
        self.answersNTypeFrame.setFrameShape(QFrame.StyledPanel)
        self.answersNTypeFrame.setFrameShadow(QFrame.Raised)
        self.answersNTypeFrameLayout = QVBoxLayout(self.answersNTypeFrame)
        self.answersNTypeFrameLayout.setSpacing(10)
        self.answersNTypeFrameLayout.setObjectName(u"answersNTypeFrameLayout")
        self.answersNTypeFrameLayout.setContentsMargins(0, 0, -1, 0)
        self.answerLabelNBtnFrame = QFrame(self.answersNTypeFrame)
        self.answerLabelNBtnFrame.setObjectName(u"answerLabelNBtnFrame")
        self.answerLabelNBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.answerLabelNBtnFrame.setFrameShadow(QFrame.Raised)
        self.answerLabelNBtnFrameLayout = QHBoxLayout(self.answerLabelNBtnFrame)
        self.answerLabelNBtnFrameLayout.setSpacing(16)
        self.answerLabelNBtnFrameLayout.setObjectName(u"answerLabelNBtnFrameLayout")
        self.answerLabelNBtnFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.answersLabel = QLabel(self.answerLabelNBtnFrame)
        self.answersLabel.setObjectName(u"answersLabel")
        self.answersLabel.setFont(font)
        self.answersLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.answerLabelNBtnFrameLayout.addWidget(self.answersLabel)

        self.addAnswerBtn = QPushButton(self.answerLabelNBtnFrame)
        self.addAnswerBtn.setObjectName(u"addAnswerBtn")
        self.addAnswerBtn.setMinimumSize(QSize(36, 36))
        self.addAnswerBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #644E76;\n"
"	border: none;\n"
"	border-radius: 18px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #6C557E;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: #604973;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../assets/icons/add-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addAnswerBtn.setIcon(icon)
        self.addAnswerBtn.setIconSize(QSize(32, 32))

        self.answerLabelNBtnFrameLayout.addWidget(self.addAnswerBtn)


        self.answersNTypeFrameLayout.addWidget(self.answerLabelNBtnFrame, 0, Qt.AlignLeft)

        self.answerTypeFrame = QFrame(self.answersNTypeFrame)
        self.answerTypeFrame.setObjectName(u"answerTypeFrame")
        self.answerTypeFrame.setFrameShape(QFrame.StyledPanel)
        self.answerTypeFrame.setFrameShadow(QFrame.Raised)
        self.answerTypeFrameLayout = QHBoxLayout(self.answerTypeFrame)
        self.answerTypeFrameLayout.setSpacing(150)
        self.answerTypeFrameLayout.setObjectName(u"answerTypeFrameLayout")
        self.answerTypeFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.answerTypeLabel = QLabel(self.answerTypeFrame)
        self.answerTypeLabel.setObjectName(u"answerTypeLabel")
        font2 = QFont()
        font2.setFamilies([u"Iosevka NF Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.answerTypeLabel.setFont(font2)
        self.answerTypeLabel.setStyleSheet(u"")

        self.answerTypeFrameLayout.addWidget(self.answerTypeLabel)

        self.answerTypeOptionFrame = QFrame(self.answerTypeFrame)
        self.answerTypeOptionFrame.setObjectName(u"answerTypeOptionFrame")
        self.answerTypeOptionFrame.setFrameShape(QFrame.StyledPanel)
        self.answerTypeOptionFrame.setFrameShadow(QFrame.Raised)
        self.answerTypeOptionFrameLayout = QHBoxLayout(self.answerTypeOptionFrame)
        self.answerTypeOptionFrameLayout.setSpacing(10)
        self.answerTypeOptionFrameLayout.setObjectName(u"answerTypeOptionFrameLayout")
        self.answerTypeOptionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.answerTypeOptionLeftBtn = QPushButton(self.answerTypeOptionFrame)
        self.answerTypeOptionLeftBtn.setObjectName(u"answerTypeOptionLeftBtn")
        self.answerTypeOptionLeftBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")

        self.answerTypeOptionFrameLayout.addWidget(self.answerTypeOptionLeftBtn, 0, Qt.AlignLeft)

        self.answerTypeOptionLabel = QLabel(self.answerTypeOptionFrame)
        self.answerTypeOptionLabel.setObjectName(u"answerTypeOptionLabel")
        font3 = QFont()
        font3.setFamilies([u"Hack Nerd Font"])
        font3.setPointSize(10)
        self.answerTypeOptionLabel.setFont(font3)

        self.answerTypeOptionFrameLayout.addWidget(self.answerTypeOptionLabel, 0, Qt.AlignHCenter)

        self.answerTypeOptionRightBtn = QPushButton(self.answerTypeOptionFrame)
        self.answerTypeOptionRightBtn.setObjectName(u"answerTypeOptionRightBtn")
        self.answerTypeOptionRightBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")

        self.answerTypeOptionFrameLayout.addWidget(self.answerTypeOptionRightBtn, 0, Qt.AlignRight)


        self.answerTypeFrameLayout.addWidget(self.answerTypeOptionFrame)


        self.answersNTypeFrameLayout.addWidget(self.answerTypeFrame, 0, Qt.AlignLeft)


        self.answersRegionLayout.addWidget(self.answersNTypeFrame)

        self.answersFrame = QFrame(self.answersRegion)
        self.answersFrame.setObjectName(u"answersFrame")
        self.answersFrame.setFrameShape(QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QFrame.Raised)
        self.answersFrameLayout = QVBoxLayout(self.answersFrame)
        self.answersFrameLayout.setSpacing(20)
        self.answersFrameLayout.setObjectName(u"answersFrameLayout")
        self.answersFrameLayout.setContentsMargins(36, 0, 0, 0)

        self.answersRegionLayout.addWidget(self.answersFrame)


        self.questionMakerFrameLayout.addWidget(self.answersRegion)

        self.optionsRegion = QFrame(self.questionMakerFrame)
        self.optionsRegion.setObjectName(u"optionsRegion")
        self.optionsRegion.setFrameShape(QFrame.StyledPanel)
        self.optionsRegion.setFrameShadow(QFrame.Raised)
        self.optionsRegionLayout = QVBoxLayout(self.optionsRegion)
        self.optionsRegionLayout.setSpacing(10)
        self.optionsRegionLayout.setObjectName(u"optionsRegionLayout")
        self.optionsRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsLabel = QLabel(self.optionsRegion)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setFont(font)
        self.optionsLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.optionsRegionLayout.addWidget(self.optionsLabel, 0, Qt.AlignLeft)

        self.optionsFrame = QFrame(self.optionsRegion)
        self.optionsFrame.setObjectName(u"optionsFrame")
        self.optionsFrame.setFrameShape(QFrame.StyledPanel)
        self.optionsFrame.setFrameShadow(QFrame.Raised)
        self.optionsFrameLayout = QVBoxLayout(self.optionsFrame)
        self.optionsFrameLayout.setSpacing(5)
        self.optionsFrameLayout.setObjectName(u"optionsFrameLayout")
        self.optionsFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.difficultyFrame = QFrame(self.optionsFrame)
        self.difficultyFrame.setObjectName(u"difficultyFrame")
        self.difficultyFrame.setFrameShape(QFrame.StyledPanel)
        self.difficultyFrame.setFrameShadow(QFrame.Raised)
        self.difficultyFrameLayout = QHBoxLayout(self.difficultyFrame)
        self.difficultyFrameLayout.setSpacing(150)
        self.difficultyFrameLayout.setObjectName(u"difficultyFrameLayout")
        self.difficultyFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.difficultyLabel = QLabel(self.difficultyFrame)
        self.difficultyLabel.setObjectName(u"difficultyLabel")
        font4 = QFont()
        font4.setFamilies([u"Iosevka NF Medium"])
        font4.setPointSize(12)
        font4.setItalic(False)
        self.difficultyLabel.setFont(font4)
        self.difficultyLabel.setStyleSheet(u"")

        self.difficultyFrameLayout.addWidget(self.difficultyLabel, 0, Qt.AlignLeft)

        self.difficultyOptionFrame = QFrame(self.difficultyFrame)
        self.difficultyOptionFrame.setObjectName(u"difficultyOptionFrame")
        self.difficultyOptionFrame.setFrameShape(QFrame.StyledPanel)
        self.difficultyOptionFrame.setFrameShadow(QFrame.Raised)
        self.difficultyOptionFrameLayout = QHBoxLayout(self.difficultyOptionFrame)
        self.difficultyOptionFrameLayout.setSpacing(10)
        self.difficultyOptionFrameLayout.setObjectName(u"difficultyOptionFrameLayout")
        self.difficultyOptionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.difficultyOptionLeftBtn = QPushButton(self.difficultyOptionFrame)
        self.difficultyOptionLeftBtn.setObjectName(u"difficultyOptionLeftBtn")
        self.difficultyOptionLeftBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")

        self.difficultyOptionFrameLayout.addWidget(self.difficultyOptionLeftBtn, 0, Qt.AlignLeft)

        self.difficultyOptionLabel = QLabel(self.difficultyOptionFrame)
        self.difficultyOptionLabel.setObjectName(u"difficultyOptionLabel")
        self.difficultyOptionLabel.setFont(font3)

        self.difficultyOptionFrameLayout.addWidget(self.difficultyOptionLabel, 0, Qt.AlignHCenter)

        self.difficultyOptionRightBtn = QPushButton(self.difficultyOptionFrame)
        self.difficultyOptionRightBtn.setObjectName(u"difficultyOptionRightBtn")
        self.difficultyOptionRightBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")

        self.difficultyOptionFrameLayout.addWidget(self.difficultyOptionRightBtn, 0, Qt.AlignRight)


        self.difficultyFrameLayout.addWidget(self.difficultyOptionFrame, 0, Qt.AlignRight)


        self.optionsFrameLayout.addWidget(self.difficultyFrame)

        self.pointsFrame = QFrame(self.optionsFrame)
        self.pointsFrame.setObjectName(u"pointsFrame")
        self.pointsFrame.setFrameShape(QFrame.StyledPanel)
        self.pointsFrame.setFrameShadow(QFrame.Raised)
        self.pointsFrameLayout = QHBoxLayout(self.pointsFrame)
        self.pointsFrameLayout.setSpacing(177)
        self.pointsFrameLayout.setObjectName(u"pointsFrameLayout")
        self.pointsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.pointsLabel = QLabel(self.pointsFrame)
        self.pointsLabel.setObjectName(u"pointsLabel")
        self.pointsLabel.setFont(font1)
        self.pointsLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.pointsFrameLayout.addWidget(self.pointsLabel, 0, Qt.AlignLeft)

        self.pointsInputBox = QSpinBox(self.pointsFrame)
        self.pointsInputBox.setObjectName(u"pointsInputBox")
        self.pointsInputBox.setMinimumSize(QSize(0, 0))
        self.pointsInputBox.setMaximumSize(QSize(1000, 32))
        self.pointsInputBox.setFont(font1)
        self.pointsInputBox.setStyleSheet(u"QSpinBox {\n"
"	background-color: #715A83;\n"
"	border-width: 2px 0px 2px 0px;\n"
"	border-style: solid;\n"
"	border-color: #715A83;\n"
"	border-radius : 4%;\n"
"	padding-left: 5%;\n"
"	color:  #F4E6E6;\n"
"}\n"
"\n"
"\n"
"")
        self.pointsInputBox.setWrapping(False)
        self.pointsInputBox.setFrame(True)
        self.pointsInputBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.pointsInputBox.setMaximum(10000)

        self.pointsFrameLayout.addWidget(self.pointsInputBox, 0, Qt.AlignRight)


        self.optionsFrameLayout.addWidget(self.pointsFrame, 0, Qt.AlignLeft)


        self.optionsRegionLayout.addWidget(self.optionsFrame, 0, Qt.AlignLeft)


        self.questionMakerFrameLayout.addWidget(self.optionsRegion)

        self.categoryNTagsRegion = QFrame(self.questionMakerFrame)
        self.categoryNTagsRegion.setObjectName(u"categoryNTagsRegion")
        self.categoryNTagsRegion.setFrameShape(QFrame.StyledPanel)
        self.categoryNTagsRegion.setFrameShadow(QFrame.Raised)
        self.categoryNTagsRegionLayout = QVBoxLayout(self.categoryNTagsRegion)
        self.categoryNTagsRegionLayout.setSpacing(10)
        self.categoryNTagsRegionLayout.setObjectName(u"categoryNTagsRegionLayout")
        self.categoryNTagsRegionLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryNTagsLabel = QLabel(self.categoryNTagsRegion)
        self.categoryNTagsLabel.setObjectName(u"categoryNTagsLabel")
        self.categoryNTagsLabel.setFont(font)
        self.categoryNTagsLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.categoryNTagsRegionLayout.addWidget(self.categoryNTagsLabel, 0, Qt.AlignLeft)

        self.categoryNTagsFrame = QFrame(self.categoryNTagsRegion)
        self.categoryNTagsFrame.setObjectName(u"categoryNTagsFrame")
        self.categoryNTagsFrame.setFrameShape(QFrame.StyledPanel)
        self.categoryNTagsFrame.setFrameShadow(QFrame.Raised)
        self.categoryNTagsFrameLayout = QVBoxLayout(self.categoryNTagsFrame)
        self.categoryNTagsFrameLayout.setSpacing(0)
        self.categoryNTagsFrameLayout.setObjectName(u"categoryNTagsFrameLayout")
        self.categoryNTagsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryFrame = QFrame(self.categoryNTagsFrame)
        self.categoryFrame.setObjectName(u"categoryFrame")
        self.categoryFrame.setFrameShape(QFrame.StyledPanel)
        self.categoryFrame.setFrameShadow(QFrame.Raised)
        self.categoryFrameLayout = QHBoxLayout(self.categoryFrame)
        self.categoryFrameLayout.setSpacing(150)
        self.categoryFrameLayout.setObjectName(u"categoryFrameLayout")
        self.categoryFrameLayout.setContentsMargins(15, 0, 0, 0)
        self.categoryLabel = QLabel(self.categoryFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")
        self.categoryLabel.setFont(font1)
        self.categoryLabel.setStyleSheet(u"QLabel {\n"
"	color: #EDDEF9;\n"
"}")

        self.categoryFrameLayout.addWidget(self.categoryLabel, 0, Qt.AlignLeft)

        self.categoryInput = QLineEdit(self.categoryFrame)
        self.categoryInput.setObjectName(u"categoryInput")
        font5 = QFont()
        font5.setFamilies([u"Iosevka NF Medium"])
        font5.setPointSize(12)
        font5.setKerning(True)
        self.categoryInput.setFont(font5)
        self.categoryInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: #715A83;\n"
"	border-radius: 5%;\n"
"	padding: 3px 2px 3px 5px;\n"
"	color:  #F4E6E6;\n"
"}")

        self.categoryFrameLayout.addWidget(self.categoryInput, 0, Qt.AlignRight)


        self.categoryNTagsFrameLayout.addWidget(self.categoryFrame, 0, Qt.AlignLeft)


        self.categoryNTagsRegionLayout.addWidget(self.categoryNTagsFrame, 0, Qt.AlignLeft)


        self.questionMakerFrameLayout.addWidget(self.categoryNTagsRegion)


        self.SAWCLayout.addWidget(self.questionMakerFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.SAWC)

        self.mainFrameLayout.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.mainFrame)


        self.retranslateUi(QuestionMaker)

        QMetaObject.connectSlotsByName(QuestionMaker)
    # setupUi

    def retranslateUi(self, QuestionMaker):
        QuestionMaker.setWindowTitle(QCoreApplication.translate("QuestionMaker", u"Form", None))
        self.questionLabel.setText(QCoreApplication.translate("QuestionMaker", u"Question", None))
        self.questionInput.setPlainText("")
        self.answersLabel.setText(QCoreApplication.translate("QuestionMaker", u"Answers", None))
        self.addAnswerBtn.setText("")
        self.answerTypeLabel.setText(QCoreApplication.translate("QuestionMaker", u"Type", None))
        self.answerTypeOptionLeftBtn.setText(QCoreApplication.translate("QuestionMaker", u"L", None))
        self.answerTypeOptionLabel.setText(QCoreApplication.translate("QuestionMaker", u"Multiple Response", None))
        self.answerTypeOptionRightBtn.setText(QCoreApplication.translate("QuestionMaker", u"R", None))
        self.optionsLabel.setText(QCoreApplication.translate("QuestionMaker", u"Options", None))
        self.difficultyLabel.setText(QCoreApplication.translate("QuestionMaker", u"Difficulty", None))
        self.difficultyOptionLeftBtn.setText(QCoreApplication.translate("QuestionMaker", u"L", None))
        self.difficultyOptionLabel.setText(QCoreApplication.translate("QuestionMaker", u"Medium", None))
        self.difficultyOptionRightBtn.setText(QCoreApplication.translate("QuestionMaker", u"R", None))
        self.pointsLabel.setText(QCoreApplication.translate("QuestionMaker", u"Points", None))
        self.categoryNTagsLabel.setText(QCoreApplication.translate("QuestionMaker", u"Category / Tags", None))
        self.categoryLabel.setText(QCoreApplication.translate("QuestionMaker", u"Category", None))
        self.categoryInput.setInputMask("")
        self.categoryInput.setPlaceholderText(QCoreApplication.translate("QuestionMaker", u"Optional", None))
    # retranslateUi

