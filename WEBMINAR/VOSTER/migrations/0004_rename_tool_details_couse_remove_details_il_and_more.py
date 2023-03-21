# Generated by Django 4.1.6 on 2023-03-15 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VOSTER', '0003_alter_details_il_alter_details_sp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='tool',
            new_name='couse',
        ),
        migrations.RemoveField(
            model_name='details',
            name='il',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
        migrations.AddField(
            model_name='details',
            name='ct',
            field=models.CharField(default=datetime.datetime(2023, 3, 15, 11, 11, 9, 885167, tzinfo=datetime.timezone.utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hw',
            name='start',
            field=models.DateField(default=datetime.datetime(2023, 3, 15, 11, 11, 34, 227624, tzinfo=datetime.timezone.utc), verbose_name='BEGAN FROM'),
            preserve_default=False,
        ),
    ]
