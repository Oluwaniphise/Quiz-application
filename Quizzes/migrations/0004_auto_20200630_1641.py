# Generated by Django 3.0.6 on 2020-06-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0003_auto_20200630_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=100),
        ),
    ]