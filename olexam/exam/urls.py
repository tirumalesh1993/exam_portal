from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exam_admin/', views.exam_admin, name='exam_admin'),
    path('login/', views.user_login, name='login')
]
