# Generated by Django 3.0.6 on 2020-07-18 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0007_auto_20200717_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoice',
            name='user_choice_question',
        ),
    ]
