from django.shortcuts import render
from .models import QuizApp_category,QuizApp_quiz,QuizApp_question,QuizApp_answer
from .serializers import CategorySerializers,QuizSerializers,QuestionSerializers,AnswerSerializers
from rest_framework import viewsets


class CategoryViews(viewsets.ModelViewSet):
    queryset = QuizApp_category.objects.all()
    serializer_class = CategorySerializers

# Create your views here.
