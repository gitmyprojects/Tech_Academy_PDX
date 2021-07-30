# Generated by Django 3.2.5 on 2021-07-26 01:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='', max_length=20)),
                ('item_category', models.CharField(choices=[('breakfast', 'breakfast'), ('snack', 'snack'), ('dessert', 'dessert'), ('fast-food', 'fast-food'), ('sandwich', 'sandwich'), ('candy', 'candy'), ('beverage', 'beverage')], default='', max_length=20)),
                ('description', models.TextField(default='')),
            ],
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
    ]