# Generated by Django 3.0 on 2020-11-21 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank='True', upload_to='courses/')),
                ('category', models.CharField(choices=[('Musical Instruments', 'Musical Instruments'), ('Photography', 'Photography'), ('Dance', 'Dance'), ('Painting', 'Painting'), ('Decoration', 'Decoration'), ('Cooking', 'Cooking')], max_length=300)),
                ('difficulty', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermidiate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('organisation', models.CharField(max_length=300)),
                ('instructor', models.CharField(max_length=300)),
                ('noofweeks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default1.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank='True', upload_to='items/')),
                ('category', models.CharField(choices=[('Bongodrum', 'Bongodrum'), ('Conga', 'Conga'), ('Doublebass', 'Doublebass'), ('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Sitar', 'Sitar'), ('Snare_drum', 'Snare_drum'), ('Trumpet', 'Trumpet'), ('Violin', 'Violin')], max_length=300)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]