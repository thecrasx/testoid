# PYSIDE
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6.QtGui
from PySide6.QtWidgets import *


from testoid.TestMenu.test_menu_ui import Ui_TestMenu
from testoid.TestMaker.test_data import TestData
from testoid.TestMenu.menu_layout import MenuLayout
from testoid.TestMenu.TestWidget.test_widget import TestWidget
from testoid.Database.database import Database, db_aws_path as db_path



class _CustomSignal(QObject):
    testClicked = Signal(object)


class TestMenu(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_TestMenu()
        self.ui.setupUi(self)

        self.__customSignal = _CustomSignal()
        self.testClicked = self.__customSignal.testClicked

        self.btns: list[TestWidget] = []

        self.__loadTests()
        self.show()



    def __testClicked(self, test: TestData) -> None:
        self.testClicked.emit(test)




    def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)


    def __loadTests(self):
        db = Database(db_path)
        tests = db.getTests()

        for test in tests:
            self.addTest(test)






    def addTest(self, test: TestData):
        b_len = len(self.btns)

        w = TestWidget(test, self.ui.mainFrame)
        w.clicked.connect(self.__testClicked)
        self.btns.append(w)



        # self.ui.addTestBtn.hide()
        self.ui.mainFrameLayout.removeWidget(self.ui.addTestBtn)

        self.ui.mainFrameLayout.addWidget(w, b_len / 3, b_len % 3)
        self.ui.mainFrameLayout.addWidget(self.ui.addTestBtn, (b_len + 1) / 3, (b_len + 1) % 3)





    def setFavorite(self):
        pass

















if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = TestMenu()

    sys.exit(app.exec())