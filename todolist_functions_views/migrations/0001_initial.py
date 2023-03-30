# Generated by Django 4.0.2 on 2022-05-14 12:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=40)),
                ('status', models.CharField(choices=[('TO_DO', 'TO_DO'), ('IN_PROGRESS', 'IN_PROGRESS'), (
                    'FINISHED', 'FINISHED')], default='TO_DO', max_length=30)),
                ('created_at', models.DateTimeField(
                    blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='todolist_functions_views.simpleuser')),
            ],
        ),
    ]
