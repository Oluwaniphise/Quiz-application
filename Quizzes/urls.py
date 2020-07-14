from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_list, name="courses-list"),
    path('courses/<course>/', views.course_detail, name="course-detail"),
    path('courses/<course_title>/questions/', views.course_quiz, name="course-quiz"),
]