# Generated by Django 5.1.7 on 2025-03-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='item_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
