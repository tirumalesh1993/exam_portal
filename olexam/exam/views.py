from django.shortcuts import render
from .models import Question, Exams
import json
from django.contrib.auth.decorators import login_required


def home(request):
    exam = Exams.objects.get(id=1)
    questions = exam.questions.all()
    return render(request, 'exam/home.html', context={'questions': questions})


@login_required
def exam_admin(request):
    return render(request, 'exam/exam_admin.html')
