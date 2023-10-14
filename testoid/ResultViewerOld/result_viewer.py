from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.ResultViewer.result_viewer_ui import Ui_ResultViewer
from testoid.ResultViewer.ResultViewerQuestion.rv_question import RVQuestion
from testoid.TestMaker.test_data import TestData
# from testoid.QuestionMaker.question_data import QuestionData





class ResultViewer(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.ui = Ui_ResultViewer()
        self.ui.setupUi(self)


        self.questionCount = 0
        self.questionWidgets = {}

        self.ui.resultFrameLayout.setStretch(0, 3)
        self.ui.resultFrameLayout.setStretch(1, 1)
        self.ui.questionFrame.hide()
        self.show()





    def addQuestion(self, text: str, user_answer: str, correct_answer: str):
        self.questionCount += 1

        if self.questionWidgets.get(self.questionCount):
            questionWidget = self.questionWidgets[self.questionCount]
            questionWidget.show()

        else:
            questionWidget = RVQuestion(self.ui.incorrectQuestionsFrame)
            self.ui.incorrectQuestionsFrameLayout.addWidget(questionWidget)

            self.questionWidgets[self.questionCount] = questionWidget

        questionWidget.ui.questionLabel.setText(text)
        questionWidget.ui.wrongAnswerLabel.setText(user_answer)
        questionWidget.ui.correctAnswerLabel.setText(correct_answer)



    def reset(self):
        for qw in self.questionWidgets:
            self.questionWidgets[qw].hide()

        self.questionCount = 0



    def setTestPassed(self, is_passed: bool):
        if is_passed:
            self.ui.resultStatusLabel.setText("PASS")
        
        else:
            self.ui.resultStatusLabel.setText("FAIL")


    
    def processTest(self, test: TestData, test_viewer_selections: dict[int, list]):
        mistakes = 0
        for question in test.questions:
            valid_answer_indexes = []

            for x in question.answers:
                valid_answer_indexes.append(1 if x[1] else 0)

            selections = test_viewer_selections.get(question.ID) 
            selections_transform: list[int] = []
            
            for i in range(1, len(valid_answer_indexes) + 1):
                if selections:
                    if i in selections:
                        selections_transform.append(1)
                    else:
                        selections_transform.append(0)
                else:
                    selections_transform.append(0)

            if valid_answer_indexes == selections_transform:
                continue

            user_selection = -1
            for i in range(len(selections_transform)):
                if selections_transform[i] == 1:
                    user_selection = i
                    break

            index = 0
            user_answer: str = ""
            for answer, isCorrect in question.answers:
                if index == user_selection:
                    user_answer = answer

                if isCorrect:
                    self.addQuestion(question.question, user_answer, answer)
                    break

                index += 1

            mistakes += 1

        if mistakes > 0:
            self.ui.resultMistakeLabel.setText(f"{mistakes} Mistakes")
        else:
            self.ui.resultMistakeLabel.clear()






        




if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = ResultViewer(None)

    sys.exit(app.exec())