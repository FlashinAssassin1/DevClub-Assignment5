# Generated by Django 4.0.6 on 2022-07-29 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_alter_quiz_duration_alter_quizattempt_time_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='New Quiz', max_length=50),
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]