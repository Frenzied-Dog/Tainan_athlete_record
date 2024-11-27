# Generated by Django 5.1.2 on 2024-11-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTrainRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='訓練日期')),
                ('distance', models.FloatField(help_text='跑步距離 (公里)')),
                ('time', models.TimeField(help_text='跑步時間')),
                ('description', models.TextField(help_text='訓練描述', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-athlete', '-date'],
            },
        ),
        migrations.CreateModel(
            name='HurtRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='受傷日期')),
                ('injury_type', models.CharField(help_text='受傷部位', max_length=10)),
                ('description', models.TextField(help_text='受傷描述', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-athlete', 'date'],
            },
        ),
        migrations.CreateModel(
            name='RaceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='比賽日期')),
                ('race_name', models.CharField(help_text='比賽名稱', max_length=10)),
                ('description', models.TextField(help_text='比賽描述', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-athlete', '-date'],
            },
        ),
    ]
