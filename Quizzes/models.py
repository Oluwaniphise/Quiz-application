from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice_question = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField()


