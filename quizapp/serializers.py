from .models import QuizApp_category,QuizApp_quiz,QuizApp_question,QuizApp_answer
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    
    model = QuizApp_category
    fields = (
    'name',
    
    )
    
    
class QuizSerializers(serializers.ModelSerializer):
    model = QuizApp_quiz
    fields = (
    'category',
    'title',
    
    )
    
    
class QuestionSerializers(serializers.ModelSerializer):
    model = QuizApp_question
    fields = (
    'quiz',
    'title',
    'difficulty',
    
    
    
    )
    
   

class AnswerSerializers(serializers.ModelSerializer):
    model = QuizApp_answer
    fields = (
    
    'answer_text',
    'is_right',
    'question',
    
    
    
    )
    
   