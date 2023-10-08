from testoid.QuestionMaker.Answer.answer import Answer

class AnswerType:
    CHOICE = "Multiple Choice"
    RESPONSE = "Multiple Response"



class Answers:
    def __init__(self, parent, layout = None) -> None:
        self.__hasLayout = True if layout else False

        self.parent = parent
        self.layout = layout
        
        self.answerType = AnswerType.CHOICE
        self.__widgets = []
        self.__widgetCount = 0
        self.__answerCount = 0


    @property
    def answerCount(self) -> int:
        return self.__answerCount





    def __onAnswerSelect(self, answer: Answer, isSelected: bool):
        if not isSelected:
            return 

        if self.answerType is AnswerType.CHOICE:
            for _answer in self.__widgets:
                if _answer is not answer:
                    _answer.setSelected(False)





    def __onAnswerRemove(self, answer: Answer):
        self.__answerCount -= 1
        answer.hide()
        answer.clear()
    
        # Removes 10 unused widgets if there is more than 15 active widgets
        if self.__answerCount <= self.__widgetCount - 10 and self.__widgetCount >= 15:
            for widget in self.__widgets:
                if widget.isHidden():
                    self.__widgets.remove(widget)





    def __isAnswerEmpty(self, text: str) -> bool:
        if len(text) == 0 or text.isspace():
            return True
        else:
            return False





    def setAnswerType(self, answer_type: str | AnswerType):
        if type(answer_type) is str:
            if answer_type == AnswerType.CHOICE:
                answer_type = AnswerType.CHOICE
            else:
                answer_type  = AnswerType.RESPONSE
        
        self.answerType = answer_type

        if answer_type is AnswerType.CHOICE:
            for _answer in self.__widgets:
                if _answer.isSelected():
                    _answer.setSelected(False)





    def clear(self):
        self.__answerCount = 0

        for widget in self.__widgets:
            if not widget.isHidden():
                widget.hide()
                widget.clear()





    def addAnswer(self):
        self.__answerCount += 1

        if self.__answerCount > self.__widgetCount:
            answer = Answer(self.parent)
            answer.selected.connect(self.__onAnswerSelect)
            answer.removed.connect(self.__onAnswerRemove)

            self.__widgetCount += 1
            self.__widgets.append(answer)

            if self.__hasLayout:
                self.layout.addWidget(answer)

        else:
            for widget in self.__widgets:
                if widget.isHidden():
                    widget.show()
                    break





    def loadAnswers(self, answers: list[tuple[str, int]] = [], resetAnswersOnEmptyList = True):
        answerCount = len(answers)

        if answerCount == 0:
            if resetAnswersOnEmptyList:
                self.clear()
            return

        adif =  self.__answerCount - answerCount
        answerIndex = 0

        if adif >= 0:
            # print("- This question has enough visible answers")
            for widget in self.__widgets:

                # HIDE THE REMAINING VISIBLE WIDGETS (ANSWERS)
                if answerIndex >= answerCount:
                    if widget.isVisible():
                        widget.clear()
                        widget.hide()

                else:
                    if widget.isVisible():
                        widget.setText(answers[answerIndex][0])
                        widget.setSelected(answers[answerIndex][1])

                        answerIndex += 1

            # if adif != 0:
            #     print(f"    - {adif} are hidden")


        else:
            # print("- This question doesn't have enough visible answers")
            wdif = self.__widgetCount - answerCount

            if wdif < 0:
                # print(f"    - Added Widgets: {wdif * -1}")
                for i in range(wdif * -1):
                    self.addAnswer()


            hiddenRevealed = 0
            for widget in self.__widgets:

                if hiddenRevealed <= self.__widgetCount - self.__answerCount:
                    if widget.isHidden():
                        widget.setVisible(True)
                        hiddenRevealed += 1


                if widget.isVisible():
                    widget.setText(answers[answerIndex][0])
                    widget.setSelected(answers[answerIndex][1])

                    answerIndex += 1

                    if answerIndex >= answerCount:
                        break


            # if hiddenRevealed != 0:
                # print(f"    - {hiddenRevealed} widgets are revealed")

        # print()
        self.__answerCount = answerCount





    def getSelection(self, allowEmptySelection = True) -> list[str]:
        selected = []

        for widget in self.__widgets:
            if widget.isSelected():
                text = widget.getText()

                if not allowEmptySelection:
                    if not self.__isAnswerEmpty(text):
                        selected.append(text)
                else:
                    selected.append(text)

        return selected





    def getResults(self) -> list[tuple[str, bool]]:
        results = []

        for widget in self.__widgets:
            if not widget.isHidden():
                text = widget.getText()

                if not self.__isAnswerEmpty(text):
                    results.append((text, widget.isSelected()))

        return results

    
    
 