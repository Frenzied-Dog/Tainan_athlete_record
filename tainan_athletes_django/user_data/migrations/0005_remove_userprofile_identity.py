# Generated by Django 5.1.2 on 2024-11-21 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0004_remove_userprofile_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='identity',
        ),
    ]
