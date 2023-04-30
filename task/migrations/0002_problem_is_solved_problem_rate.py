# Generated by Django 4.2 on 2023-04-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='is_solved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='rate',
            field=models.IntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
    ]