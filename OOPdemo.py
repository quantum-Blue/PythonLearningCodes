
# Question
class Question:
    def __init__(self,text,choice,answer):
        self.text = text
        self.choices = choice
        self.answer = answer.lower()
    
    def checkAnswer(self,answer):
        return self.answer == answer   
    
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score=0
        self.questionIndex=0

    def getQuestions(self):
        return self.questions[self.questionIndex]
    
    def displayQuestions(self):
        question = self.getQuestions()
        print(f"Soru {self.questionIndex+1}: {question.text}")
        for q in question.choices:
            print('-'+q)
        answer =input("cevap: ")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question=self.getQuestions()
        if(question.checkAnswer(answer)):
            self.score +=1
        self.questionIndex +=1       
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()

    def showScore(self):
        print("score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion :
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,'*'))

q1=Question('En iyi programlama dili hangisidir?',['python','c#','javascript','java'],'python')
q2=Question('En populer programlama dili hangisidir?',['java','c#','javascript','python'],'python')
q3=Question('En cok kazandiran programlama dili hangisidir?',['c#','python','javascript','java'],'python')
q4=Question('En cok sevilen programlama dili hangisidir?',['c#','python','javascript','java'],'python')
q5=Question('En kolay programlama dili hangisidir?',['c#','python','javascript','java'],'python')
questions=[q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.loadQuestion()


