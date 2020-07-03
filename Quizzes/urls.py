from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name="questions"),
    path('courses/', views.courses_list, name="courses-list"),
    path('courses/<course>/', views.course_detail, name="course-detail"),
    path('courses/<course>/quiz/<int:pk>/', views.course_quiz, name="course-quiz"),
]