# Generated by Django 5.0.4 on 2024-04-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]