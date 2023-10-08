# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 672)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #463851;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBarFrame = QFrame(self.centralwidget)
        self.titleBarFrame.setObjectName(u"titleBarFrame")
        self.titleBarFrame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	background-color: #6F1CC1;\n"
"}")
        self.titleBarFrame.setFrameShape(QFrame.StyledPanel)
        self.titleBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBarFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.versionLabel = QLabel(self.titleBarFrame)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout.addWidget(self.versionLabel, 0, Qt.AlignLeft)

        self.titleLabel = QLabel(self.titleBarFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"FreeSans"])
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"QLabel {\n"
"	color: #D6C1E5;\n"
"}")

        self.horizontalLayout.addWidget(self.titleLabel, 0, Qt.AlignHCenter)

        self.titleButtonsFrame = QFrame(self.titleBarFrame)
        self.titleButtonsFrame.setObjectName(u"titleButtonsFrame")
        self.titleButtonsFrame.setMinimumSize(QSize(0, 0))
        self.titleButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.titleButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleButtonsFrame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, 7, 4)
        self.minimizeBtn = QPushButton(self.titleButtonsFrame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/round-minimize-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.minimizeBtn)

        self.toggleMaximizeBtn = QPushButton(self.titleButtonsFrame)
        self.toggleMaximizeBtn.setObjectName(u"toggleMaximizeBtn")
        self.toggleMaximizeBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/maximize-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleMaximizeBtn.setIcon(icon1)
        self.toggleMaximizeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.toggleMaximizeBtn)

        self.exitBtn = QPushButton(self.titleButtonsFrame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/round-close-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon2)
        self.exitBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.horizontalLayout.addWidget(self.titleButtonsFrame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.titleBarFrame, 0, Qt.AlignTop)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuPages = QStackedWidget(self.mainFrame)
        self.menuPages.setObjectName(u"menuPages")
        self.menuPages.setStyleSheet(u"background-color: #221B2B;")
        self.menuPage = QWidget()
        self.menuPage.setObjectName(u"menuPage")
        self.menuPageLayout = QVBoxLayout(self.menuPage)
        self.menuPageLayout.setSpacing(0)
        self.menuPageLayout.setObjectName(u"menuPageLayout")
        self.menuPageLayout.setContentsMargins(0, 0, 0, 0)
        self.menuFrame = QFrame(self.menuPage)
        self.menuFrame.setObjectName(u"menuFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy1)
        self.menuFrame.setMinimumSize(QSize(200, 0))
        self.menuFrame.setStyleSheet(u"QFrame {\n"
"	background: #221B2B;\n"
"	border: none;\n"
"}")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.menuButtonsFrame = QFrame(self.menuFrame)
        self.menuButtonsFrame.setObjectName(u"menuButtonsFrame")
        self.menuButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.menuButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menuButtonsFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(14, 18, 14, 0)
        self.testMenuBtn = QPushButton(self.menuButtonsFrame)
        self.testMenuBtn.setObjectName(u"testMenuBtn")
        sizePolicy1.setHeightForWidth(self.testMenuBtn.sizePolicy().hasHeightForWidth())
        self.testMenuBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(11)
        self.testMenuBtn.setFont(font1)
        self.testMenuBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.verticalLayout_2.addWidget(self.testMenuBtn)

        self.historyMenuBtn = QPushButton(self.menuButtonsFrame)
        self.historyMenuBtn.setObjectName(u"historyMenuBtn")
        sizePolicy1.setHeightForWidth(self.historyMenuBtn.sizePolicy().hasHeightForWidth())
        self.historyMenuBtn.setSizePolicy(sizePolicy1)
        self.historyMenuBtn.setFont(font1)
        self.historyMenuBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.verticalLayout_2.addWidget(self.historyMenuBtn)

        self.menuLine = QFrame(self.menuButtonsFrame)
        self.menuLine.setObjectName(u"menuLine")
        self.menuLine.setStyleSheet(u"Line {\n"
"	background-color: #33293F\n"
"}")
        self.menuLine.setLineWidth(1)
        self.menuLine.setFrameShape(QFrame.HLine)
        self.menuLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.menuLine)

        self.makeTestMenuBtn = QPushButton(self.menuButtonsFrame)
        self.makeTestMenuBtn.setObjectName(u"makeTestMenuBtn")
        sizePolicy1.setHeightForWidth(self.makeTestMenuBtn.sizePolicy().hasHeightForWidth())
        self.makeTestMenuBtn.setSizePolicy(sizePolicy1)
        self.makeTestMenuBtn.setFont(font1)
        self.makeTestMenuBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #463851;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 10px 0px 10px 0px\n"
