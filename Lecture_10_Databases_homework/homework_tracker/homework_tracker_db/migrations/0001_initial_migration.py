# Generated by Django 3.2.3 on 2021-05-24 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('deadline', models.IntegerField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'homeworks',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework_tracker_db.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework_tracker_db.student')),
            ],
            options={
                'db_table': 'homework_results',
            },
        ),
    ]
