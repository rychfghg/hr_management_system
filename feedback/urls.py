# feedback/urls.py
from django.urls import path
from .views import feedback_view, feedback_list

urlpatterns = [
    path('submit/', feedback_view, name='feedback_submit'),
    path('list/', feedback_list, name='feedback_list'),
]
