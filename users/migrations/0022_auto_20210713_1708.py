# Generated by Django 3.0 on 2021-07-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20210713_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
