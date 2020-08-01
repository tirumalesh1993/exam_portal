from django.contrib import admin
from .models import Exams, Question, ExamId

admin.site.register(ExamId)


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
    list_display = ['exam_name', 'no_of_ques', 'time_duration']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'option1', 'option2', 'option3', 'option4']
