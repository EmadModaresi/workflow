# Generated by Django 3.2.11 on 2022-02-06 08:38

from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('river', '0003_auto_20220206_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopingRiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('buier_name', models.CharField(max_length=255)),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoriver.food2')),
                ('state', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.state')),
            ],
        ),
    ]