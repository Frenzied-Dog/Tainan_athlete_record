# Generated by Django 5.1.2 on 2024-11-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_hurtrecord_injure_date_basicinfo_physicaltest'),
    ]

    operations = [
        migrations.AddField(
            model_name='racerecord',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/proof/'),
        ),
    ]
