# Generated by Django 4.0.6 on 2022-07-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_folder_document_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='folder',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
