# Generated by Django 3.0 on 2020-11-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='orgnaisation',
            new_name='organisation',
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank='True', upload_to='courses/'),
        ),
    ]
