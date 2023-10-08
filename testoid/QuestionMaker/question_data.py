from typing import Self


class QuestionData:
    def __init__(self, ID: int = 0):
        self.__ID = ID

        self.question: str = ""

        # Answers - (answer, is_correct)
        self.answers: list[tuple[str, bool]] = []
        self.answerType: str = None

        self.category: str = ""
        self.difficulty: str = ""
        self.points: int = 0


    @property
    def ID(self) -> int:
        return self.__ID
    
    def changeID(self, id: int):
        self.__ID = id


    def addAnswer(self, answer: str, is_correct: bool) -> None:
        self.answers.append((answer, is_correct))




    def copy(self, ID: int = None) -> Self:
        if ID is not None:
            question = QuestionData(ID)
        else:
            question = QuestionData(self.__ID)

        question.question = self.question
        question.answers = self.answers
        question.answerType = self.answerType
        question.category = self.category
        question.points = self.points

        return question
    


    def __repr__(self) -> str:
        answer_count: int = 0
        answer_text: str = ""

        for answer, is_correct in self.answers:
            answer_count += 1
            answer_text += f"   Answer {answer_count}: {answer}\n"


        return (
            f"Question: {self.question}\n"
            f"Answers:\n"
            f"{answer_text}"
            f"-----------------------------\n"
            f"Answer Type: {self.answerType}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Category: {self.category}\n"
            f"Points: {self.points}\n"
        )

