# Generated by Django 3.0.5 on 2020-07-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200701_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
    ]
