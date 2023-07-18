# Generated by Django 4.2.3 on 2023-07-17 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_alter_postcomments_timestamp_alter_property_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='property_type',
            new_name='propertyType',
        ),
        migrations.AlterField(
            model_name='postcomments',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 0, 6, 0, 184952)),
        ),
    ]