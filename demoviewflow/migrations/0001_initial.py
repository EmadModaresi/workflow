# Generated by Django 3.2.11 on 2022-02-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0008_jsonfield_and_artifact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shoping',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.process')),
                ('shop_name', models.CharField(max_length=255)),
                ('buier_name', models.CharField(max_length=255)),
                ('approved', models.BooleanField(default=False)),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoviewflow.food')),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]