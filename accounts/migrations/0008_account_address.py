# Generated by Django 4.1.1 on 2023-03-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
