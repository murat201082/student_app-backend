from django.contrib import admin
from .models import QuizApp_category, QuizApp_quiz, QuizApp_question, QuizApp_answer

# Register your models here.
admin.site.register(QuizApp_category)
admin.site.register( QuizApp_quiz)
admin.site.register(QuizApp_question)
admin.site.register(QuizApp_answer)

# class TocArticleInline(nested_admin.NestedStackedInline):
#     model = QuizApp_quiz
#     sortable_field_name = "position"

# class TocSectionInline(nested_admin.NestedStackedInline):
#     model = QuizApp_question
#     sortable_field_name = "position"
#     inlines = [TocArticleInline]
    
# class TocSectionOutline(nested_admin.NestedStackedInline):
#     model = QuizApp_answer
#     sortable_field_name = "position"
#     inlines = [TocArticleInline]

# class TableOfContentsAdmin(nested_admin.NestedModelAdmin):
#     inlines = [TocSectionOutline]

# admin.site.register(QuizApp_category, TableOfContentsAdmin)