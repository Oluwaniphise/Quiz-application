# Generated by Django 3.0.6 on 2020-07-25 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0009_userchoice_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quizzes.Course'),
        ),
    ]
