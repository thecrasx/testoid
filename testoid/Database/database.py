from testoid.Database.sqlite_database import SQLiteDB
import testoid.Database.schema as db_schema
from testoid.TestMaker.test_data import TestData
from testoid.QuestionMaker.question_data import QuestionData



db_path = "./testoid/Database/db/mydb.db"
db_aws_path = "./testoid/Database/db/aws.db"


# TODO: Implement the error for duplication
class Database(SQLiteDB):
    def __init__(self, database: str):
        super().__init__(database)

        self.execute(db_schema.test)
        self.execute(db_schema.question)
        self.execute(db_schema.answer)



    

    def __listToCSV(self, _list: list) -> str:
        out: str = ""

        for item in _list:
            out += f"{item},"

        return out[:-1]
    




    def __processTest(self, db_fetch: tuple) -> TestData | None:
        if db_fetch is None:
            return None
        
        if type(db_fetch) is tuple:
            if len(db_fetch) != 8:
                raise ValueError()
        else:
            raise TypeError()
        
        test = TestData()
        test.name = db_fetch[1]
        test.author = db_fetch[2]
        test.category = db_fetch[3]

        for question_id in db_fetch[4].split(','):
            question = self.getQuestionByID(int(question_id))
            
            if question is not None:
                test.questions.append(question)

        test.pointsToPass = db_fetch[5]
        test.validAnswers = db_fetch[6]
        test.maxMistakes = db_fetch[7]

        return test
    




    def __processQuestion(self, db_fetch: tuple) -> QuestionData | None:
            if db_fetch is None:
                return None
            
            if type(db_fetch) is tuple:
                if len(db_fetch) != 8:
                    raise ValueError()
            else:
                raise TypeError()

            question = QuestionData(db_fetch[0])
            question.question = db_fetch[1]
            question.category =  db_fetch[2]
            question.difficulty = db_fetch[3] 
            question.points = db_fetch[4]
            correct_answers = db_fetch[6]

            for answer_id in db_fetch[5].split(','):
                if answer_id != "":
                    answer = self.getAnswerByID(int(answer_id))

                    if answer != "":
                        is_correct = True if answer_id in correct_answers else False
                        question.addAnswer(answer, is_correct)

            question.answerType = db_fetch[7]

            return question
 




    def __fetchTest(self) -> TestData | None:
        data = self.fetchOne()
        return self.__processTest(data)





    def __fetchQuestion(self) -> QuestionData | None:
            data = self.fetchOne()
            return self.__processQuestion(data)





    def addTest(self, test: TestData) -> bool:
        if type(test) is not TestData:
            raise TypeError("addTest requires TestData type as input")
        

        question_count = len(test.questions)
        question_ids: list[int] = []
        question_ids_csv: str = ""



        if question_count > 0:
            self.execute("SELECT COUNT(id) FROM Question") # Gets question count


            # question id = last question id in db
            question_id: int = self.fetchOne()[0] # returns tuple[int] - (0, )

            for question in test.questions:
                    out = self.addQuestion(question)

                    if out > 0:
                        question_ids.append(out)

                    elif out == 0:
                        question_id += 1
                        question_ids.append(question_id)

            question_ids.sort()
            question_ids_csv = self.__listToCSV(question_ids)
        

        success = self.execute(
            f"""INSERT INTO Test (name, author, category, question_ids, points_to_pass, valid_answers, max_mistakes)
            VALUES (\"{test.name}\", \"{test.author}\", \"{test.category}\", \"{question_ids_csv}\", 
            {test.pointsToPass}, {test.validAnswers}, {test.maxMistakes})"""
        )

        return self.commitOnExecutionSuccess(success)
    




    def addQuestion(self, question: QuestionData) -> int:
        """
        Args:
            - question: QuestionData
        
        Return:
            - returns question id if there is a duplication
            - returns 0 on execution success
            - returns -1 on execution fail
        """


        if type(question) is not QuestionData:
            raise TypeError("addQuestion requires QuestionData type as input")
        

        answer_count: int = len(question.answers)
        answer_ids: list[int] = []
        correct_answer_ids: list[int] = []

        answer_ids_csv: str = ""
        correct_answer_ids_csv: str = ""


        if answer_count > 0:
            self.execute("SELECT COUNT(id) FROM Answer") # Gets answer count


            # answer id = last answer id in db
            answer_id: int = self.fetchOne()[0] # returns tuple[int] - (0, )

            for answer, is_correct in question.answers:
                    out = self.addAnswer(answer)

                    if out > 0:
                        answer_ids.append(out)

                        if is_correct:
                            correct_answer_ids.append(out)

                    elif out == 0:
                        answer_id += 1
                        answer_ids.append(answer_id)

                        if is_correct:
                            correct_answer_ids.append(answer_id)

            answer_ids.sort()
            correct_answer_ids.sort()
            answer_ids_csv = self.__listToCSV(answer_ids)
            correct_answer_ids_csv = self.__listToCSV(correct_answer_ids)

        
        question.question = question.question.replace("\"", "\"\"").replace("'", "''")

        
        # Check if there is a duplicate based on question and answer ids
        self.execute(f"SELECT * FROM Question WHERE question = \"{question.question}\" AND answer_ids = \"{answer_ids_csv}\"")

        out = self.fetchOne()
        if out:
            # TODO: raise a db_duplication error if user enables error_on_duplication function arg
            print("THIS IS A DUPLICATE!")
            return out[0] # Returns question id
        
        
        success = self.execute(
            f"""INSERT INTO Question (question, category, difficulty, points, answer_ids, correct_answer_ids, answer_type)
            VALUES (\"{question.question}\", \"{question.category}\", \"{question.difficulty}\", 
            {question.points}, \"{answer_ids_csv}\", \"{correct_answer_ids_csv}\", \"{question.answerType}\")"""
        )

        return 0 if self.commitOnExecutionSuccess(success) else -1





    def addAnswer(self, answer: str, explanation: str = "") -> int:
        """
        Args:
            - answer: str
            - explanation: str
        
        Return:
            - returns answer id if there is a duplication
            - returns 0 on execution success
            - returns -1 on execution fail
        """

        answer = answer.replace("\"", "\"\"").replace("'", "''")
        
        # Check for duplicate
        self.execute(f"SELECT * FROM Answer WHERE answer = \"{answer}\" AND explanation = \"{explanation}\"")

        data = self.fetchOne()

        if data:
            return data[0] # Returns answer id
        
        success = self.execute(f"INSERT INTO Answer (answer, explanation) VALUES (\"{answer}\", \"{explanation}\")")

        return 0 if self.commitOnExecutionSuccess(success) else -1
    




    def getTests(self) -> list[TestData]:
        self.execute(f"SELECT * FROM Test")
        
        tests = self.fetchAll()

        out: list[TestData] = []

        for test in tests:
            out.append(self.__processTest(test))

        return out





    def getTestByName(self, test_name: str) -> TestData | None:
        self.execute(f"SELECT * FROM Test WHERE name = \"{test_name}\"")
        return self.__fetchTest()
    

    def getTestByID(self, id: int) -> TestData | None:
        self.execute(f"SELECT * FROM Test WHERE id = {id}")
        return self.__fetchTest()









    def getQuestion(self, question: str) -> QuestionData | None:
        self.execute(f"SELECT * FROM Question WHERE question = \"{question}\"")
        return self.__fetchQuestion()
    
    def getQuestionByID(self, id: int) -> QuestionData | None:
        self.execute(f"SELECT * FROM Question WHERE id = {id}")
        return self.__fetchQuestion()





    def getAnswerByID(self, answer_id: int) -> str | None:
        self.execute(f"SELECT answer FROM Answer WHERE id = {answer_id}")

        data = self.fetchOne()

        if data:
            return data[0]
        
        return None
    




    def removeTest(self, test: TestData | str) -> bool:
        if type(test) is TestData:
            test = test.name

        success = self.execute(f"DELETE FROM Test WHERE name = \"{test}\"")
        return self.commitOnExecutionSuccess(success)





    def removeTestByID(self, id: int) -> bool:
        success = self.execute(f"DELETE FROM Test WHERE id = {id}")
        return self.commitOnExecutionSuccess(success)
    




    def removeQuestion(self, question: QuestionData | str) -> bool:
        if type(question) is QuestionData:
            question = question.question

        success = self.execute(f"DELETE FROM Question WHERE question = \"{question}\"")
        return self.commitOnExecutionSuccess(success)





    def removeQuestionByID(self, id: int) -> bool:
        success = self.execute(f"DELETE FROM Question WHERE id = {id}")
        return self.commitOnExecutionSuccess(success)






    def removeAnswer(self, answer: str) -> bool:
        success = self.execute(f"DELETE FROM Answer WHERE answer = \"{answer}\"")
        return self.commitOnExecutionSuccess(success)





    def removeAnswerByID(self, id: int) -> bool:
        success = self.execute(f"DELETE FROM Answer WHERE id = {id}")
        return self.commitOnExecutionSuccess(success)











if __name__ == "__main__":
    db = Database(db_path)

    test = TestData()
    test.name = "What"
    test.author = "Me"
    test.category = "test"
    test.pointsToPass = 120
    test.validAnswers = 4
    test.maxMistakes = 1

    question = QuestionData()
    question.question = "What is good?"
    question.answers = [("It is", False), ("Something", True), ("Nothing", False)]
    question.answerType = "Multiple Choice"

    question2 = question.copy()
    question2.question = "What is bad?"

    test.questions = [question, question2]
    # db.addTest(test)



    db.close()

