from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/exam/room/<int:course_id>', consumers.ExamConsumer),
]
