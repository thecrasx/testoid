from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.TestMaker.TestConfigurator.test_configurator_ui import Ui_TestConfigurator
from testoid.TestMaker.test_data import TestData



class TCButtonStyleSheet:
    NORMAL = (
        "QLineEdit {\n"
        "   background-color: #715a83;\n"
        "   border-radius: 6%;\n"
        "   padding: 4px 2px 3px 5px;\n"
        "   color:  #F5E6E6;\n"
        "}\n"
    )

    WARNING = (
        "QLineEdit {\n"
        "   background-color: #715a83;\n"
        "   border: 2px solid #F8485D;\n"
        "   border-radius: 6%;\n"
        "   padding: 2px 0px 1px 3px;\n"
        "   color:  #F5E6E6;\n"
        "}\n"
    )





class TestConfigurator(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


        self.ui = Ui_TestConfigurator()
        self.ui.setupUi(self)


        # Hide continue button
        self.ui.continueBtnFrame.hide()





        self.show()


    

    def clear(self):
        self.ui.nameInput.clear()
        self.ui.authorInput.clear()
        self.ui.categoryInput.clear()
        self.ui.pointToPassInput.clear()
        self.ui.validAnswersInput.clear()
        self.ui.maxMistakesInput.clear()

        self.ui.nameInput.setStyleSheet(TCButtonStyleSheet.NORMAL)





    def getConfiguration(self) -> TestData:
        test = TestData()
        test.name = self.ui.nameInput.text()
        test.author = self.ui.authorInput.text()
        test.category = self.ui.categoryInput.text()
        test.pointsToPass = self.ui.pointToPassInput.value()
        test.validAnswers = self.ui.validAnswersInput.value()
        test.maxMistakes = self.ui.maxMistakesInput.value()

        return test





    def validateTestConfiguratorInputs(self) -> bool:
        if self.ui.nameInput.text().replace(' ', '') == '':
            self.ui.nameInput.setStyleSheet(
                TCButtonStyleSheet.WARNING
            )

            return False
         
        return True





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = TestConfigurator()

    sys.exit(app.exec())
        