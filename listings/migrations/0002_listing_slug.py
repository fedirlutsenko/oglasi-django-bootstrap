# Generated by Django 4.1.1 on 2022-10-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
    ]
