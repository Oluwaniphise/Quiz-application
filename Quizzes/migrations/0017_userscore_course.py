# Generated by Django 3.0.6 on 2020-07-21 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0016_remove_userscore_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Quizzes.Course'),
            preserve_default=False,
        ),
    ]
