# Generated by Django 3.0 on 2021-07-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/defualt.jpg', upload_to='media/profilepic'),
        ),
    ]
