# Generated by Django 5.1.2 on 2024-11-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0004_alter_userprofile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='emr_phone',
            field=models.CharField(blank=True, help_text='緊急聯絡電話', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='guardian',
            field=models.CharField(blank=True, help_text='監護人 (姓名/稱謂)', max_length=10, null=True),
        ),
    ]
