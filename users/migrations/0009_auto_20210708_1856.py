# Generated by Django 3.0 on 2021-07-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210708_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default', upload_to='profilepic'),
        ),
    ]