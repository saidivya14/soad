# Generated by Django 3.0.7 on 2020-07-02 05:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 5, 8, 0, 105295, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
