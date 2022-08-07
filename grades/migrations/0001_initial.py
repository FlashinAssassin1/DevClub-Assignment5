# Generated by Django 4.0.6 on 2022-08-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
                ('grade', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csvfiles')),
            ],
        ),
    ]
