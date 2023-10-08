from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.QuestionMaker.QuestionListMenu.question_list_menu_ui import Ui_QuestionListMenu
from testoid.QuestionMaker.question_data import QuestionData 
from testoid.Tools.stylesheet import load as ssLoad




class _QLMStyleSheet:
    NORMAL = ssLoad("question-list-menu-button-normal")
    SELECTED = ssLoad("question-list-menu-button-selected")
    WARNING = ssLoad("question-list-menu-button-warning")
    WARNING_SELECTED = ssLoad("question-list-menu-button-warning-selected")




class _CustomSignal(QObject):
    newQuestionAdded = Signal(object)
    editQuestionPressed = Signal(object, bool)





class QuestionListMenu(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_QuestionListMenu()
        self.ui.setupUi(self)

        self.ui.questionBtn.hide()

        # StyleSheet
        _QLMStyleSheet.NORMAL
        __ssButtonSelected = ssLoad("question-list-menu-button-selected")

        self.__customSignal = _CustomSignal()
        self.newQuestionAdded = self.__customSignal.newQuestionAdded
        self.editQuestionPressed = self.__customSignal.editQuestionPressed

        self.ui.addQuestionBtn.clicked.connect(self.addQuestion)

        self.__questions: dict[int, QPushButton] = {}
        self.__questionCount: int = 0
        
        self.__prevPressedButton = None


        self.show()





    def _display(self, question: QuestionData):
        print()
        print(question.question)



    def setWarning(self, question_id: int) -> None:
        button = self.__questions.get(question_id)

        if button is None:
            return
        
        button.setStyleSheet(_QLMStyleSheet.WARNING)
        button.warning = True

    
    def clearWarning(self, question_id: int) -> None:
        button = self.__questions.get(question_id)

        if button is None:
            return
        
        button.setStyleSheet(_QLMStyleSheet.NORMAL)
        button.warning = False





    def clear(self) -> None:
        for k in self.__questions:
            self.__questions[k].close()

        self.__questions = {}
        self.__questionCount = 0





    def __onButtonPressed(self, button):
        if self.__prevPressedButton:
            if self.__prevPressedButton.warning:
                self.__prevPressedButton.setStyleSheet(_QLMStyleSheet.WARNING)
            else:
                self.__prevPressedButton.setStyleSheet(_QLMStyleSheet.NORMAL)

        self.__prevPressedButton = button
        
        if button.warning:
            button.setStyleSheet(_QLMStyleSheet.WARNING_SELECTED)
        else:
            button.setStyleSheet(_QLMStyleSheet.SELECTED)

        self.editQuestionPressed.emit(button.question, button.warning)





    def getQuestions(self) -> list[QuestionData]:
        return [self.__questions[k].question for k in self.__questions]





    def addQuestion(self, question: QuestionData = None):
        if not question:
            self.__questionCount += 1
            question = QuestionData(self.__questionCount)


        if self.__prevPressedButton:
            self.__prevPressedButton.setStyleSheet(_QLMStyleSheet.NORMAL)

        button = QPushButton(self.ui.questionsFrame)
        button.setStyleSheet(_QLMStyleSheet.SELECTED)
        button.question = question
        button.warning = False

        self.__prevPressedButton = button

        # Signal
        button.clicked.connect(lambda: self.__onButtonPressed(button))

        
        button.setText(f"{question.ID}. {question.question[:30]}")
        self.__questions[question.ID] = button

        self.ui.questionsFrameLayout.addWidget(button, 0, Qt.AlignLeft)

        self.newQuestionAdded.emit(question)





    def saveQuestion(self, question: QuestionData):
        s_question = self.__questions.get(question.ID)

        if s_question:
            s_question.question = question.question
            s_question.answers = question.answers
            s_question.answerType = question.answerType





    def getQuestion(self, ID) -> QuestionData| None:
        return self.__questions.get(ID).question
    







    def updateQuestionText(self, question: QuestionData):
        if question.question:
            self.__questions[question.ID].setText(f"{question.ID}. {question.question[:15]}")












if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = QuestionListMenu()

    sys.exit(app.exec())