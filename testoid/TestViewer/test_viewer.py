from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from testoid.TestViewer.test_viewer_ui import Ui_TestViewer
from testoid.TestMaker.test_data import TestData
from testoid.QuestionMaker.question_data import QuestionData
from testoid.TestViewer.QuestionBar.question_bar import QuestionBar
from testoid.TestViewer.tv_answer_label import TVAnswerLabel
from testoid.Overlay.test_overview_overlay import TestOverviewOverlay
from testoid.Overview.QuestionOverview.question_overview import QuestionOverview
from testoid.Tools.stylesheet import load as ssLoad
from random import shuffle




class TestViewer(QWidget):
    def __init__(self, parent: QWidget | None = None, mainWindow: QWidget = None):
        if mainWindow is None:
            raise TypeError("mainWindow argument missing")

        super().__init__(parent)

        self.ui = Ui_TestViewer()
        self.ui.setupUi(self)



        self.testOverviewOverlay = TestOverviewOverlay(mainWindow)
        self.testOverviewOverlay.setTitleBarOffset(mainWindow.ui.titleBarFrame)
        self.testOverviewOverlay.setParentResizeSignal(mainWindow.resized)
        self.testOverviewOverlay.testOverview.ui.closeBtn.clicked.connect(
            self.testOverviewOverlay.close
        )

        self.questionBar = QuestionBar(self.ui.questionBarFrame)
        self.ui.questionBarFrameLayout.addWidget(self.questionBar)
        self.questionBar.clicked.connect(self.__onQuestionBarClick)

        
        self.__answerCount: int = 0
        self.__answerWidgetCount = 0
        self.__answerWidgets: dict[int, TVAnswerLabel] = {}
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

        self.ui.prevBtn.setStyleSheet(ssLoad("tv-prev-btn"))
        self.ui.nextBtn.setStyleSheet(ssLoad("tv-next-btn"))
        self.ui.overviewBtn.clicked.connect(self.__showTestOverview)

        self.show()



    def __showTestOverview(self):
        self.saveSelection()
        self.testOverviewOverlay.show()

        if self.ui.finishBtn.isHidden():
            self.ui.finishBtn.show()


    
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



    def __onJumpToQuestionClick(self, question_number):
        # self.__setupQuestion(question)
        # question = self.getquestion(question_number)
        self.questionBar.setSelected(question_number)
        self.testOverviewOverlay.hide()





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
        if self.__currentQuestionID < len(self.__test.questions):
            if self.__currentQuestionID == len(self.__test.questions) - 1:
                if not self.ui.overviewBtn.isEnabled():
                    self.ui.overviewBtn.setEnabled(True)

            return self.__test.questions[self.__currentQuestionID]

        return None
        





    def reset(self):
        self.__currentQuestionID = -1
        self.__selections = {}
        self.clearSelections()


    
    def loadTest(self, test: TestData):
        if self.__currentQuestionID != -1:
            self.reset()

        self.__test = test
        self.testOverviewOverlay.testOverview.setupTest(test)
        self.ui.testLabel.setText(test.name)
        self.questionBar.setBarSize(len(test.questions), True, )
        self.questionBar.unmarkAllQuestions()
         
        for index, question in enumerate(test.questions):
            question.changeID(index + 1)
            shuffle(question.answers)

            qo = self.testOverviewOverlay.testOverview.getQuestionOverview(question.ID)
            if not qo.jumpToQuestionSignalConnected:
                qo.jumpToQuestionClicked.connect(self.__onJumpToQuestionClick)
                qo.jumpToQuestionSignalConnected = True

        self.questionBar.setSelected(1)
        
        self.ui.overviewBtn.setDisabled(True)
        self.ui.finishBtn.hide()









    def saveSelection(self):
        question = self.getCurrentQuestion()
        
        if question is None or self.__currentQuestionID == -1:
            return
        

        self.__selections[question.ID] = []
        questionOverview = self.testOverviewOverlay.testOverview.getQuestionOverview(question.ID)

        if questionOverview is not None:
            questionOverview.removeUserAnswers()


        for i in range(1, self.__answerCount + 1):
            if self.__answerWidgets[i].isSelected():
                self.__selections[question.ID].append(i)
                questionOverview.addUserAnswer(self.__answerWidgets[i].text())
                




    
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



    def setupOverview(self):
        pass
    













if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = TestViewer()

    sys.exit(app.exec())