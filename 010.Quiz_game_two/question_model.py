'''
How the model should look like?
atributes:
    text
    answer

example
new_question = Question(text,answer)

data model:
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
'''

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
        pass
