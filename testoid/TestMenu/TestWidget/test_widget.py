# PYSIDE
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6.QtGui
from PySide6.QtWidgets import *

# TESTOID
from testoid.TestMenu.TestWidget.test_widget_ui import Ui_TestWidget
from testoid.Tools.stylesheet import load as ssLoad
from testoid.TestMaker.test_data import TestData




class _TestWidgetSignals(QObject):
    clicked = Signal(object)





class _TestWidgetStyleSheet:
    # Favorite Button StyleSheet
    FAV_NOT_SELECTED: str = ssLoad("test-menu-widget-fav-button")
    FAV_SELECTED: str = ssLoad("test-menu-widget-fav-filled-button")

    # Stats Button StyleSheet
    STATS: str = ssLoad("test-menu-widget-stats-button")





class TestWidget(QWidget):
    def __init__(self, test: TestData, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_TestWidget()
        self.ui.setupUi(self)

        # SIGNALS
        self.__testWidgetSignals = _TestWidgetSignals(self)
        self.clicked: Signal = self.__testWidgetSignals.clicked


        self.__isSelected: bool = False
        self.__favorite: bool = False

        self.__test: TestData = test
        self.setName(test.name)



        # Buttons
        self.ui.favoriteBtn.clicked.connect(lambda: self.setFavorite(not self.__favorite))

        self.__hideButtons()
        self.show()


    def getTest(self) -> TestData:
        return self.__test


    def setName(self, name: str) -> None:
        self.ui.testLabel.setText(name)



    def __showButtons(self):
        if not self.__favorite:
            self.ui.favoriteBtn.setStyleSheet(_TestWidgetStyleSheet.FAV_NOT_SELECTED)

        self.ui.statsBtn.setStyleSheet(_TestWidgetStyleSheet.STATS)





    def __hideButtons(self):
        if not self.__favorite:
            self.ui.favoriteBtn.setStyleSheet("border: none; background: transparent;")

        self.ui.statsBtn.setStyleSheet("border: none; background: transparent;")





    def isSelected(self) -> bool:
        return self.__isSelected





    def setFavorite(self, favorite: bool) -> None:
        if self.__favorite == favorite:
            return

        self.__favorite = favorite

        if self.__favorite:
            self.ui.favoriteBtn.setStyleSheet(_TestWidgetStyleSheet.FAV_SELECTED)
        else:
            self.ui.favoriteBtn.setStyleSheet(_TestWidgetStyleSheet.FAV_NOT_SELECTED)





    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)





    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        
        if event.button() is Qt.MouseButton.LeftButton:
            self.__isSelected = True
            self.clicked.emit(self.__test)



        # elif event.button() is Qt.MouseButton.RightButton:
        #     pass





    def enterEvent(self, event: QEnterEvent) -> None:
        super().enterEvent(event)

        self.__showButtons()





    def leaveEvent(self, event: QEvent) -> None:
        super().leaveEvent(event)

        self.__hideButtons()











if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = TestWidget()

    sys.exit(app.exec())