from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from src.ResultViewer.ResultViewerQuestion.rv_question_ui import Ui_RVQuestion

class RVQuestion(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.ui = Ui_RVQuestion()
        self.ui.setupUi(self)



        self.show()







if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = RVQuestion(None)

    sys.exit(app.exec())