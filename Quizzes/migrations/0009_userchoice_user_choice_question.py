# Generated by Django 3.0.6 on 2020-07-18 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0008_remove_userchoice_user_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='user_choice_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Quizzes.Question'),
            preserve_default=False,
        ),
    ]
