from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.QuestionMaker.Answer.answer_ui import Ui_Answer
from testoid.Tools.stylesheet import load as ssLoad



class _CustomSignals(QObject):
    selected = Signal(QWidget, bool)
    removed = Signal(QWidget)



class Answer(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_Answer()
        self.ui.setupUi(self)

        # SIGNALS
        self.__customSignal = _CustomSignals()
        self.selected = self.__customSignal.selected
        self.removed = self.__customSignal.removed


        self.ui.checkBtn.clicked.connect(self.__select)
        self.ui.removeBtn.clicked.connect(self.close)

        self.ui.removeBtn.setStyleSheet("border: none;")
        self.__removeBtnStyleSheet = ssLoad("close-answer-button")

        self.__selected = False

        self.show()





    def enterEvent(self, event: QEnterEvent) -> None:
        super().enterEvent(event)
        self.ui.removeBtn.setStyleSheet(self.__removeBtnStyleSheet)





    def leaveEvent(self, event: QEvent) -> None:
        super().leaveEvent(event)
        self.ui.removeBtn.setStyleSheet("border: none;")





    def close(self):
        self.removed.emit(self)
        super().close()





    def setText(self, text: str):
        self.ui.answerTextEdit.setPlainText(text)





    def getText(self) -> str:
        return self.ui.answerTextEdit.toPlainText()





    def clear(self) -> None:
        self.ui.answerTextEdit.clear()
        self.setSelected(False)





        # Clear Explanation
    def __select(self):
        if self.__selected:
            self.setSelected(False)
            self.selected.emit(self, False)
        
        else:
            self.setSelected(True)
            self.selected.emit(self, True)





    def isSelected(self):
        return self.__selected





    def setSelected(self, selected: bool):
        if selected:
            self.__selected = True

            self.ui.checkBtn.setStyleSheet(u"QPushButton {\n"
            "	border: none;\n"
            "	background-color: #C368EE;\n"
            "	border-top-right-radius: 20%;\n"
            "	border-bottom-right-radius: 20%\n"
            " }")


        else:
            self.__selected = False

            self.ui.checkBtn.setStyleSheet(u"QPushButton {\n"
            "	border: none;\n"
            "	background-color: #9B71BC;\n"
            "	border-top-right-radius: 20%;\n"
            "	border-bottom-right-radius: 20%\n"
            " }")


            


            


        





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Answer()

    sys.exit(app.exec())
