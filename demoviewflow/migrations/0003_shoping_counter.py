# Generated by Django 3.2.11 on 2022-02-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoviewflow', '0002_auto_20220206_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoping',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]
