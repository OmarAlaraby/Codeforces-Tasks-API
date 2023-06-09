# Generated by Django 4.2.1 on 2023-05-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_user_alter_problem_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Handle', models.CharField(max_length=255)),
                ('rate', models.IntegerField(db_index=True, default=800)),
                ('number_of_problems', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
