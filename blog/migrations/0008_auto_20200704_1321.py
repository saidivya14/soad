# Generated by Django 3.0.7 on 2020-07-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='minprice',
            field=models.IntegerField(),
        ),
    ]
