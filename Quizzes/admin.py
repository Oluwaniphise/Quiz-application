from django.contrib import admin
from .models import Subject, Course, Question, Choice

# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]