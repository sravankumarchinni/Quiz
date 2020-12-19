Test_taken_by =input("Enter your name:") 
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a) Red\n(b) Green\n(c) Orange \n Your answer: ",
     "What color are bananas?\n(a) Red\n(b) Green\n(c) Yellow \n Your answer: ",
     "What color are India?\n(a) Delhi\n(b) Mumbai\n(c) Calcutta \n Your answer: ",
     "What color are Pakistan?\n(a) Islamabad\n(b) karachi\n(c) Hyderabad \n Your answer: ",
     "What color are Python?\n(a) Function oriented\n(b) OOP\n(c) Procedure oriented\n Your answer: ",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print( Test_taken_by,"you got", score,"Correct answers", "out of", len(questions))

run_quiz(questions)		