"}")

        self.verticalLayout_2.addWidget(self.makeTestMenuBtn)


        self.verticalLayout_4.addWidget(self.menuButtonsFrame, 0, Qt.AlignTop)

        self.settingsMenuBtnFrame = QFrame(self.menuFrame)
        self.settingsMenuBtnFrame.setObjectName(u"settingsMenuBtnFrame")
        self.settingsMenuBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsMenuBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.settingsMenuBtnFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settingsMenuBtn = QPushButton(self.settingsMenuBtnFrame)
        self.settingsMenuBtn.setObjectName(u"settingsMenuBtn")
        sizePolicy1.setHeightForWidth(self.settingsMenuBtn.sizePolicy().hasHeightForWidth())
        self.settingsMenuBtn.setSizePolicy(sizePolicy1)
        self.settingsMenuBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border:  none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/settings-rounded-normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsMenuBtn.setIcon(icon3)
        self.settingsMenuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.settingsMenuBtn)


        self.verticalLayout_4.addWidget(self.settingsMenuBtnFrame, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.menuPageLayout.addWidget(self.menuFrame)

        self.menuPages.addWidget(self.menuPage)
        self.testMakerMenuPage = QWidget()
        self.testMakerMenuPage.setObjectName(u"testMakerMenuPage")
        self.testMakerMenuPageLayout = QVBoxLayout(self.testMakerMenuPage)
        self.testMakerMenuPageLayout.setSpacing(0)
        self.testMakerMenuPageLayout.setObjectName(u"testMakerMenuPageLayout")
        self.testMakerMenuPageLayout.setContentsMargins(0, 0, 0, 0)
        self.menuPages.addWidget(self.testMakerMenuPage)

        self.horizontalLayout_4.addWidget(self.menuPages, 0, Qt.AlignLeft)

        self.pages = QStackedWidget(self.mainFrame)
        self.pages.setObjectName(u"pages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy2)
        self.testMenuPage = QWidget()
        self.testMenuPage.setObjectName(u"testMenuPage")
        self.testMenuPageLayout = QVBoxLayout(self.testMenuPage)
        self.testMenuPageLayout.setSpacing(0)
        self.testMenuPageLayout.setObjectName(u"testMenuPageLayout")
        self.testMenuPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.testMenuPage)
        self.testMakerPage = QWidget()
        self.testMakerPage.setObjectName(u"testMakerPage")
        self.testMakerPageLayout = QVBoxLayout(self.testMakerPage)
        self.testMakerPageLayout.setSpacing(0)
        self.testMakerPageLayout.setObjectName(u"testMakerPageLayout")
        self.testMakerPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.testMakerPage)
        self.testConfiguratorPage = QWidget()
        self.testConfiguratorPage.setObjectName(u"testConfiguratorPage")
        self.testConfiguratorPageLayout = QVBoxLayout(self.testConfiguratorPage)
        self.testConfiguratorPageLayout.setSpacing(0)
        self.testConfiguratorPageLayout.setObjectName(u"testConfiguratorPageLayout")
        self.testConfiguratorPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.testConfiguratorPage)
        self.testViewerPage = QWidget()
        self.testViewerPage.setObjectName(u"testViewerPage")
        self.testViewerPageLayout = QVBoxLayout(self.testViewerPage)
        self.testViewerPageLayout.setSpacing(0)
        self.testViewerPageLayout.setObjectName(u"testViewerPageLayout")
        self.testViewerPageLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.testViewerPage)
        self.resultViewerPage = QWidget()
        self.resultViewerPage.setObjectName(u"resultViewerPage")
        self.resultViewerPageLayout = QVBoxLayout(self.resultViewerPage)
        self.resultViewerPageLayout.setSpacing(0)
        self.resultViewerPageLayout.setObjectName(u"resultViewerPageLayout")
        self.resultViewerPageLayout.setContentsMargins(90, 30, 90, 0)
        self.f123 = QFrame(self.resultViewerPage)
        self.f123.setObjectName(u"f123")
        self.f123.setStyleSheet(u"background: white;")
        self.f123.setFrameShape(QFrame.StyledPanel)
        self.f123.setFrameShadow(QFrame.Raised)

        self.resultViewerPageLayout.addWidget(self.f123)

        self.pages.addWidget(self.resultViewerPage)

        self.horizontalLayout_4.addWidget(self.pages)


        self.verticalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.versionLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"AWS", None))
        self.minimizeBtn.setText("")
        self.toggleMaximizeBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.exitBtn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.exitBtn.setText("")
        self.testMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.historyMenuBtn.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.makeTestMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Make Test", None))
        self.settingsMenuBtn.setText("")
    # retranslateUi

