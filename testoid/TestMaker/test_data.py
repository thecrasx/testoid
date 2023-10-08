from testoid.QuestionMaker.question_data import QuestionData
from typing import Self





class TestData:
    def __init__(self) -> None:
        self.name: str = ""
        self.author: str = ""
        self.category: str = ""
        self.tags: list[str] = []

        self.timeToFinish = None
        self.pointsToPass: int = 0
        self.validAnswers: int = 0
        self.maxMistakes: int = 0

        self.questions: list[QuestionData] = []


    def copy(self) -> Self:
        test = TestData()
        test.name = self.name
        test.author = self.author
        test.category = self.category
        test.tags = self.tags.copy()
        test.timeToFinish = self.timeToFinish
        test.pointsToPass = self.pointsToPass
        test.validAnswers = self.validAnswers
        test.maxMistakes = self.maxMistakes
        test.questions = []

        for q in self.questions:
            test.questions.append(q.copy())

        return test
