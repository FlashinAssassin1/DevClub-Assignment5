# Generated by Django 4.0.6 on 2022-08-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='lecture_notes')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('visible_name', models.CharField(max_length=50)),
                ('filetype', models.ImageField(default='filetype_pics/unknown.jpg', upload_to='')),
            ],
        ),
    ]
