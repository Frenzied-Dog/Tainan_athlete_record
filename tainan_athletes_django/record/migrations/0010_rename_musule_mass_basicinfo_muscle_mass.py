# Generated by Django 5.1.2 on 2024-12-28 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0009_alter_racerecord_proof_alter_racerecord_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicinfo',
            old_name='musule_mass',
            new_name='muscle_mass',
        ),
    ]
