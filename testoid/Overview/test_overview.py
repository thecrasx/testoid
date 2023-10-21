from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.Overview.overview_ui import Ui_Overview
from testoid.TestMaker.test_data import TestData
from testoid.Overview.QuestionOverview.question_overview import QuestionOverview
from testoid.Tools.stylesheet import load as ssLoad





class TestOverview(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_Overview()
        self.ui.setupUi(self)
        self.ui.closeBtn.setStyleSheet(ssLoad("close-answer-button"))


        self.__questions: list[QuestionOverview] = []
        self.__questionCount: int = 0

        self.show()


    def setupTest(self, test: TestData):
        index = 0
        for question in test.questions:
            if index < self.__questionCount:
                questionOverview = self.__questions[index]
                questionOverview.removeUserAnswers()
            else:
                questionOverview = QuestionOverview()
                questionOverview.hideCorrectAnswers()

            questionOverview.setNumber(index + 1)
            questionOverview.setText(question.question)

            if index >= self.__questionCount:
                self.__addQuestion(questionOverview)
            index += 1


        if index < self.__questionCount:
            for questionOverview in self.__questions[index:]:
                questionOverview.close()
                self.__questionCount -= 1

            self.__questions = self.__questions[:index]



    def questionCount(self) -> int:
        return self.__questionCount


    def __addQuestion(self, question: QuestionOverview):
        question.setParent(self.ui.questionsFrame)
        self.ui.questionsFrameLayout.addWidget(question)
        self.__questions.append(question)
        self.__questionCount += 1
        

    def getQuestionOverview(self, question_number: int) -> QuestionOverview | None:
        if question_number < 1 or question_number > self.__questionCount:
            return None
        
        return self.__questions[question_number - 1]











if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = TestOverview()

    sys.exit(app.exec())