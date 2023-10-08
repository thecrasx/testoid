from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from testoid.QuestionMaker.question_maker_ui import Ui_QuestionMaker
from testoid.QuestionMaker.QuestionListMenu.question_list_menu import QuestionListMenu
from testoid.QuestionMaker.question_data import QuestionData
from testoid.QuestionMaker.Answer.answers import Answers
from testoid.Options.difficulty_option import DifficultyOption
from testoid.Options.answer_type_option import AnswerTypeOption
from testoid.Tools.stylesheet import load as ssLoad




class _QuestionMakerStyleSheet:
    QUESTION_INPUT_NORMAL = (
        "QPlainTextEdit {\n"
        "    background-color: #4E4C6C;\n"
        "    border: none;\n"
        "    border-radius: 15%;\n"
        "    padding: 7px 10px 7px 10px;\n"
        "    color: #F1DADA;\n"
        "}\n"
    )

    QUESTION_INPUT_WARNING = (
        "QPlainTextEdit {\n"
        "    background-color: #4E4C6C;\n"
        "    border: 3px solid #EB5050;\n"
        "    border-radius: 15%;\n"
        "    padding: 4px 7px 4px 7px;\n"
        "    color: #F1DADA;\n"
        "}\n"
    )





class QuestionMaker(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_QuestionMaker()
        self.ui.setupUi(self)

        self.__setupUI()
        self.__hideDesignUI()

        self.answers = Answers(self.ui.answersFrame, self.ui.answersFrameLayout)
        self.ui.addAnswerBtn.clicked.connect(self.answers.addAnswer)

        self.ui.addAnswerBtn.setStyleSheet(ssLoad("add-answer-button"))

        # self.__sc = QShortcut(QKeySequence("ctrl+s"), self)
        # self.__sc.activated.connect(self.displayResults)


        self.__currentQuestion: QuestionData = None
        self.__currentQuestionWarning: bool = False

        self.__hidden: bool = False
        self.hideQuestionMaker()

        self.show()



    def hideQuestionMaker(self) -> None:
        if not self.__hidden:
            self.ui.mainFrame.hide()
            self.__hidden = True

    def showQuestionMaker(self) -> None:
        if self.__hidden:
            self.ui.mainFrame.show()
            self.__hidden = False
        


    
    def validateQuestions(self, questions: list[QuestionData] = None) -> bool:
        if questions is None:
            questions = self.getQuestions()

        invalid_question_ids: list[int] = []

        for question in questions:
            if not self.validateQuestion(question):
                invalid_question_ids.append(question.ID)

        print("IDs: ", invalid_question_ids)

        for iq in invalid_question_ids:
            self.questionListMenu.setWarning(iq)

            if self.__currentQuestion.ID == iq:
                self.ui.questionInput.setStyleSheet(_QuestionMakerStyleSheet.QUESTION_INPUT_WARNING)




        if len(invalid_question_ids) > 0:
            return False





    
    def validateQuestion(self, question: QuestionData | str) -> bool:
        """
        Checks if question is not whitespace string
        """

        if type(question) is QuestionData:
            question = question.question

        if len(question) != 0 and not question.isspace():
            return True
            
        return False



        




    
    def getQuestions(self) -> list[QuestionData]:
        self.__saveCurrentQuestion()
        return self.questionListMenu.getQuestions()





    def __hideDesignUI(self):
        self.ui.difficultyLabel.hide()
        self.ui.difficultyOptionFrame.hide()
        self.ui.answerTypeLabel.hide()
        self.ui.answerTypeOptionFrame.hide()





    def __setupUI(self):
        self.ui.difficulty = DifficultyOption(self.ui.difficultyFrame)
        self.ui.difficultyFrameLayout.addWidget(self.ui.difficulty)

        self.ui.answerType = AnswerTypeOption(self.ui.answerTypeFrame)
        self.ui.answerTypeFrameLayout.addWidget(self.ui.answerType)

        self.ui.answerType.changed.connect(
            lambda: self.answers.setAnswerType(
                self.ui.answerType.current
            )
        )

        # QUESTION LIST MENU
        self.questionListMenu = QuestionListMenu(self.ui.questionListMenuFrame)
        self.ui.questionListMenuFrameLayout.addWidget(self.questionListMenu)

        self.questionListMenu.ui.addQuestionBtn.clicked.connect(self.showQuestionMaker)

        self.ui.questionListMenuFrame.setMinimumWidth(200)
        self.questionListMenu.newQuestionAdded.connect(self.__onNewQuestionAdded)
        self.questionListMenu.editQuestionPressed.connect(self.__onQuestionEdit)

        self.ui.questionInput.textChanged.connect(self.__onQuestionInputChanged)





    def __onQuestionInputChanged(self):
        text = self.ui.questionInput.toPlainText()

        if self.__currentQuestionWarning and len(text) != 0 and not text.isspace():
            self.ui.questionInput.setStyleSheet(_QuestionMakerStyleSheet.QUESTION_INPUT_NORMAL)
            self.questionListMenu.clearWarning(self.__currentQuestion.ID)
            self.__currentQuestionWarning = False

        self.__currentQuestion.question = text





    def __saveCurrentQuestion(self):
        if self.__currentQuestion:
            self.__currentQuestion.answers = self.answers.getResults()
            self.__currentQuestion.answerType = self.answers.answerType
            self.__currentQuestion.difficulty = self.ui.difficulty.current
            self.__currentQuestion.points = self.ui.pointsInputBox.value()
            self.__currentQuestion.category = self.ui.categoryInput.text()
            self.questionListMenu.updateQuestionText(self.__currentQuestion)





    def clear(self):
        self.ui.questionInput.clear()
        self.answers.clear()

        self.ui.answerType.resetCurrentToDefault()
        self.ui.difficulty.resetCurrentToDefault()
        self.ui.categoryInput.clear()
        self.ui.pointsInputBox.setValue(0)





    def displayResults(self):
        for result in self.answers.getResults():
            print(result)





    # QUESTION LIST MENU SIGNALS
    def __onNewQuestionAdded(self, question):
        self.__saveCurrentQuestion()
        self.__currentQuestion = question

        self.clear()





    def __onQuestionEdit(self, question: QuestionData, warning: bool):
        if self.__currentQuestion is not question:
            self.__saveCurrentQuestion()
            self.__currentQuestion = question

            # Question
            self.ui.questionInput.setPlainText(question.question)

            # Answers
            self.ui.answerType.setOption(question.answerType)
            self.answers.loadAnswers(question.answers)

            # Points
            self.ui.pointsInputBox.setValue(question.points)

            # Category
            self.ui.categoryInput.setText(question.category)

            # Difficulty
            if question.difficulty:
                self.ui.difficulty.setOption(question.difficulty)


        if warning:
            self.ui.questionInput.setStyleSheet(_QuestionMakerStyleSheet.QUESTION_INPUT_WARNING)

        elif not self.__currentQuestionWarning:
            self.ui.questionInput.setStyleSheet(_QuestionMakerStyleSheet.QUESTION_INPUT_NORMAL)

        self.__currentQuestionWarning = warning




    






        















if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = QuestionMaker()

    sys.exit(app.exec())