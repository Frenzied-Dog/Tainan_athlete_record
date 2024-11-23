# Generated by Django 5.1.2 on 2024-11-23 09:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_initial'),
        ('user_data', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hurtrecord',
            name='injure_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='受傷日期'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.SmallIntegerField(help_text='年齡')),
                ('height', models.FloatField(help_text='身高')),
                ('weight', models.FloatField(help_text='體重')),
                ('BMI', models.FloatField(help_text='BMI')),
                ('musule_mass', models.FloatField(help_text='肌肉量')),
                ('body_fat', models.FloatField(help_text='體脂率')),
                ('test_date', models.DateField(help_text='測試日期')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('athlete', models.ForeignKey(help_text='運動員', on_delete=django.db.models.deletion.CASCADE, related_name='basic_info', to='user_data.userprofile')),
            ],
            options={
                'ordering': ['-athlete'],
            },
        ),
        migrations.CreateModel(
            name='PhysicalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vertical_jump', models.FloatField(blank=True, help_text='垂直跳 (cm)', null=True)),
                ('agility', models.FloatField(blank=True, help_text='敏捷性 (秒)', null=True)),
                ('grip_strength', models.FloatField(blank=True, help_text='握力', null=True)),
                ('sprint_30m', models.FloatField(blank=True, help_text='30M衝刺', null=True)),
                ('back_muscle_strength', models.FloatField(blank=True, help_text='背肌力', null=True)),
                ('aerobic_fitness', models.FloatField(blank=True, help_text='有氧適能', null=True)),
                ('test_date', models.DateField(help_text='測試日期')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('athlete', models.ForeignKey(help_text='運動員', on_delete=django.db.models.deletion.CASCADE, related_name='physical_test', to='user_data.userprofile')),
            ],
            options={
                'ordering': ['-athlete', 'test_date'],
            },
        ),
    ]
