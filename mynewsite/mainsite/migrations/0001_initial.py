# Generated by Django 5.1.7 on 2025-03-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('brand_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='medium', max_length=10)),
            ],
            options={
                'ordering': ('-item_number',),
            },
        ),
    ]
