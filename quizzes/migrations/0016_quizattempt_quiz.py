# Generated by Django 4.0.6 on 2022-07-30 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0015_remove_quizattempt_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizattempt',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz'),
            preserve_default=False,
        ),
    ]
