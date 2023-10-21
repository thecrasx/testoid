from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.Overview.QuestionOverview.question_overview_ui import Ui_QuestionOverview
from testoid.Tools.stylesheet import load as ssLoad


class _Signals(QObject):
    jumpToQuestionClicked = Signal(int)


class QuestionOverview(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_QuestionOverview()
        self.ui.setupUi(self)

        self.__signals = _Signals(self)
        self.jumpToQuestionClicked = self.__signals.jumpToQuestionClicked
        self.jumpToQuestionSignalConnected: bool = False 

        self.ui.jumpToQuestionBtn.setStyleSheet(ssLoad("jump-question-button"))
        self.ui.jumpToQuestionBtn.clicked.connect(self.__onJumpToQuestionClick)


        # Close design labels
        self.ui.userAnswerLabel.close()
        self.ui.correctAnswerLabel.close()

        self.__userAnswers: list[QLabel] = []
        self.__correctAnswers: list[QLabel] = []
        self.__number: int = -1

        self.show()


    
    def __answerLabel(self, parent, text: str) -> QLabel:
        font = QFont()
        font.setFamilies([u"Iosevka NF Medium"])
        font.setPointSize(12)

        answer = QLabel(parent)
        answer.setText('- ' + text)
        answer.setFont(font)
        answer.setWordWrap(True)

        return answer
    

    def __onJumpToQuestionClick(self):
        self.jumpToQuestionClicked.emit(self.__number)


    @property
    def number(self) -> int:
        return self.__number


    def hideUserAnswers(self):
        self.ui.userAnswersRegion.hide()

    def showUserAnswers(self):
        self.ui.userAnswersRegion.show()
    
    def hideCorrectAnswers(self):
        self.ui.correctAnswersRegion.hide()

    def showCorrectAnswers(self):
        self.ui.correctAnswersRegion.show()



    def setText(self, text: str):
        self.ui.questionLabel.setText(text)

    def setNumber(self, num: int):
        self.__number = num
        self.ui.questionNumberLabel.setText(str(num))



    def addUserAnswer(self, text: str):
        _stylesheet: str = ("QLabel {\n"
                           "color: #D6C5E3;\n"
                           "padding: 0px;\n"
                           "}\n")


        answer = self.__answerLabel(self.ui.userAnswersFrame, text)
        answer.setStyleSheet(_stylesheet)
        self.ui.userAnswersFrameLayout.addWidget(answer)

        self.__userAnswers.append(answer)




    def addCorrectAnswer(self, text: str):
        _stylesheet: str = ("QLabel {\n"
                           "color: #DFC3F4;\n"
                           "padding: 0px;\n"
                           "}\n")
        
        answer = self.__answerLabel(self.ui.correctAnswersFrame, text)
        answer.setStyleSheet(_stylesheet)
        self.ui.correctAnswersFrameLayout.addWidget(answer)

        self.__correctAnswers.append(answer)


    def removeUserAnswers(self):
        for answer in self.__userAnswers:
            answer.close()

        self.__userAnswers = []
        

    def removeUserAnswerByIndex(self, index: int):
        if index < 0 or index > len(self.__userAnswers) - 1:
            raise ValueError()
        
        self.__userAnswers[index].close()

    
    def removeUserAnswerByText(self, text: str):
        for answer in self.__userAnswers:
            if text == answer.text():
                answer.close()
                break




    def removeCorrectAnswers(self):
        for answer in self.__correctAnswers:
            answer.close()


        self.__correctAnswers = []



    def removeCorrectAnswerByIndex(self, index: int):
        if index < 0 or index > len(self.__correctAnswers) - 1:
            raise ValueError()
        
        self.__correctAnswers[index].close()



    def removeCorrectAnswerByText(self, text: str):
        for answer in self.__correctAnswers:
            if text == answer.text():
                answer.close()
                break



    def getUserAnswerByIndex(self, index: int) -> QLabel:
        if index < 0 or index > len(self.__userAnswers) - 1:
            raise ValueError()

        return self.__userAnswers[index]
    

    def getUserAnswerByText(self, text: str) -> QLabel:
        for answer in self.__userAnswers:
            if text == answer.text():
                return answer



    def getCorrectAnswerByIndex(self, index: int) -> QLabel:
        if index < 0 or index > len(self.__correctAnswers) - 1:
            raise ValueError()

        return self.__correctAnswers[index]


    def getCorrectAnswerByText(self, text: str) -> QLabel:
        for answer in self.__correctAnswers:
            if text == answer.text():
                return answer











if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = QuestionOverview()

    sys.exit(app.exec())