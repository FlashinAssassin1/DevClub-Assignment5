# Generated by Django 4.0.6 on 2022-07-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filetype',
            field=models.ImageField(default='filetype_pics/unknown.jpg', upload_to=''),
        ),
    ]
