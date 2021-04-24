from django.contrib import admin
from .models import Question, Answer

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Answer)

"""
Using Inline. 
This allows us to body up different table together 
so that i can build data consecutively so that i can build data all at once
"""


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer',
        'is_correct'
    ]
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'updated_at'
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]
