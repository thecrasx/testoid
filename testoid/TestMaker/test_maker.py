from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from testoid.TestMaker.test_maker_ui import Ui_TestMaker
from testoid.TestMaker.TestConfigurator.test_configurator import TestConfigurator, TCButtonStyleSheet
from testoid.QuestionMaker.question_maker import QuestionMaker
from testoid.TestMaker.test_data import TestData
from testoid.Database.database import Database, db_path


class _CustomSignal(QObject):
    testCreated = Signal(object)


class TestMaker(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_TestMaker()
        self.ui.setupUi(self)

        self.__setupUI()

        self.__customSignal = _CustomSignal()
        self.testCreated = self.__customSignal.testCreated

        # self.showTestConfigurator()
        self.showQuestionMaker()

        
        
        # self.saveTest()

        self.show()





    def __setupUI(self):
        self.testConfigurator = TestConfigurator(self.ui.testConfiguratorPage)
        self.ui.testConfiguratorPageLayout.addWidget(self.testConfigurator)

        self.questionMaker = QuestionMaker(self.ui.questionMakerPage)
        self.ui.questionMakerPageLayout.addWidget(self.questionMaker)





    def showTestConfigurator(self):
        self.ui.pages.setCurrentWidget(self.ui.testConfiguratorPage)


    def showQuestionMaker(self):
        self.ui.pages.setCurrentWidget(self.ui.questionMakerPage)





    def saveTest(self):
        test = self.testConfigurator.getConfiguration()

        if not self.testConfigurator.validateTestConfiguratorInputs():
            self.showTestConfigurator()
            return
        
        questions = self.questionMaker.getQuestions()

        if len(questions) == 0:
            # TODO: Set border to red on QuestionMaker button in TestMakerMenu
            return
        
        if not self.questionMaker.validateQuestions(questions):
            return

        for question in questions:
            test.questions.append(question)

        database = Database(db_path)
        database.addTest(test)
        database.close()

        self.testConfigurator.clear()
        self.questionMaker.clear()
        self.questionMaker.hideQuestionMaker()
        self.questionMaker.questionListMenu.clear()

        self.testCreated.emit(test)












if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = TestMaker()

    sys.exit(app.exec())
       
