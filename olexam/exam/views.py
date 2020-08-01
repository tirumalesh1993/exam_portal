from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Exams, ExamId
import json
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    exam = Exams.objects.get(id=1)
    exam_id = request.GET.get('id', 1)
    players = ExamId.objects.filter(exam_id=exam_id)
    questions = exam.questions.all()
    return render(request, 'exam/home.html', context={'questions': questions, 'players': players, 'exam_id': exam_id})


@login_required
def exam_admin(request):
    exam_id = request.GET.get('id', 1)
    return render(request, 'exam/exam_admin.html', {'exam_id': exam_id})


def user_login(request):
    next = request.GET.get('next', '/exam_admin/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next)
                else:
                    return HttpResponse('Disabled Login')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'exam/login.html', {'form': form})
