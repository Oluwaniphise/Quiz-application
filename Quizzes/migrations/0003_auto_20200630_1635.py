# Generated by Django 3.0.6 on 2020-06-30 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0002_auto_20200630_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='text',
            new_name='choice_text',
        ),
    ]
