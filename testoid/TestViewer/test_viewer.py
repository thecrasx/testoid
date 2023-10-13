from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from testoid.TestViewer.test_viewer_ui import Ui_TestViewer
from testoid.TestMaker.test_data import TestData
from testoid.QuestionMaker.question_data import QuestionData
from testoid.TestViewer.QuestionBar.question_bar import QuestionBar
from testoid.TestViewer.tv_answer_label import TVAnswerLabel


class TestViewer(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_TestViewer()
        self.ui.setupUi(self)

        self.questionBar = QuestionBar(self.ui.questionBarFrame)
        self.ui.questionBarFrameLayout.addWidget(self.questionBar)
        self.questionBar.clicked.connect(self.__onQuestionBarClick)

        
        self.__answerCount: int = 0
        self.__answerWidgetCount = 0
        self.__answerWidgets = {}
        self.__lastSelectedAnswer = None



        self.__test: TestData = None
        self.__currentQuestionID: int = -1

        self.__selections: dict[int, list] = {}


        # Hide design testing label
        self.ui.label.hide()

        # Buttons
        self.ui.nextBtn.clicked.connect(self.nextQuestion)
        self.ui.prevBtn.clicked.connect(self.previousQuestion)
        self.ui.markBtn.clicked.connect(self.__markQuestionSwitch)

        self.show()




    
    def __setupQuestion(self, question: QuestionData):
        if question.ID == self.__currentQuestionID:
            return
        
        self.saveSelection()
        self.clearSelections()

        selection = self.__selections.get(question.ID)

        index = 1
        for answer, is_correct in question.answers:
            selected = False

            if selection is not None:
                if index in selection:
                    selected = True

            self.addAnswer(answer, selected)
            index += 1


        self.ui.answerTypeLabel.setText(f"Answer Type: {question.answerType}")
        self.ui.question.setPlainText(question.question)
        mark_text = "Unmark" if self.questionBar.isQuestionMarked() else "Mark"
        self.ui.markBtn.setText(mark_text)
        
        self.__currentQuestionID = question.ID

        




    def __onAnswerSelect(self, answer: TVAnswerLabel):
        if self.getCurrentQuestion().answerType == "Multiple Choice":
            
            if self.__lastSelectedAnswer and self.__lastSelectedAnswer is not answer:
                self.__lastSelectedAnswer.setSelected(False)
        
        self.__lastSelectedAnswer = answer





    def __onQuestionBarClick(self, button: int):
        question = self.getQuestion(button)
        self.__setupQuestion(question)





    def getQuestion(self, id_: int) -> QuestionData | None:
        if id_ < 1 and id_ > len(self.__test.questions):
            return None
        
        return self.__test.questions[id_ - 1]





    def getCurrentQuestion(self) -> QuestionData | None:
        if self.__currentQuestionID == -1:
            return None

        return self.__test.questions[self.__currentQuestionID - 1]
    
    



    def getPreviousQuestion(self) -> QuestionData | None:
        if self.__currentQuestionID - 2 < 0:
            return None
        
        return self.__test.questions[self.__currentQuestionID - 2]





    def getNextQuestion(self) -> QuestionData | None:
        if self.__currentQuestionID + 1 > len(self.__test.questions):
            return None
        
        return self.__test.questions[self.__currentQuestionID]





    def reset(self):
        self.__currentQuestionID = -1
        self.__selections = {}
        self.clearSelections()



    
    def loadTest(self, test: TestData):
        if self.__currentQuestionID != -1:
            self.reset()

        self.__test = test
        self.ui.testLabel.setText(test.name)
        self.questionBar.setBarSize(len(test.questions))
         
        for index, question in enumerate(test.questions):
            question.changeID(index + 1)

        self.questionBar.setSelected(1)





    def saveSelection(self):
        question = self.getCurrentQuestion()
        
        if question is None or self.__currentQuestionID == -1:
            return
        
        self.__selections[question.ID] = []

        for i in range(1, self.__answerCount + 1):
            if self.__answerWidgets[i].isSelected():
                self.__selections[question.ID].append(i)




    
    def clearSelections(self):
        for i in self.__answerWidgets:
            if self.__answerWidgets[i].isSelected():
                self.__answerWidgets[i].setSelected(False)
            self.__answerWidgets[i].hide()

        self.__lastSelectedAnswer = None
        self.__answerCount = 0

 



    def nextQuestion(self):
        question = self.getNextQuestion()       

        if question is not None:
            self.questionBar.setSelected(question.ID)
            
    

    
    
    def previousQuestion(self):
        question = self.getPreviousQuestion()       

        if question is not None:
            self.questionBar.setSelected(question.ID)



    def addAnswer(self, answer, isSelected = False):
        self.__answerCount += 1

        if self.__answerCount <= self.__answerWidgetCount:
            answerWidget = self.__answerWidgets[self.__answerCount]

            if answerWidget.isHidden():
                answerWidget.show()    

        else:
            self.__answerWidgetCount += 1

            answerWidget = TVAnswerLabel(self.ui.answersFrame)
            answerWidget.clicked.connect(self.__onAnswerSelect)

            self.__answerWidgets[self.__answerWidgetCount] = answerWidget
            self.ui.answersFrameLayout.addWidget(answerWidget)


        
        if isSelected:
            self.__lastSelectedAnswer = answerWidget

        answerWidget.setText(answer)
        answerWidget.setSelected(isSelected)




    def getResultViewerData(self) -> tuple[TestData, dict[int, list]]:
        self.saveSelection()
        return (self.__test, self.__selections.copy())

    



    def __markQuestionSwitch(self):
        if self.questionBar.isQuestionMarked():
            self.questionBar.unmarkQuestion()
            self.ui.markBtn.setText("Mark")
        else:
            self.questionBar.markQuestion()
            self.ui.markBtn.setText("Unmark")
    













if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = TestViewer()

    sys.exit(app.exec())