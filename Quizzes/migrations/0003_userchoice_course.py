# Generated by Django 3.0.6 on 2020-07-24 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0002_auto_20200723_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quizzes.Course'),
        ),
    ]
