# Generated by Django 3.0.8 on 2020-07-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200716_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_exp',
            field=models.BooleanField(default=False),
        ),
    ]
