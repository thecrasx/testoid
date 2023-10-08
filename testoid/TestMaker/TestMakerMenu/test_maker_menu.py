from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from testoid.TestMaker.TestMakerMenu.test_maker_menu_ui import Ui_TestMakerMenu

class TestMakerMenu(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


        self.ui = Ui_TestMakerMenu()
        self.ui.setupUi(self)



        self.show()









if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = TestMakerMenu()

    sys.exit(app.exec())
        