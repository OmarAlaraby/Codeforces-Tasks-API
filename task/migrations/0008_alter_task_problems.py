# Generated by Django 4.2 on 2023-04-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_remove_task_problems_task_problems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='problems',
            field=models.ManyToManyField(blank=True, related_name='Task', to='task.problem'),
        ),
    ]
