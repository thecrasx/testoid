


test = """CREATE TABLE IF NOT EXISTS Test (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    author TEXT,
    category TEXT,
    question_ids TEXT,
    points_to_pass INTEGER,
    valid_answers INTEGER,
    max_mistakes INTEGER

)"""

# answer_ids - IDs of answers stored as a text in the csv format
# correct_answer_ids - IDs of correct answers stored as a text in the csv format 
question = """CREATE TABLE IF NOT EXISTS Question (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    category TEXT,
    difficulty TEXT,
    points INTEGER,
    answer_ids TEXT,
    correct_answer_ids TEXT,
    answer_type TEXT NOT NULL
)"""

answer = """CREATE TABLE IF NOT EXISTS Answer (
    id INTEGER PRIMARY KEY,
    answer TEXT,
    explanation TEXT
)"""