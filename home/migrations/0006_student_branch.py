# Generated by Django 4.2.10 on 2024-02-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.TextField(default='CSE'),
        ),
    ]
