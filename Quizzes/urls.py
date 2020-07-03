from django.urls import path
from . import views

urlpatterns = [
    path('questions/<que_id>/', views.questions, name="questions")
]