# Generated by Django 3.2.23 on 2024-04-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.CharField(max_length=500)),
                ('task_status', models.BooleanField()),
                ('task_label', models.CharField(max_length=100)),
            ],
        ),
    ]
