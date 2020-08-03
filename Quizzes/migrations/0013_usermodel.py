# Generated by Django 3.0.6 on 2020-07-31 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quizzes', '0012_auto_20200730_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizzes.UserChoice')),
            ],
        ),
    ]
