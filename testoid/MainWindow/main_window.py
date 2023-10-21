from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.MainWindow.main_window_ui import Ui_MainWindow
from testoid.TestMenu.test_menu import TestMenu
from testoid.ResultViewer.result_viewer import ResultViewer
from testoid.MainWindow.size_grip import SizeGrip
from testoid.Tools.stylesheet import load as ssLoad

from testoid.TestMaker.test_maker import TestMaker
from testoid.TestMaker.TestMakerMenu.test_maker_menu import TestMakerMenu
# from testoid.TestMaker.TestConfigurator.test_configurator import TestConfigurator
from testoid.TestViewer.test_viewer import TestViewer



class _Signals(QObject):
    resized = Signal()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1365, 800) 


        # Signals
        self.__signals = _Signals(self)
        self.resized = self.__signals.resized

        self.__setupUI()
        self.__framelessWindow(True)


        # Title Bar Events
        self.ui.titleBarFrame.mousePressEvent = self.__mousePressEvent
        self.ui.titleBarFrame.mouseMoveEvent = self.__moveWindowEvent

        # Buttons
        self.ui.toggleMaximizeBtn.clicked.connect(self.__toggleMaximize)
        self.ui.toggleMaximizeBtn.setStyleSheet(ssLoad("maximize-in-button"))

        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.minimizeBtn.setStyleSheet(ssLoad("minimize-button"))

        self.ui.exitBtn.clicked.connect(self.close)
        self.ui.settingsMenuBtn.setStyleSheet(ssLoad("settings-button"))
        self.ui.exitBtn.setStyleSheet(ssLoad("close-button"))
        

        # Size Grip
        self.sizeGrip = SizeGrip(self)
        self.sizeGrip.setGripWidth(10)

        self.show()
        





    def __setupUI(self):
        # Hide Menu
        self.ui.menuPages.hide()
        self.ui.menuPages.setCurrentWidget(self.ui.testMakerMenuPage)

        # Result Viewer
        self.resultViewer = ResultViewer(self.ui.resultViewerPage, self)
        self.ui.resultViewerPageLayout.addWidget(self.resultViewer)
        self.resultViewer.ui.continueBtn.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.testMenuPage)
        )

        # Test Menu
        self.testMenu = TestMenu(self.ui.testMenuPage)
        self.ui.testMenuPageLayout.addWidget(self.testMenu)

        # Test Maker
        self.testMaker = TestMaker(self.ui.testMakerPage)
        self.ui.testMakerPageLayout.addWidget(self.testMaker)

        self.testMaker.testCreated.connect(self.testMenu.addTest)

        # Test Viewer
        self.testViewer = TestViewer(self.ui.testViewerPage, self)
        self.ui.testViewerPageLayout.addWidget(self.testViewer)

        self.testViewer.ui.quitBtn.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.testMenuPage)
        )

        def startTest(test):
            self.testViewer.loadTest(test)
            self.ui.pages.setCurrentWidget(self.ui.testViewerPage)
        
        self.testMenu.testClicked.connect(startTest)

        def finishTest():
            data = self.testViewer.getResultViewerData()
            # self.resultViewer.reset()
            self.resultViewer.processTest(data[0], data[1])
            self.ui.pages.setCurrentWidget(self.ui.resultViewerPage)

        self.testViewer.ui.finishBtn.clicked.connect(finishTest)





        def _testMenuBtn():
            self.ui.pages.setCurrentWidget(self.ui.testMakerPage)
            self.testMaker.showTestConfigurator()
            self.ui.menuPages.show()

        self.testMenu.ui.addTestBtn.clicked.connect(
            _testMenuBtn
        )


        self.testMakerMenu = TestMakerMenu(self.ui.testMakerMenuPage)
        self.ui.testMakerMenuPageLayout.addWidget(self.testMakerMenu)

        self.testMakerMenu.ui.testConfiguratorBtn.clicked.connect(
            self.testMaker.showTestConfigurator
        )

        self.testMakerMenu.ui.questionMakerBtn.clicked.connect(
            self.testMaker.showQuestionMaker
        )

        self.testMakerMenu.ui.saveBtn.clicked.connect(
            self.testMaker.saveTest
        )



        def printQuestion():
            q = self.testMaker.questionMaker.questionListMenu.getQuestions()

            for i in q:
                print(i.question)

            print()

        self.testMakerMenu.ui.backBtn.clicked.connect(printQuestion)
        # self.ui.pages.setCurrentWidget(self.ui.resultViewerPage)





    def __framelessWindow(self, frameless: bool):
            if frameless:
                self.setWindowFlags(Qt.FramelessWindowHint)
                self.setAttribute(Qt.WA_TranslucentBackground)





    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.resized.emit()
        self.sizeGrip.updateGeometry()




    ########################################
    """         TITLE BAR EVENTS         """
    ########################################
    def __mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()




    def __moveWindowEvent(self, event):
        if self.isMaximized() == False:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()





    def __toggleMaximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.toggleMaximizeBtn.setStyleSheet(ssLoad("maximize-in-button"))
        
        else:
            self.showMaximized()
            self.ui.toggleMaximizeBtn.setStyleSheet(ssLoad("maximize-out-button"))






if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())