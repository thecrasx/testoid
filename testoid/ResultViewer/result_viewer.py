from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.ResultViewer.result_viewer_ui import Ui_ResultViewer
from testoid.Overlay.mistakes_overview_overlay import MistakesOverviewOverlay
from testoid.TestMaker.test_data import TestData
from testoid.Tools.stylesheet import load as ssLoad

class ResultViewer(QWidget):
    def __init__(self, parent: QWidget | None = None, mainWindow: QWidget = None):
        if mainWindow is None:
            raise TypeError("mainWindow argument missing")

        super().__init__(parent)

        self.ui = Ui_ResultViewer()
        self.ui.setupUi(self)


        self.mistakesOverviewOverlay = MistakesOverviewOverlay(mainWindow)
        self.mistakesOverviewOverlay.setTitleBarOffset(mainWindow.ui.titleBarFrame)
        self.mistakesOverviewOverlay.setParentResizeSignal(mainWindow.resized)
        self.mistakesOverviewOverlay.mistakesOverview.ui.closeBtn.clicked.connect(
            self.mistakesOverviewOverlay.close
        )

        self.ui.showMistakesBtn.setStyleSheet(ssLoad("rv-mistake-viewer-btn"))
        self.ui.showMistakesBtn.clicked.connect(self.mistakesOverviewOverlay.show)


        self.show()



    def setupResults(self, _pass: bool, accuracy: int, mistakes: int, attempt: int, success_rate: int):
        text = "PASS" if _pass else "FAIL"
        self.ui.resultLabel.setText(text)

        self.ui.accuracyValueLabel.setText(str(accuracy) + "%")

        if mistakes == 0:
            self.ui.mistakesFrame.hide()
        else:
            self.ui.mistakesValueLabel.setText(str(mistakes))
            if self.ui.mistakesFrame.isHidden():
                self.ui.mistakesFrame.show()

        self.ui.attemptsValueLabel.setText(str(attempt))
        self.ui.successRateValueLabel.setText(str(success_rate) + "%")
    


    def setTestPassed(self, passed: bool):
        if passed:
            self.ui.resultLabel.setText("PASS")
        else:
            self.ui.resultLabel.setText("FAIL")




    def processTest(self, test: TestData, test_viewer_selections: dict[int, list]):
        self.mistakesOverviewOverlay.mistakesOverview.clear()
        mistakes = 0
        mistaken = False

        for question in test.questions:
            user_selection = test_viewer_selections.get(question.ID)

            if user_selection is not None:
                out = []
                for i in range(1, len(question.answers) + 1):
                    if i in user_selection:
                        out.append(True)
                    else:
                        out.append(False)

                user_selection = out


            valid_answers = []
            invalid_answers = []
            index = 0
            for answer, correct in question.answers:
                if user_selection is None:
                    if correct:
                        valid_answers.append(answer)
                    mistaken = True

                else:
                    if correct and user_selection[index]:
                        pass

                    elif not correct and not user_selection[index]:
                        pass
                    
                    else:
                        mistaken = True
                        if correct:
                            valid_answers.append(answer)

                        elif user_selection[index]:
                            invalid_answers.append(answer)

                index += 1

            if mistaken:
                self.mistakesOverviewOverlay.mistakesOverview.addMistake(
                    question.ID, question.question, valid_answers, invalid_answers
                )
                mistaken = False
                mistakes += 1 

        question_count = len(test.questions)
        accuracy = int((question_count - mistakes) / question_count * 100)
        
        _pass = True if accuracy >= 70 else False

        self.setupResults(_pass, accuracy, mistakes, 1, 100)


                












if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = ResultViewer()

    sys.exit(app.exec())