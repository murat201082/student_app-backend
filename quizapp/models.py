from django.db import models

class QuizApp_category(models.Model):
    name = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.name
    
    
class QuizApp_quiz(models.Model):
    category = models.ForeignKey(QuizApp_category,on_delete=models.CASCADE,related_name='quizzes')
    title = models.CharField(max_length=50, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
    
class QuizApp_question(models.Model):
    quiz = models.ForeignKey(QuizApp_quiz,on_delete=models.CASCADE,related_name='questions')  
    
    DEGREE = (
        ("E", "easy"),
        ("M", "medium"),
        ("H", "hard"),
    )
    date_updated=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=60,primary_key=True)
    difficulty = models.CharField(max_length=3, choices=DEGREE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

class QuizApp_answer(models.Model):
    updated=models.DateTimeField(auto_now=True)
    answer_text = models.TextField(max_length=400)
    is_right = models.BooleanField(default=False)
    
    question = models.ForeignKey(QuizApp_question,on_delete=models.CASCADE,related_name='question')
    
    def __str__(self):
        return self.answer_text

     

