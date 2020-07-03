from django.contrib import admin
from .models import Subject, Course, Question, UserChoice, Answer, Choice

# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(UserChoice)




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]