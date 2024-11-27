# Generated by Django 5.1.2 on 2024-11-23 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user_data', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ForeignKey(default=1, help_text='使用者群組', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.group'),
        ),
    ]