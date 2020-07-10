from django.contrib import admin
<<<<<<< HEAD
from .models import Subject, Course, Question, UserChoice, Answer, Choice
=======
from .models import Course, Question, Choice
>>>>>>> Quiz-application-dev

# Register your models here.

admin.site.register(Course)
admin.site.register(UserChoice)




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]