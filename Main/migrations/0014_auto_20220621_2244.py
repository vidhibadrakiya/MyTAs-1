# Generated by Django 3.0.5 on 2022-06-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20220621_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.EmailField(max_length=30),
        ),
    ]
