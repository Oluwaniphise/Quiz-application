from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Subject model is redundant for now, course question and choice should do...

"""

"""

class Course(models.Model):
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
    user_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} is {1}".format(self.user_choice, self.is_correct)

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_score = models.IntegerField()


