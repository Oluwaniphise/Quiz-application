# Generated by Django 3.0.6 on 2020-06-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='answer',
            field=models.BooleanField(default=False),
        ),
    ]
