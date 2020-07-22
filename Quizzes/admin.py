from django.contrib import admin
from .models import Course, Question, Choice, UserChoice, UserScore

admin.site.register(UserChoice)
admin.site.register(UserScore)



# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class UserChoiceInline(admin.TabularInline):
    model = UserChoice



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

