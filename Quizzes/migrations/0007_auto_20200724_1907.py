# Generated by Django 3.0.6 on 2020-07-25 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0006_question_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='course',
        ),
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.RemoveField(
            model_name='userchoice',
            name='course',
        ),
    ]
