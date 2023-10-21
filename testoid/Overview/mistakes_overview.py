from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.Overview.overview_ui import Ui_Overview
from testoid.Overview.QuestionOverview.question_overview import QuestionOverview
from testoid.Tools.stylesheet import load as ssLoad





class MistakesOverview(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_Overview()
        self.ui.setupUi(self)
        self.ui.closeBtn.setStyleSheet(ssLoad("close-answer-button"))


        self.__mistakes: list[QuestionOverview] = []
        self.__mistakeCount: int = 0

        self.show()



    def mistakeCount(self) -> int:
        return self.__mistakeCount


    def clear(self):
        for i in range(self.__mistakeCount):
            self.__mistakes[i].close()

        self.__mistakes = []
        self.__mistakeCount = 0

        

    
    def addMistake(self, question_number: int, question: str, valid_answers: list[str], invalid_answers: list[str]):
        mistakeOverview = QuestionOverview(self.ui.questionsFrame)
        self.ui.questionsFrameLayout.addWidget(mistakeOverview)
        
        mistakeOverview.setNumber(question_number)
        mistakeOverview.setText(question)
        mistakeOverview.ui.jumpToQuestionBtn.close()

        for answer in invalid_answers:
            mistakeOverview.addUserAnswer(answer)

        for answer in valid_answers:
            mistakeOverview.addCorrectAnswer(answer)

        self.__mistakes.append(mistakeOverview)
        self.__mistakeCount += 1