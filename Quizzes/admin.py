from django.contrib import admin
from .models import Course, Question, Choice, UserScore, UserChoice

admin.site.register(UserChoice)
admin.site.register(UserScore)
admin.site.register(Course)




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class UserChoiceInline(admin.TabularInline):
    model = UserChoice



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

