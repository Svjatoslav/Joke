# Generated by Django 4.1.2 on 2022-12-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0003_addition_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
